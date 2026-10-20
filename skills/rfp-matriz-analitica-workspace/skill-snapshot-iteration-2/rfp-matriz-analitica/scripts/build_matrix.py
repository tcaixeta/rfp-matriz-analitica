#!/usr/bin/env python3
"""Monta a matriz analítica em Markdown a partir de um arquivo JSON de itens.

Uso:
    python build_matrix.py itens.json --out <processo>_Matriz_Analitica.md [--extracao <pasta>] [--xlsx]

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
  no texto extraído (trechos com localizador "(OCR)" não são conferidos);
- ao final, roda check_matrix.py e, com --xlsx, exporta para Excel.

Formato do JSON:
{
  "processo": "RFP nº 2026-017 — Banco Exemplo S.A.",
  "documentos": [
    {"codigo": "D01", "arquivo": "RFP.pdf", "tipo": "RFP", "versao": "v1.0 — 15/10/2026", "situacao": "processado"},
    {"codigo": "D02", "arquivo": "Anexo_IV.xlsx", "tipo": "Planilha de preços", "versao": "v1.0", "situacao": "não anexado"}
  ],
  "itens": [
    {"chave": "d01_inventario", "doc": "D01", "secao": "Capa e documento inteiro", "localizador": "p. 1–6",
     "evidencia": "\\"Solicitação de Proposta (RFP) nº 2026-017\\"", "tipo": "Registro de cobertura",
     "dominio": "Administrativo do processo", "descricao": "Inventário: ...", "responsavel": "Bid Manager"},
    {"chave": "d01_transicao", "doc": "D01", "secao": "3. Cronograma — 3.2", "localizador": "p. 2 (impressa: 1)",
     "evidencia": "\\"...em até 30 (trinta) dias corridos...\\"", "tipo": "Prazo / marco", "dominio": "Transição/Implantação",
     "descricao": "...", "obrigatoriedade": "Mandatório", "s": 4, "p": 3, "impacto": "...",
     "relacionados": ["d02_transicao"], "vigencia": "Em esclarecimento", "acao": "Esclarecer no Q&A",
     "pergunta": "...", "responsavel": "Delivery/Operação",
     "pendencia": "texto curto para o status final (opcional)"}
  ],
  "status": {"final": true}            // ou {"final": false, "proximo": "Anexo I (D02), a partir da seção 4"}
}
Campos omitidos recebem padrão: obrigatoriedade "Informativo", natureza "Explícita",
vigencia "Vigente", acao "Nenhuma (informativo)", demais "—".
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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("itens", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--extracao", type=Path, help="pasta gerada por extract_documents.py, para conferir citações")
    ap.add_argument("--xlsx", action="store_true", help="exportar também para Excel")
    a = ap.parse_args()
    data = json.loads(a.itens.read_text(encoding="utf-8"))
    docs = {d["codigo"]: d for d in data["documentos"]}
    errors, warns = [], []

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

    def resolve(text):
        def rep(m):
            k = m.group(1)
            if k in ids:
                return ids[k]
            errors.append(f"referência a chave inexistente: {{{k}}}")
            return m.group(0)
        return re.sub(r"\{([A-Za-z0-9_\-]+)\}", rep, str(text))

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
        if tipo in NO_RATING:
            r["Severidade"] = r["Probabilidade"] = r["Criticidade"] = "—"
        else:
            s, p = it.get("s"), it.get("p")
            if s not in SEV or p not in PROB:
                errors.append(f"{rid}: 's' e 'p' devem ser inteiros de 1 a 5 (recebido s={s}, p={p}).")
                s, p = s if s in SEV else 3, p if p in PROB else 3
            r["Severidade"], r["Probabilidade"], r["Criticidade"] = f"{s} · {SEV[s]}", f"{p} · {PROB[p]}", band(s, p)
            if p != 3 and "probabilidade" not in r["Descrição analítica"].lower():
                errors.append(f"{rid}: Probabilidade {p} sem justificativa ('Probabilidade {p}: ...') na descrição.")
        rel = it.get("relacionados") or []
        r["IDs relacionados"] = " · ".join(ids.get(x, x) for x in rel) if rel else "—"
        for x in rel:
            if x not in ids and not re.match(r"^D\d{2}-\d{3}$", x):
                warns.append(f"{rid}: relacionado '{x}' não é chave conhecida (mantido como texto).")
        if it.get("pendencia"):
            pend.append(f"{rid} ({resolve(it['pendencia'])})")
        rows.append(r)

    # 3. Conferência das citações contra o texto extraído
    if a.extracao:
        corpus = {}
        for f in a.extracao.glob("D*.md"):
            corpus[f.name[:3]] = norm(f.read_text(encoding="utf-8"))
        everything = " ".join(corpus.values())
        for r in rows:
            if "ocr" in r["Localizador"].lower() or docs[r["ID"][:3]].get("situacao", "processado") != "processado":
                continue
            for q in re.findall(r'"([^"]{8,})"', r["Evidência"]):
                for piece in re.split(r"\s*\[\.\.\.\]\s*", q):
                    piece = norm(piece.strip(" .;:,"))
                    if len(piece) >= 8 and piece not in everything:
                        warns.append(f"{r['ID']}: citação não encontrada no texto extraído: \"{piece[:70]}\"")

    # 4. Saída
    out = [f"# Matriz Analítica — {data.get('processo', '')}", "",
           "| Código | Arquivo | Tipo | Versão/Data | Situação |", "|---|---|---|---|---|"]
    for d in data["documentos"]:
        out.append(f"| {d['codigo']} | {clean(d['arquivo'])} | {clean(d.get('tipo'))} | {clean(d.get('versao'))} | {clean(d.get('situacao', 'processado'))} |")
    out += ["", "| " + " | ".join(COLUMNS) + " |", "|" + "---|" * len(COLUMNS)]
    out += ["| " + " | ".join(clean(r[c]) for c in COLUMNS) + " |" for r in rows]
    st = data.get("status", {"final": True})
    total = len(docs)
    proc = sum(1 for d in data["documentos"] if d.get("situacao", "processado") == "processado")
    first, last = (rows[0]["ID"], rows[-1]["ID"]) if rows else ("—", "—")
    out.append("")
    if st.get("final", True):
        out += ["✅ STATUS: ANÁLISE CONCLUÍDA",
                f"Documentos processados: {proc} de {total} · Total de itens: {len(rows)} (de {first} a {last})",
                "Pendências de cobertura: " + (" · ".join(pend) if pend else "nenhuma"),
                'Não é necessário enviar "continuar".']
    else:
        done = st.get("concluidos", proc)
        out += [f"⏸ STATUS: ANÁLISE EM ANDAMENTO — parte {st.get('parte', 1)}",
                f"Progresso: {done} de {total} documentos concluídos · {len(rows)} itens registrados até aqui (último ID: {last})",
                f"Próximo trecho: {st.get('proximo', '—')}",
                '➜ Envie "continuar" para prosseguir.']
    a.out.write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"{len(rows)} itens gravados em {a.out}")
    for e in errors:
        print("ERRO:", e)
    for w in warns:
        print("AVISO:", w)
    chk = subprocess.run([sys.executable, str(HERE / "check_matrix.py"), str(a.out)], capture_output=True, text=True)
    print("\n--- check_matrix.py ---\n" + chk.stdout.strip())
    if a.xlsx:
        x = subprocess.run([sys.executable, str(HERE / "export_xlsx.py"), str(a.out)], capture_output=True, text=True)
        print(x.stdout.strip() or x.stderr.strip())
    return 1 if errors or chk.returncode else 0


if __name__ == "__main__":
    sys.exit(main())
