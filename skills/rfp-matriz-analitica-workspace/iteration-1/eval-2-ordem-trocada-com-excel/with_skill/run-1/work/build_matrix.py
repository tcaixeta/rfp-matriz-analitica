#!/usr/bin/env python3
"""Gera a matriz analítica (Markdown) a partir de work/rows.txt.

Formato de rows.txt: registros separados por linha em branco; cada linha "campo: valor".
Referências @chave em qualquer campo são trocadas pelo ID atribuído.
"""
import re
import sys
from pathlib import Path

WORK = Path(__file__).parent
OUT = Path(sys.argv[1])

DOCS = {
    "D01": ("RFP-2026-017_Servicos_SOC_IAM.pdf", "Versão 1.0 — 15/10/2026"),
    "D02": ("Anexo_I_Especificacao_Tecnica.docx", "Versão 1.0 — 15/10/2026"),
    "D03": ("Apresentacao_Ambiente_Atual.pptx", "22/10/2026 (workshop)"),
    "D04": ("QA_Rodada1_e_Questionario.xlsx", "não informada"),
}
SEV = {1: "Insignificante", 2: "Menor", 3: "Moderada", 4: "Maior", 5: "Severa"}
PROB = {1: "Remota", 2: "Improvável", 3: "Possível", 4: "Provável", 5: "Quase certa"}
DEFAULTS = {"nat": "Explícita", "obr": "Mandatório", "fw": "—", "ctrl": "—", "assoc": "Não aplicável",
            "rel": "—", "st": "Vigente", "perg": "—", "imp": "—", "s": "", "p": "", "ver": ""}
COLS = ["ID", "Documento", "Versão/Data", "Seção/Cláusula", "Localizador", "Evidência", "Tipo de item",
        "Domínio", "Descrição analítica", "Obrigatoriedade", "Natureza da evidência", "Severidade",
        "Probabilidade", "Criticidade", "Impacto para o proponente", "Framework/Referência",
        "Controle/Cláusula", "Tipo de associação", "IDs relacionados", "Status de vigência",
        "Ação recomendada", "Pergunta de esclarecimento", "Responsável interno sugerido"]


def band(s, p):
    sc = s * p
    b = "Baixa" if sc <= 4 else "Média" if sc <= 9 else "Alta" if sc <= 15 else "Crítica"
    if s == 5 and b in ("Baixa", "Média"):
        b = "Alta"
    return f"{sc} · {b}"


recs = []
for block in re.split(r"\n\s*\n", (WORK / "rows.txt").read_text(encoding="utf-8").strip()):
    r = dict(DEFAULTS)
    for line in block.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        k, _, v = line.partition(":")
        r[k.strip()] = v.strip()
    recs.append(r)

ids, counters = {}, {}
for r in recs:
    d = r["doc"]
    counters[d] = counters.get(d, 0) + 1
    rid = f"{d}-{counters[d]:03d}"
    if r["k"] in ids:
        sys.exit(f"chave duplicada {r['k']}")
    ids[r["k"]] = rid
    r["id"] = rid


def resolve(text):
    def sub(m):
        if m.group(1) not in ids:
            sys.exit(f"referência desconhecida @{m.group(1)}")
        return ids[m.group(1)]
    return re.sub(r"@([a-z0-9_]+)", sub, text)


lines = []
for r in recs:
    tipo = r["tipo"]
    norate = tipo.startswith(("Registro de cobertura", "Oportunidade"))
    if norate:
        s = p = c = "—"
    else:
        si, pi = int(r["s"]), int(r["p"])
        s, p, c = f"{si} · {SEV[si]}", f"{pi} · {PROB[pi]}", band(si, pi)
    rel = r["rel"]
    if rel != "—":
        rel = " · ".join(resolve("@" + x.strip().lstrip("@")) for x in rel.split(",") if x.strip())
    ver = r["ver"] or DOCS[r["doc"]][1]
    cells = [r["id"], DOCS[r["doc"]][0], ver, r["sec"], r["loc"], r["ev"], tipo, r["dom"], r["desc"],
             r["obr"] if not tipo.startswith("Registro") else "Informativo", r["nat"], s, p, c, r["imp"],
             r["fw"], r["ctrl"], r["assoc"] if not tipo.startswith("Registro") else "—", rel, r["st"],
             r["acao"], r["perg"], r["resp"]]
    cells = [resolve(x).replace("|", "/").replace("\n", " ").strip() or "—" for x in cells]
    lines.append("| " + " | ".join(cells) + " |")

n = len(recs)
first, last = recs[0]["id"], recs[-1]["id"]
pend = [ids[k] for k in ("d1_lac4", "d1_lac2", "d2_matriz")]
head = ["# RFP nº 2026-017 — Banco Horizonte Fictício S.A. — Serviços Gerenciados de SOC e IAM — Matriz Analítica", "",
        "Análise do ponto de vista do proponente. Data da análise: 17/10/2026.", "",
        "## Documentos", "",
        "| Código | Arquivo | Versão/Data | Ordem de envio pelo usuário |", "|---|---|---|---|",
        "| D01 | RFP-2026-017_Servicos_SOC_IAM.pdf | Versão 1.0 — 15/10/2026 | 4º |",
        "| D02 | Anexo_I_Especificacao_Tecnica.docx | Versão 1.0 — 15/10/2026 | 3º |",
        "| D03 | Apresentacao_Ambiente_Atual.pptx | 22/10/2026 (workshop) | 2º |",
        "| D04 | QA_Rodada1_e_Questionario.xlsx | não informada (respostas do Q&A Rodada 1 datadas de 12/11/2026) | 1º |", "",
        "Os documentos foram reordenados para a ordem de processamento (documento principal → anexo técnico → apresentação → Q&A/questionário), para que as alterações do Q&A sejam confrontadas com os originais.", "",
        "## Matriz", "",
        "| " + " | ".join(COLS) + " |", "|" + "---|" * len(COLS)]
tail = ["", "## Status", "",
        "✅ STATUS: ANÁLISE CONCLUÍDA",
        f"Documentos processados: 4 de 4 · Total de itens: {n} (de {first} a {last})",
        f"Pendências de cobertura: {' · '.join(pend)} (Lacunas de documentos citados ou inferidos e não fornecidos: Anexo IV — Planilha de Preços; Anexo II; matriz de classificação de incidentes do Contratante). Sem trechos ilegíveis: a p. 6 do D01 (imagem) foi lida por OCR e a aba oculta \"Pesos\" e as notas do slide 5 foram analisadas.",
        "Não é necessário enviar \"continuar\"."]
OUT.write_text("\n".join(head + lines + tail) + "\n", encoding="utf-8")
print(f"{n} linhas gravadas em {OUT}")
