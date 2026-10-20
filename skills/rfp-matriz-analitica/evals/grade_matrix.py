#!/usr/bin/env python3
"""Avalia automaticamente uma matriz gerada a partir do kit sintético RFP 2026-017.

Uso:
    python grade_matrix.py --eval-id 1 --matrix <matriz.md> [--outputs <pasta>] [--out grading.json]

Cada verificação corresponde a uma expectativa de evals.json (mesmo texto) e
gera um grading.json no formato do skill-creator (text, passed, evidence).
A avaliação item a item contra o gabarito continua manual (Planilha de Avaliação).
"""
import argparse
import json
import re
import sys
from pathlib import Path

COLUMNS = ["ID", "Documento", "Versão/Data", "Seção/Cláusula", "Localizador", "Evidência", "Tipo de item",
           "Domínio", "Descrição analítica", "Obrigatoriedade", "Natureza da evidência", "Severidade",
           "Probabilidade", "Criticidade", "Impacto para o proponente", "Framework/Referência",
           "Controle/Cláusula", "Tipo de associação", "IDs relacionados", "Status de vigência",
           "Ação recomendada", "Pergunta de esclarecimento", "Responsável interno sugerido"]


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if re.match(r"^\|\s*D\d{2}-\d{3}\s*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 23:
                r = dict(zip(COLUMNS, cells))
                r["_all"] = " ".join(cells)
                rows.append(r)
    return text, rows


def band(s):
    return "Baixa" if s <= 4 else "Média" if s <= 9 else "Alta" if s <= 15 else "Crítica"


def ids(rs, n=6):
    return ", ".join(r["ID"] for r in rs[:n]) + ("..." if len(rs) > n else "") if rs else "nenhuma linha"


def find(rows, tipo=None, all_terms=(), any_terms=(), col="_all"):
    out = []
    for r in rows:
        if tipo and not any(r["Tipo de item"].startswith(t) for t in (tipo if isinstance(tipo, tuple) else (tipo,))):
            continue
        t = r[col].lower()
        if all(x.lower() in t for x in all_terms) and (not any_terms or any(x.lower() in t for x in any_terms)):
            out.append(r)
    return out


def lacuna_anexo_iv(rows):
    """Lacuna sobre o próprio Anexo IV: ancorada na instrução 4.3 que o cita."""
    return [r for r in find(rows, tipo="Lacuna", all_terms=("anexo iv",))
            if "4.3" in r["Seção/Cláusula"] or r["Evidência"].lower().startswith("não localizado · \"conforme a planilha")]


def checks_core(text, rows, eval_id=1):
    res = []
    raw_lines = [l for l in text.splitlines() if re.match(r"^\|\s*D\d{2}-\d{3}\s*\|", l)]
    bad = len(raw_lines) - len(rows)
    uniq = len({r["ID"] for r in rows}) == len(rows)
    res.append(("[Formato] A matriz tem 23 colunas em todas as linhas e IDs únicos no formato Dnn-nnn",
                bad == 0 and uniq and len(rows) > 0, f"{len(rows)} linhas válidas, {bad} com nº de colunas errado, IDs únicos: {uniq}"))

    arith, unjust, crit, rated = [], [], 0, 0
    for r in rows:
        if r["Severidade"] == "—":
            continue
        try:
            s, p = int(r["Severidade"][0]), int(r["Probabilidade"][0])
            sc, lab = re.match(r"(\d+)\s*·\s*(\S+)", r["Criticidade"]).groups()
        except Exception:
            arith.append(r)
            continue
        rated += 1
        exp = band(s * p)
        if s == 5 and exp in ("Baixa", "Média"):
            exp = "Alta"
        if int(sc) != s * p or lab != exp:
            arith.append(r)
        if p != 3 and "probabilidade" not in r["Descrição analítica"].lower():
            unjust.append(r)
        crit += lab == "Crítica"
    res.append(("[Formato] Toda Criticidade é igual a Severidade × Probabilidade e respeita a regra da Severidade 5",
                not arith, f"{len(arith)} divergência(s): {ids(arith)}" if arith else f"{rated} itens avaliados conferidos"))
    res.append(("[Formato] Toda Probabilidade diferente de 3 tem justificativa na Descrição analítica",
                not unjust, f"sem justificativa: {ids(unjust)}" if unjust else "todas justificadas"))
    share = crit / rated if rated else 1
    res.append(("[Formato] No máximo cerca de 25% dos itens avaliados são Crítica (criticidade calibrada)",
                share <= 0.25, f"{crit} de {rated} ({share:.0%}) como Crítica"))

    ocr = find(rows, all_terms=("p. 6", "ocr"), col="Localizador")
    res.append(("[Formato] A página 6 do PDF (Anexo III, digitalizada) foi lida por OCR ou visão",
                bool(ocr), f"linhas com localizador p. 6 (OCR): {ids(ocr)}"))
    a3 = [r for r in find(rows, tipo="Critério eliminatório", all_terms=("p. 6",), col="Localizador")]
    res.append(("[Formato] A declaração do Anexo III (assinatura sob pena de inabilitação) foi registrada como critério eliminatório",
                bool(a3), ids(a3)))
    dados = find(rows, tipo="Contradição", all_terms=("território nacional",), any_terms=("livre escolha", "região"))
    res.append(("[Formato] A contradição entre dados exclusivamente no Brasil (Anexo III) e nuvem em região livre (Anexo I) foi registrada",
                bool(dados), ids(dados)))
    tr = find(rows, tipo="Contradição", all_terms=("30", "60", "dias"), any_terms=("transição",))
    res.append(("[Formato] A contradição do prazo de transição (30 × 60 dias) foi registrada", bool(tr), ids(tr)))
    ret = find(rows, tipo=("Contradição", "Ambiguidade"), all_terms=("12",), any_terms=("5 (cinco) anos", "5 anos"))
    ret = [r for r in ret if "log" in r["_all"].lower()]
    res.append(("[Formato] A divergência de retenção de logs (12 meses × 5 anos) foi registrada como Contradição ou Ambiguidade",
                bool(ret), ids(ret)))
    pts = find(rows, tipo="Contradição", all_terms=("65", "60"))
    res.append(("[Formato] A contradição na pontuação técnica (critérios somam 65, máximo declarado 60) foi registrada", bool(pts), ids(pts)))
    us = find(rows, tipo="Contradição", all_terms=("4.500", "6.200"))
    res.append(("[Formato] A divergência da base de usuários (4.500 × 6.200) foi registrada como Contradição", bool(us), ids(us)))
    notes = find(rows, all_terms=("notas",), col="Localizador")
    notes = [r for r in notes if "subsidiárias" in r["_all"].lower()]
    res.append(("[Formato] As notas do apresentador do slide 5 (inclusão das subsidiárias) foram analisadas", bool(notes), ids(notes)))
    pesos = [r for r in find(rows, all_terms=("pesos",), col="Localizador") if "2 (dois) pontos" in r["_all"]]
    res.append(("[Formato] A aba oculta 'Pesos' e a regra de desconto de 2 pontos foram analisadas", bool(pesos), ids(pesos)))
    a4 = [r for r in lacuna_anexo_iv(rows) if r["Criticidade"] != "—"]
    if eval_id == 3:
        cob = [r for r in find(rows, tipo="Registro de cobertura", any_terms=("anexo iv", "anexo_iv"))
               if re.search(r"não anexad|listad", r["_all"], re.I)]
        res.append(("[Formato] O Anexo IV listado e não anexado gera só Registro de cobertura, sem Lacuna própria",
                    bool(cob) and not a4, f"cobertura: {ids(cob)} · Lacuna do Anexo IV: {ids(a4)}"))
    else:
        res.append(("[Formato] O Anexo IV (citado e não fornecido) foi registrado como Lacuna com criticidade", bool(a4), ids(a4)))
    mc = [r for r in find(rows, tipo="Lacuna", all_terms=("matriz de classificação",)) if r["Criticidade"] != "—"]
    res.append(("[Formato] A matriz de classificação de criticidade do Contratante foi registrada como Lacuna com criticidade", bool(mc), ids(mc)))
    pr = find(rows, tipo="Lacuna", all_terms=("precedência",))
    res.append(("[Formato] A ausência de ordem de precedência entre documentos foi registrada como Lacuna", bool(pr), ids(pr)))
    alt = [r for r in rows if "20/11/2026" in r["Evidência"] and r["Status de vigência"].startswith(("Alterado", "Substituído"))]
    res.append(("[Formato] O prazo de entrega original (20/11/2026) está marcado como Alterado pela resposta do Q&A", bool(alt), ids(alt)))
    lei = [r for r in rows if "14.133" in r["Framework/Referência"]]
    res.append(("[Formato] Nenhum item associa a Lei 14.133/2021 (contratação privada)", not lei, ids(lei) if lei else "nenhuma associação"))
    iso13 = [r for r in rows if re.search(r"\bA\.(9|1[0-8])\.\d", r["Controle/Cláusula"])]
    res.append(("[Formato] Nenhum controle ISO/IEC 27001 usa a numeração da versão 2013 (A.9 a A.18)", not iso13,
                ids(iso13) if iso13 else "nenhum"))
    inst = [r for r in rows if "fundado em 1987" in r["Evidência"]]
    res.append(("[Formato] O parágrafo institucional (§1.1, 'fundado em 1987') não virou item", not inst, ids(inst) if inst else "não extraído"))
    pdf_p = [r for r in rows if r["ID"].startswith("D01") and re.search(r"\bp\. [2-5]\b", r["Localizador"])]
    no_pr = [r for r in pdf_p if "impressa" not in r["Localizador"]]
    res.append(("[Formato] Os localizadores do PDF trazem página física e impressa (ex.: 'p. 2 (impressa: 1)')",
                bool(pdf_p) and not no_pr, f"{len(pdf_p) - len(no_pr)} de {len(pdf_p)} com página impressa"))
    m = re.search(r"✅ STATUS: ANÁLISE CONCLUÍDA.*?Total de itens:\s*(\d+)", text, re.S)
    ok = bool(m) and int(m.group(1)) == len(rows)
    res.append(("[Formato] O status final ✅ ANÁLISE CONCLUÍDA está presente e informa o total correto de itens", ok,
                f"status informa {m.group(1)} itens; matriz tem {len(rows)}" if m else "status final ausente"))
    return res


ABSENT = r"não (foi )?(fornecid|enviad|anexad|recebid|veio|consta)|ausente|faltando|citad[oa] e não|não está no pacote|inexistente"


def lines_with(text, all_terms=(), any_terms=(), regex=None):
    out = []
    for l in text.splitlines():
        t = l.lower()
        if all(x in t for x in all_terms) and (not any_terms or any(x in t for x in any_terms)) and (not regex or re.search(regex, t)):
            out.append(l.strip())
    return out


def checks_conteudo(text):
    """Achados-chave do kit, procurados linha a linha em qualquer formato (tabela, relatório, lista)."""
    C = [
        ("A declaração do Anexo III (página 6, só imagem) foi lida e tratada como causa de inabilitação",
         lines_with(text, any_terms=("anexo iii", "localização de dados"), regex=r"inabilita")),
        ("O conflito entre dados só no Brasil (Anexo III) e SIEM em nuvem de região livre (Anexo I) foi apontado",
         lines_with(text, any_terms=("território nacional", "no brasil", "só no brasil"), regex=r"livre escolha|qualquer região")),
        ("O conflito do prazo de transição (30 × 60 dias) foi apontado",
         lines_with(text, all_terms=("30", "60"), regex=r"transição")),
        ("O conflito de retenção de logs (12 meses × 5 anos) foi apontado",
         lines_with(text, all_terms=("12",), regex=r"5 (\(cinco\) )?anos")),
        ("A inconsistência da pontuação técnica (soma 65 × máximo 60) foi apontada",
         lines_with(text, all_terms=("65", "60"), regex=r"pont|nota")),
        ("A divergência da base de usuários (4.500 × 6.200) foi apontada",
         lines_with(text, all_terms=("4.500", "6.200"))),
        ("A inclusão das subsidiárias (cerca de 900 usuários), só nas notas do slide 5, foi apontada",
         lines_with(text, all_terms=("subsidiárias", "900"))),
        ("A regra oculta da aba 'Pesos' (desconto de 2 pontos) foi apontada",
         lines_with(text, all_terms=("pesos",), regex=r"2 (\(dois\) )?pontos|dois pontos")),
        ("O Anexo IV (planilha de preços) foi apontado como não disponível",
         lines_with(text, any_terms=("anexo iv", "anexo_iv"), regex=ABSENT)),
        ("A matriz de classificação de criticidade do Contratante foi apontada como não fornecida",
         lines_with(text, regex=r"matriz de (classifica|criticidade)") and lines_with(text, regex=r"matriz de (classifica|criticidade).*(" + ABSENT + ")|(" + ABSENT + ").*matriz de (classifica|criticidade)")),
        ("A falta de ordem de precedência entre documentos foi apontada",
         lines_with(text, regex=r"(precedência|hierarquia).*(não (há|existe|define|tem)|sem |ausência|inexist|lacuna)|(não (há|existe|define|tem)|nenhum documento define|sem |ausência).*(precedência|hierarquia)")),
        ("A multa por SLA sem teto e a responsabilidade ilimitada foram apontadas como risco",
         lines_with(text, all_terms=("multa",), regex=r"sem (teto|limite)|ilimitad") and lines_with(text, all_terms=("responsabilidade",), regex=r"ilimitad")),
        ("A recusa do cliente em informar a volumetria (EPS) antes da adjudicação foi apontada",
         lines_with(text, any_terms=("eps", "volumetria"), regex=r"vencedor|recus|q&a ?(n[ºo°] ?)?#? ?3|qa ?#? ?3")),
        ("O risco de cronograma (SIEM legado até 31/01/2027 × início em 01/02/2027) foi apontado",
         lines_with(text, all_terms=("31/01/2027",), regex=r"01/02/2027|início")),
        ("A migração de 24 meses de logs históricos, citada só na apresentação, foi apontada",
         lines_with(text, all_terms=("24 meses",), regex=r"log")),
        ("A prorrogação da entrega para 27/11/2026 pelo Q&A foi registrada",
         lines_with(text, all_terms=("27/11",))),
    ]
    res = [("[Conteúdo] " + t, bool(hit), (hit[0][:160] if hit and isinstance(hit, list) else "não encontrado")) for t, hit in C]
    return res


def checks_eval2(text, rows, outputs):
    res = []
    d01 = [r for r in rows if r["ID"].startswith("D01")]
    is_rfp = bool(d01) and all("RFP-2026-017" in r["Documento"] or r["ID"] != "D01-001" for r in d01[:1])
    res.append(("[Formato] Mesmo com os anexos enviados em ordem inversa, o RFP recebeu o código D01 e o Q&A o último código",
                is_rfp and any(r["ID"].startswith("D04") and "QA_Rodada1" in r["Documento"] for r in rows),
                f"D01 = {d01[0]['Documento'] if d01 else '—'}"))
    xlsx = list(Path(outputs).glob("*.xlsx")) if outputs else []
    res.append(("[Formato] Foi gerado um arquivo Excel com a matriz", bool(xlsx), ", ".join(x.name for x in xlsx) or "nenhum .xlsx"))
    return res


def checks_eval3(text, rows, outputs):
    res = []
    pend = re.search(r"Pendências de cobertura:.*", text)
    res.append(("[Formato] As Pendências de cobertura do status final citam o Anexo IV", bool(pend and "IV" in pend.group(0)),
                pend.group(0)[:200] if pend else "linha de pendências ausente"))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eval-id", type=int, required=True)
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--outputs", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    text, rows = load(a.matrix)
    res = checks_core(text, rows, a.eval_id) + checks_conteudo(text)
    if a.eval_id == 2:
        res += checks_eval2(text, rows, a.outputs)
    elif a.eval_id == 3:
        res += checks_eval3(text, rows, a.outputs)
    exps = [{"text": t, "passed": bool(p), "evidence": e} for t, p, e in res]
    passed = sum(e["passed"] for e in exps)
    grading = {"expectations": exps,
               "summary": {"passed": passed, "failed": len(exps) - passed, "total": len(exps),
                           "pass_rate": round(passed / len(exps), 2)}}
    if a.out:
        Path(a.out).write_text(json.dumps(grading, ensure_ascii=False, indent=2), encoding="utf-8")
    for e in exps:
        print(("✔" if e["passed"] else "✘"), e["text"], "—", e["evidence"])
    print(f"{passed}/{len(exps)}")


if __name__ == "__main__":
    sys.exit(main())
