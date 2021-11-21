from PyPDF2 import PdfFileReader,PdfFileWriter
import os

infile = "需要处理的文件.pdf"


def split_pdf(infile):
    filename = os.path.splitext(infile)[0]
    os.mkdir(filename)
    pdf_in = PdfFileReader(open(infile,"rb"))
    page_count = pdf_in.numPages
    for i in range(page_count):
        page = pdf_in.getPage(i)
        pdf_out = PdfFileWriter()
        pdf_out.addPage(page)
        path = "./"+filename+"/"+ filename +"第%d页" % (i+1) + ".pdf"
        pdf_out.write(open(path,"wb"))


split_pdf(infile)