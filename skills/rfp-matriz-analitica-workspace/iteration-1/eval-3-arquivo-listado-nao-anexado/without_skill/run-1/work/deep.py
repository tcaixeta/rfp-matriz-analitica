import sys, pdfplumber, zipfile, openpyxl, pptx
d=sys.argv[1]
with pdfplumber.open(f"{d}/RFP-2026-017_Servicos_SOC_IAM.pdf") as pdf:
    for i,p in enumerate(pdf.pages,1):
        cols=set((c.get('non_stroking_color'),round(c['size'])) for c in p.chars)
        print(i,"chars",len(p.chars),"imgs",len(p.images),"annots",len(p.annots or []),"cols",cols)
    p=pdf.pages[5]; print(repr(p.extract_text()))
    print(pdf.doc.catalog if hasattr(pdf.doc,'catalog') else '')
z=zipfile.ZipFile(f"{d}/Anexo_I_Especificacao_Tecnica.docx")
print(z.read("customXml/item1.xml")[:500])
print(z.read("docProps/app.xml")[:800])
pr=pptx.Presentation(f"{d}/Apresentacao_Ambiente_Atual.pptx")
for i,s in enumerate(pr.slides,1):
    print("slide",i,"hidden",s._element.get('show'), [ (sh.shape_type, sh.name) for sh in s.shapes])
z=zipfile.ZipFile(f"{d}/Apresentacao_Ambiente_Atual.pptx"); print([n for n in z.namelist() if 'comment' in n.lower() or 'media' in n])
wb=openpyxl.load_workbook(f"{d}/QA_Rodada1_e_Questionario.xlsx")
print(wb.defined_names, )
for ws in wb.worksheets:
    print(ws.title, {k:v.hidden for k,v in ws.row_dimensions.items() if v.hidden}, {k:v.hidden for k,v in ws.column_dimensions.items() if v.hidden}, ws.data_validations.dataValidation)
z=zipfile.ZipFile(f"{d}/QA_Rodada1_e_Questionario.xlsx"); print(z.namelist())
