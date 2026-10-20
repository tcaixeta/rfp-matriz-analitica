import re, sys, glob
R = sys.argv[1]
src = ""
for f in glob.glob(R + "/work/extracao/D0*.md"):
    t = open(f, encoding="utf-8").read()
    t = re.sub(r"\[aba [^\]]*\]\s*", "", t)
    src += " " + t
ocr = ("ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS Declaramos, para os devidos fins, que todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato. Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação.")
src += " " + ocr
norm = lambda s: re.sub(r"\s+", " ", s).strip()
S = norm(src)
bad = 0
for line in open(R + "/outputs/RFP-2026-017_Matriz_Analitica.md", encoding="utf-8"):
    if not re.match(r"^\| D\d\d-\d{3} \|", line): continue
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    for q in re.findall(r'"([^"]+)"', c[5]):
        for part in q.split("[...]"):
            p = norm(part.replace("\\'", "'"))
            if p and p not in S:
                bad += 1; print(c[0], "NOT FOUND:", p[:90])
print("bad", bad)
