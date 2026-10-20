#!/usr/bin/env python3
"""Valida uma matriz analítica de RFP em Markdown.

Uso:
    python check_matrix.py <matriz.md> [--max-critica 0.25]

Erros (saída com código 1) indicam algo a corrigir antes de entregar.
Avisos indicam itens a reexaminar com julgamento: não são erros automáticos.
"""
import argparse
import re
import sys
from collections import Counter

COLUMNS = ["ID", "Documento", "Versão/Data", "Seção/Cláusula", "Localizador", "Evidência", "Tipo de item",
           "Domínio", "Descrição analítica", "Obrigatoriedade", "Natureza da evidência", "Severidade",
           "Probabilidade", "Criticidade", "Impacto para o proponente", "Framework/Referência",
           "Controle/Cláusula", "Tipo de associação", "IDs relacionados", "Status de vigência",
           "Ação recomendada", "Pergunta de esclarecimento", "Responsável interno sugerido"]
NO_RATING = ("Registro de cobertura", "Oportunidade")
ID_RE = re.compile(r"^D\d{2}-\d{3}$")


def band(score):
    return "Baixa" if score <= 4 else "Média" if score <= 9 else "Alta" if score <= 15 else "Crítica"


def parse(path):
    text = open(path, encoding="utf-8").read()
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\|\s*D\d{2}-\d{3}\s*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append((n, cells))
    return text, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("matrix")
    ap.add_argument("--max-critica", type=float, default=0.25)
    a = ap.parse_args()
    text, rows = parse(a.matrix)
    errors, warns = [], []
    if not rows:
        print("ERRO: nenhuma linha de item (| Dnn-nnn | ...) encontrada.")
        return 1

    header = next((l for l in text.splitlines() if l.startswith("| ID |")), None)
    if header:
        cols = [c.strip() for c in header.strip().strip("|").split("|")]
        if cols != COLUMNS:
            errors.append(f"Cabeçalho difere das 23 colunas esperadas: {cols}")
    else:
        errors.append("Cabeçalho da tabela (| ID | Documento | ...) não encontrado.")

    ids = Counter()
    labels = Counter()
    rated = 0
    for n, c in rows:
        if len(c) != 23:
            errors.append(f"linha {n}: {len(c)} colunas (esperado 23) — confira '|' dentro do conteúdo.")
            continue
        r = dict(zip(COLUMNS, c))
        rid = r["ID"]
        ids[rid] += 1
        if not ID_RE.match(rid):
            errors.append(f"{rid}: ID fora do formato Dnn-nnn.")
        for col in ("Evidência", "Localizador", "Tipo de item"):
            if r[col] in ("", "—"):
                errors.append(f"{rid}: coluna '{col}' vazia.")
        tipo, sev, prob, crit = r["Tipo de item"], r["Severidade"], r["Probabilidade"], r["Criticidade"]
        if tipo.startswith(NO_RATING):
            if any(x != "—" for x in (sev, prob, crit)):
                errors.append(f"{rid}: {tipo} não recebe Severidade/Probabilidade/Criticidade (use '—').")
            if tipo.startswith("Registro de cobertura") and re.search(r"em branco", r["Descrição analítica"], re.I):
                warns.append(f"{rid}: Registro de cobertura descreve página 'em branco' — confira se não é imagem não lida.")
            continue
        try:
            s, p = int(sev.split("·")[0]), int(prob.split("·")[0])
            m = re.match(r"(\d+)\s*·\s*(\S+)", crit)
            score, label = int(m.group(1)), m.group(2)
        except (ValueError, AttributeError):
            errors.append(f"{rid}: Severidade/Probabilidade/Criticidade fora do formato 'n · Rótulo' ({sev} | {prob} | {crit}).")
            continue
        rated += 1
        exp = band(s * p)
        if s == 5 and exp in ("Baixa", "Média"):
            exp = "Alta"
        if score != s * p:
            errors.append(f"{rid}: pontuação {score} ≠ {s}×{p}.")
        if label != exp:
            errors.append(f"{rid}: criticidade '{label}' deveria ser '{exp}' (S{s}×P{p}" + (", regra da Severidade 5" if s == 5 else "") + ").")
        labels[label] += 1
        desc = r["Descrição analítica"]
        if p != 3 and "probabilidade" not in desc.lower():
            errors.append(f"{rid}: Probabilidade {p} sem justificativa na Descrição analítica.")
        if p >= 4 and tipo in ("Contradição", "Ambiguidade", "Lacuna"):
            warns.append(f"{rid}: {tipo} com Probabilidade {p} — confira se há evidência específica (o padrão é 3).")
        if re.search(r"\bA\.(9|1[0-8])\.\d", r["Controle/Cláusula"]):
            errors.append(f"{rid}: controle '{r['Controle/Cláusula']}' parece da ISO/IEC 27001:2013 (a versão 2022 vai de A.5 a A.8).")
        if "14.133" in r["Framework/Referência"]:
            warns.append(f"{rid}: Lei 14.133/2021 associada — confirme que o regime identificado é de contratação pública.")
        if tipo == "Contradição" and not ("A:" in r["Evidência"] and "B:" in r["Evidência"]):
            warns.append(f"{rid}: Contradição sem as duas evidências marcadas como 'A:' e 'B:'.")

    for rid, k in ids.items():
        if k > 1:
            errors.append(f"{rid}: ID repetido {k} vezes.")
    by_doc = {}
    for rid in ids:
        if ID_RE.match(rid):
            by_doc.setdefault(rid[:3], []).append(int(rid[4:]))
    for d, nums in sorted(by_doc.items()):
        missing = sorted(set(range(1, max(nums) + 1)) - set(nums))
        if missing:
            warns.append(f"{d}: numeração com lacunas {missing[:10]}{'...' if len(missing) > 10 else ''}.")

    share = labels["Crítica"] / rated if rated else 0
    if share > a.max_critica:
        warns.append(f"{labels['Crítica']} de {rated} itens avaliados ({share:.0%}) são Crítica — revise efeito em cadeia e evidência das probabilidades 4 e 5.")

    m = re.search(r"✅ STATUS: ANÁLISE CONCLUÍDA.*?Total de itens:\s*(\d+)", text, re.S)
    if m:
        if int(m.group(1)) != len(rows):
            errors.append(f"Status final informa {m.group(1)} itens, mas a matriz tem {len(rows)} linhas.")
    elif "⏸ STATUS" not in text:
        warns.append("Nenhum bloco de status (✅ ou ⏸) encontrado no arquivo.")

    print(f"Linhas: {len(rows)} · avaliadas: {rated} · distribuição: {dict(labels)}")
    for e in errors:
        print("ERRO:", e)
    for w in warns:
        print("AVISO:", w)
    print("Resultado:", "OK" if not errors else f"{len(errors)} erro(s)", f"· {len(warns)} aviso(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
