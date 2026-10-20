import sys, pdfplumber, docx, pptx, openpyxl
D, W = sys.argv[1], sys.argv[2]
# PDF
with pdfplumber.open(f"{D}/RFP-2026-017_Servicos_SOC_IAM.pdf") as pdf, open(f"{W}/rfp.txt","w") as f:
    for i,p in enumerate(pdf.pages,1):
        f.write(f"\n===== PAGINA {i} =====\n"); f.write(p.extract_text() or "")
        for t in p.extract_tables():
            f.write("\n[TABELA]\n")
            for r in t: f.write(" | ".join(str(c) for c in r)+"\n")
# DOCX
d = docx.Document(f"{D}/Anexo_I_Especificacao_Tecnica.docx")
with open(f"{W}/anexo.txt","w") as f:
    body = d.element.body
    for el in body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag=='p':
            p = docx.text.paragraph.Paragraph(el,d)
            if p.text.strip(): f.write(f"[{p.style.name}] {p.text}\n")
        elif tag=='tbl':
            t = docx.table.Table(el,d); f.write("[TABELA]\n")
            for r in t.rows: f.write(" | ".join(c.text for c in r.cells)+"\n")
    for s in d.sections:
        for p in s.header.paragraphs+s.footer.paragraphs:
            if p.text.strip(): f.write(f"[HDR/FTR] {p.text}\n")
# PPTX
pr = pptx.Presentation(f"{D}/Apresentacao_Ambiente_Atual.pptx")
with open(f"{W}/ppt.txt","w") as f:
    for i,s in enumerate(pr.slides,1):
        f.write(f"\n===== SLIDE {i} =====\n")
        for sh in s.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip(): f.write(sh.text_frame.text+"\n")
            if getattr(sh,'has_table',False) and sh.has_table:
                for r in sh.table.rows: f.write(" | ".join(c.text for c in r.cells)+"\n")
        if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip():
            f.write("[NOTAS] "+s.notes_slide.notes_text_frame.text+"\n")
# XLSX
wb = openpyxl.load_workbook(f"{D}/QA_Rodada1_e_Questionario.xlsx")
with open(f"{W}/xlsx.txt","w") as f:
    for ws in wb.worksheets:
        f.write(f"\n===== ABA {ws.title} ({ws.sheet_state}) =====\n")
        for r in ws.iter_rows(values_only=True):
            if any(c is not None for c in r): f.write(" | ".join("" if c is None else str(c) for c in r)+"\n")
