import sys, pdfplumber, zipfile, re
D=sys.argv[1]
with pdfplumber.open(f"{D}/RFP-2026-017_Servicos_SOC_IAM.pdf") as pdf:
    print("meta", pdf.metadata)
    for i,p in enumerate(pdf.pages,1):
        cols=set(); sizes=set()
        for c in p.chars: cols.add(str(c.get('non_stroking_color'))); sizes.add(round(c['size'],1))
        print(i, "colors",cols,"sizes",sizes, "annots", len(p.annots or []), "images", len(p.images), "rects", len(p.rects))
        odd=[c for c in p.chars if c['size']<6 or str(c.get('non_stroking_color')) in ('(1, 1, 1)','[1, 1, 1]','(1,)','[1]')]
        if odd: print("ODD:", "".join(c['text'] for c in odd))
for fn in ["Anexo_I_Especificacao_Tecnica.docx","Apresentacao_Ambiente_Atual.pptx","QA_Rodada1_e_Questionario.xlsx"]:
    z=zipfile.ZipFile(f"{D}/{fn}"); print("\n##",fn); print([n for n in z.namelist()])
    for n in z.namelist():
        if n.endswith('.xml') or n.endswith('.rels'):
            s=z.read(n).decode('utf8','ignore')
            for pat in ['w:vanish','w:del ','w:ins ','w:comment','show="0"','hidden','state=','<w:color w:val="FFFFFF"','FFFFFF','sz w:val="2"','w:highlight']:
                if pat in s: print(n, "contains", pat, s.count(pat))
