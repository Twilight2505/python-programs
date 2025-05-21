from pypdf import PdfWriter
import os
merger = PdfWriter()
def mergepdf(path):
 files=os.listdir(path)
 for file in files:
    if file.endswith(".pdf"):
            print(file)
    
            merger.append(f"{path}/{file}")
            merger.write("merged-pdf.pdf")
            merger.close()


mergepdf(r"C:\Users\LENOVO\Documents\pdfs")
