import sys, pdfplumber
with pdfplumber.open(sys.argv[1]) as pdf:
    p=pdf.pages[5]; print(p.images[0]['x0'],p.images[0]['top'],p.images[0]['x1'],p.images[0]['bottom'], p.width,p.height)
    p.to_image(resolution=150).save(sys.argv[2]+"/p6.png")
