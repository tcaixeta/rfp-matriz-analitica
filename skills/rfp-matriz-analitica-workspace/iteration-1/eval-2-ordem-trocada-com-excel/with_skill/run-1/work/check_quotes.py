import re,sys,glob
R=sys.argv[1]
src=" ".join(open(f,encoding="utf-8").read() for f in glob.glob(R+"/work/extracao/D0*.md"))
# texto OCR da p.6 (lido da imagem)
src+=" ANEXO III — DECLARAÇÃO DE LOCALIZAÇÃO DE DADOS Declaramos, para os devidos fins, que todos os dados do Banco Horizonte Fictício S.A., incluindo os registros (logs) de segurança, serão armazenados e processados exclusivamente em território nacional, durante toda a vigência do contrato. Esta declaração deverá ser entregue assinada pelo representante legal do proponente junto com a proposta, sob pena de inabilitação."
src=re.sub(r"\[aba [^\]]*\]","",src)
norm=lambda s:re.sub(r"\s+"," ",s).strip()
src=norm(src)
for line in open(R+"/outputs/RFP-2026-017_Matriz_Analitica.md",encoding="utf-8"):
    if not re.match(r"^\| D\d\d-\d{3} ",line): continue
    c=[x.strip() for x in line.strip().strip("|").split("|")]
    for q in re.findall(r'"([^"]+)"',c[5]):
        for part in q.split("[...]"):
            p=norm(part)
            if p and p not in src: print(c[0],"NÃO ENCONTRADO:",p[:90])
