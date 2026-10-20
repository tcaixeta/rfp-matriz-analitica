#!/usr/bin/env python3
"""Monta a matriz analítica em Markdown a partir de um arquivo JSON de itens.

Uso (caminhos relativos à pasta da skill; use o caminho absoluto se estiver em outra pasta):
    python <pasta_da_skill>/scripts/build_matrix.py itens.json --out <processo>_Matriz_Analitica.md [--extracao <pasta>] [--xlsx]

O que o script faz por você (e por isso evita erros comuns de montagem):
- numera os IDs (D01-001, D01-002...) na ordem dos itens de cada documento;
- resolve referências entre itens: em "relacionados" e em textos, use a chave do
  item entre chaves, por exemplo "{d01_transicao}", e ela vira o ID final;
- preenche Documento e Versão/Data a partir da lista de documentos;
- escreve os rótulos de Severidade e Probabilidade e calcula a Criticidade
  (S × P, com a regra da Severidade 5), e usa "—" em Registro de cobertura e Oportunidade;
- limpa "|" e quebras de linha das células;
- gera a tabela de documentos e o bloco de status (✅ final ou ⏸ em andamento),
  com o total de itens e as pendências de cobertura;
- com --extracao, confere se cada citação entre aspas da coluna Evidência aparece
  no texto extraído (veja "Conferência de citações" abaixo);
- ao final, roda check_matrix.py e, com --xlsx, exporta para Excel.

FORMATO DO JSON
{
  "processo": "RFP nº 2026-017 — Banco Exemplo S.A.",
  "documentos": [ {...}, ... ],
  "itens": [ {...}, ... ],
  "status": {...}
}

documentos[] — um por arquivo, na ordem de processamento:
  codigo     "D01", "D02"... (o mesmo do inventário da extração)
  arquivo    nome do arquivo
  tipo       ex.: "RFP", "Anexo técnico", "Q&A e questionário"
  versao     versão ou data; "não informada" se não houver
  situacao   "processado" (padrão) · "pendente" (ainda não analisado, em montagem parcial)
             · "não anexado" (listado pelo usuário e não recebido) · "ilegível"
             Só "processado" conta em "Documentos processados" no status.

itens[] — um por linha da matriz, na ordem em que aparecem em cada documento:
  chave         identificador seu, em minúsculas com "_" (ex.: "d01_transicao"); vira o ID final
  doc           código do documento (ex.: "D01")
  secao, localizador, evidencia, tipo, dominio, descricao     obrigatórios
  obrigatoriedade  padrão "Informativo"      natureza   padrão "Explícita"
  s, p          inteiros de 1 a 5 (omitir em Registro de cobertura, Oportunidade / diferencial
                e itens com vigencia "Duplicado", que ficam com "—")
  impacto, framework, controle, associacao, pergunta, responsavel     padrão "—"
  relacionados  lista de chaves (ou IDs/rótulos externos, como "QT-03")
  vigencia      padrão "Vigente"             acao       padrão "Nenhuma (informativo)"
                "Duplicado" = mesmo conteúdo de outro item, sem informação nova: exige o original
                em "relacionados" e não recebe criticidade (ela fica só no original)
  Registro de cobertura recebe "—" em obrigatoriedade e natureza, salvo se informadas.
  pendencia     texto curto: o item entra em "Pendências de cobertura" no status final
  Em qualquer texto, "{chave}" é trocado pelo ID do item.

status — controla o bloco no fim do arquivo:
  {"final": true}                         → ✅ ANÁLISE CONCLUÍDA
  {"final": false, "proximo": "Anexo I (D02), a partir da seção 4",
   "parte": 2, "concluidos": 1}           → ⏸ ANÁLISE EM ANDAMENTO
  parte       número da parte (padrão 1)
  concluidos  documentos concluídos até aqui (padrão: quantos estão "processado")

MONTAGEM PARCIAL (status final = false)
Itens de documentos já processados podem citar chaves de itens de documentos
posteriores, que ainda não existem. Na montagem parcial isso não é erro: a
referência aparece como "(item posterior: chave)" e é resolvida quando o item
for incluído. Na montagem final, toda chave precisa existir.

CONFERÊNCIA DE CITAÇÕES (--extracao)
Cada trecho entre aspas da Evidência é procurado no texto extraído. Em linhas
com várias evidências ("A: ... · B: ..."), cada trecho é associado ao localizador
de mesmo rótulo ("A: p. 2 · B: §4.1"); só os trechos cujo localizador tem "(OCR)"
dependem de transcrição. Para conferi-los também, salve a transcrição da imagem
na pasta de extração como Dnn_pN_ocr.md (ex.: D01_p6_ocr.md). Sem transcrição,
esses trechos são pulados e contados no relatório.
"""
import argparse
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
COLUMNS = ["ID", "Documento", "Versão/Data", "Seção/Cláusula", "Localizador", "Evidência", "Tipo de item",
           "Domínio", "Descrição analítica", "Obrigatoriedade", "Natureza da evidência", "Severidade",
           "Probabilidade", "Criticidade", "Impacto para o proponente", "Framework/Referência",
           "Controle/Cláusula", "Tipo de associação", "IDs relacionados", "Status de vigência",
           "Ação recomendada", "Pergunta de esclarecimento", "Responsável interno sugerido"]
SEV = {1: "Insignificante", 2: "Menor", 3: "Moderada", 4: "Maior", 5: "Severa"}
PROB = {1: "Remota", 2: "Improvável", 3: "Possível", 4: "Provável", 5: "Quase certa"}
TIPOS = ["Requisito funcional / de serviço", "Requisito não funcional", "Critério eliminatório / de habilitação",
         "Critério de avaliação / pontuação", "Instrução de resposta", "Prazo / marco", "SLA / KPI",
         "Penalidade / multa / glosa", "Obrigação contratual", "Entregável", "Premissa do cliente", "Restrição",
         "Responsabilidade / dependência do cliente", "Dado de dimensionamento", "Contradição", "Ambiguidade",
         "Lacuna", "Risco para o proponente", "Requisito implícito", "Oportunidade / diferencial",
         "Registro de cobertura"]
NO_RATING = ("Registro de cobertura", "Oportunidade / diferencial")
FIELD = {"secao": "Seção/Cláusula", "localizador": "Localizador", "evidencia": "Evidência", "tipo": "Tipo de item",
         "dominio": "Domínio", "descricao": "Descrição analítica", "obrigatoriedade": "Obrigatoriedade",
         "natureza": "Natureza da evidência", "impacto": "Impacto para o proponente",
         "framework": "Framework/Referência", "controle": "Controle/Cláusula", "associacao": "Tipo de associação",
         "vigencia": "Status de vigência", "acao": "Ação recomendada", "pergunta": "Pergunta de esclarecimento",
         "responsavel": "Responsável interno sugerido"}
DEFAULTS = {"obrigatoriedade": "Informativo", "natureza": "Explícita", "vigencia": "Vigente",
            "acao": "Nenhuma (informativo)"}
KEY_RE = re.compile(r"^[a-z][a-z0-9_\-]*$")


def band(s, p):
    score = s * p
    label = "Baixa" if score <= 4 else "Média" if score <= 9 else "Alta" if score <= 15 else "Crítica"
    if s == 5 and label in ("Baixa", "Média"):
        label = "Alta"
    return f"{score} · {label}"


def clean(x):
    x = "—" if x is None or str(x).strip() == "" else str(x)
    return re.sub(r"\s*\n\s*", " · ", x.replace("|", "/")).strip()


def norm(t):
    t = unicodedata.normalize("NFC", t).lower()
    t = t.replace("“", '"').replace("”", '"').replace("’", "'").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", t)


def labeled(text):
    """Divide 'A: ... · B: ...' em {rótulo: trecho}. Sem rótulos, devolve {'': texto}."""
    parts = re.split(r"(?:^|\s·\s|\s)([A-E]):\s", text)
    if len(parts) < 3:
        return {"": text}
    out = {"": parts[0]} if parts[0].strip() else {}
    for i in range(1, len(parts) - 1, 2):
        out[parts[i]] = parts[i + 1]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("itens", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--extracao", type=Path, help="pasta gerada por extract_documents.py, para conferir citações")
    ap.add_argument("--xlsx", action="store_true", help="exportar também para Excel")
    a = ap.parse_args()
    data = json.loads(a.itens.read_text(encoding="utf-8"))
    docs = {d["codigo"]: d for d in data["documentos"]}
    st = data.get("status", {"final": True})
    final = st.get("final", True)
    errors, warns, pending_refs = [], [], set()

    # 1. IDs por documento, na ordem dos itens
    counters, ids = {}, {}
    for it in data["itens"]:
        d = it.get("doc")
        if d not in docs:
            errors.append(f"item {it.get('chave')}: documento '{d}' não está na lista de documentos.")
            continue
        counters[d] = counters.get(d, 0) + 1
        key = it.get("chave") or f"_{d}_{counters[d]}"
        if key in ids:
            errors.append(f"chave repetida: {key}")
        ids[key] = f"{d}-{counters[d]:03d}"
        it["_id"] = ids[key]

    def ref(k):
        if k in ids:
            return ids[k]
        if not final:
            pending_refs.add(k)
            return f"(item posterior: {k})"
        errors.append(f"referência a chave inexistente: {k}")
        return k

    def resolve(text):
        return re.sub(r"\{([A-Za-z0-9_\-]+)\}", lambda m: ref(m.group(1)), str(text))

    # 2. Linhas da matriz
    rows, pend = [], []
    order = list(docs)
    items = sorted([it for it in data["itens"] if "_id" in it], key=lambda it: (order.index(it["doc"]), it["_id"]))
    for it in items:
        rid = it["_id"]
        r = {"ID": rid, "Documento": docs[it["doc"]]["arquivo"], "Versão/Data": docs[it["doc"]].get("versao", "não informada")}
        for f, col in FIELD.items():
            r[col] = resolve(it.get(f, DEFAULTS.get(f, "—")))
        tipo = r["Tipo de item"]
        if tipo not in TIPOS:
            warns.append(f"{rid}: tipo '{tipo}' fora da taxonomia.")
        for f in ("secao", "localizador", "evidencia", "tipo", "dominio", "descricao"):
            if not str(it.get(f, "")).strip():
                errors.append(f"{rid}: campo obrigatório '{f}' vazio.")
        if tipo == "Registro de cobertura":
            # Cobertura não é exigência do cliente: sem obrigatoriedade nem natureza, salvo se informadas
            r["Obrigatoriedade"] = resolve(it.get("obrigatoriedade", "—"))
            r["Natureza da evidência"] = resolve(it.get("natureza", "—"))
        duplicate = r["Status de vigência"].startswith("Duplicado")
        if duplicate and not it.get("relacionados"):
            errors.append(f"{rid}: item Duplicado precisa do original em 'relacionados'.")
        if tipo in NO_RATING or duplicate:
            r["Severidade"] = r["Probabilidade"] = r["Criticidade"] = "—"
        else:
            s, p = it.get("s"), it.get("p")
            if s not in SEV or p not in PROB:
                errors.append(f"{rid}: 's' e 'p' devem ser inteiros de 1 a 5 (recebido s={s}, p={p}).")
                s, p = s if s in SEV else 3, p if p in PROB else 3
            r["Severidade"], r["Probabilidade"], r["Criticidade"] = f"{s} · {SEV[s]}", f"{p} · {PROB[p]}", band(s, p)
            if p != 3 and "probabilidade" not in r["Descrição analítica"].lower():
                errors.append(f"{rid}: Probabilidade {p} sem justificativa ('Probabilidade {p}: ...') na descrição.")
        rel = []
        for x in it.get("relacionados") or []:
            if x in ids or re.match(r"^D\d{2}-\d{3}$", x):
                rel.append(ids.get(x, x))
            elif KEY_RE.match(x):
                rel.append(ref(x))
            else:
                rel.append(x)  # rótulo externo, como "QT-03"
        r["IDs relacionados"] = " · ".join(rel) if rel else "—"
        if it.get("pendencia"):
            pend.append(f"{rid} ({resolve(it['pendencia'])})")
        rows.append(r)

    # 3. Conferência das citações contra o texto extraído, trecho a trecho
    skipped_ocr = 0
    if a.extracao:
        corpus = " ".join(norm(f.read_text(encoding="utf-8")) for f in a.extracao.glob("D*.md"))
        has_ocr = {f.name[:3] for f in a.extracao.glob("D*_p*_ocr.md")}
        for r in rows:
            if docs[r["ID"][:3]].get("situacao", "processado") != "processado":
                continue
            locs = labeled(r["Localizador"])
            for label, segment in labeled(r["Evidência"]).items():
                loc = locs.get(label, r["Localizador"] if label == "" or len(locs) == 1 else "")
                is_ocr = "ocr" in loc.lower()
                if is_ocr:
                    m = re.search(r"\bD\d{2}\b", loc)
                    src = m.group(0) if m else r["ID"][:3]
                    if src not in has_ocr:
                        skipped_ocr += len(re.findall(r'"([^"]{8,})"', segment))
                        continue
                for q in re.findall(r'"([^"]{8,})"', segment):
                    for piece in re.split(r"\s*\[\.\.\.\]\s*", q):
                        piece = norm(piece.strip(" .;:,"))
                        if len(piece) >= 8 and piece not in corpus:
                            warns.append(f"{r['ID']}: citação não encontrada no texto extraído: \"{piece[:70]}\"")

    # 4. Saída
    out = [f"# Matriz Analítica — {data.get('processo', '')}", "",
           "| Código | Arquivo | Tipo | Versão/Data | Situação |", "|---|---|---|---|---|"]
    for d in data["documentos"]:
        out.append(f"| {d['codigo']} | {clean(d['arquivo'])} | {clean(d.get('tipo'))} | {clean(d.get('versao'))} | {clean(d.get('situacao', 'processado'))} |")
    out += ["", "| " + " | ".join(COLUMNS) + " |", "|" + "---|" * len(COLUMNS)]
    out += ["| " + " | ".join(clean(r[c]) for c in COLUMNS) + " |" for r in rows]
    total = len(docs)
    proc = sum(1 for d in data["documentos"] if d.get("situacao", "processado") == "processado")
    first, last = (rows[0]["ID"], rows[-1]["ID"]) if rows else ("—", "—")
    out.append("")
    if final:
        out += ["✅ STATUS: ANÁLISE CONCLUÍDA",
                f"Documentos processados: {proc} de {total} · Total de itens: {len(rows)} (de {first} a {last})",
                "Pendências de cobertura: " + (" · ".join(pend) if pend else "nenhuma"),
                'Não é necessário enviar "continuar".']
    else:
        out += [f"⏸ STATUS: ANÁLISE EM ANDAMENTO — parte {st.get('parte', 1)}",
                f"Progresso: {st.get('concluidos', proc)} de {total} documentos concluídos · {len(rows)} itens registrados até aqui (último ID: {last})",
                f"Próximo trecho: {st.get('proximo', '—')}",
                '➜ Envie "continuar" para prosseguir.']
    a.out.write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"{len(rows)} itens gravados em {a.out}" + ("" if final else " (montagem parcial)"))
    if pending_refs:
        print(f"Referências a itens posteriores, a resolver na montagem final: {', '.join(sorted(pending_refs))}")
    if skipped_ocr:
        print(f"{skipped_ocr} citação(ões) de trechos (OCR) sem transcrição salva — não conferidas (veja 'Conferência de citações').")
    for e in dict.fromkeys(errors):
        print("ERRO:", e)
    for w in dict.fromkeys(warns):
        print("AVISO:", w)
    chk = subprocess.run([sys.executable, str(HERE / "check_matrix.py"), str(a.out)], capture_output=True, text=True)
    print("\n--- check_matrix.py ---\n" + chk.stdout.strip())
    if a.xlsx:
        x = subprocess.run([sys.executable, str(HERE / "export_xlsx.py"), str(a.out)], capture_output=True, text=True)
        print(x.stdout.strip() or x.stderr.strip())
    return 1 if errors or chk.returncode else 0


if __name__ == "__main__":
    sys.exit(main())
