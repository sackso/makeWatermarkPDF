import PyPDF2

#pdf_file = "c:/tempdata/ENOVIA-R2019x-Apps-FD01.pdf"
pdf_file = "c:/tempdata/MQL-Programmers-Guide.pdf"
watermark = "c:/tempdata/donotcopy.pdf"
merged_file = "c:/tempdata/merged.pdf"

input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

output = PyPDF2.PdfFileWriter()
merged_file = open(merged_file,'wb')

inputFilePages = input_pdf.getNumPages()
print("inputFilePages=>",inputFilePages)

watermark_page = watermark_pdf.getPage(0)

x = 0
while x < inputFilePages:
    print("",round((x/inputFilePages) * 100,2),"% completed" )
    pdf_page = input_pdf.getPage(x)    
    pdf_page.mergePage(watermark_page)
    output.addPage(pdf_page)
    output.write(merged_file)
    x = x + 1


merged_file.close()
watermark_file.close()
input_file.close()