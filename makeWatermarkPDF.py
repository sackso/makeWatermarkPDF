import PyPDF2

#pdf_file = "c:/tempdata/ENOVIA-R2019x-Apps-FD01.pdf"
pdf_file = "c:/tempdata/MQL-Programmers-Guide.pdf"
watermark = "c:/tempdata/donotcopy.pdf"
merged_file = "c:/tempdata/merged.pdf"

input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

merged_file = open(merged_file,'wb')
output_pdf = PyPDF2.PdfFileWriter()

inputFilePages = input_pdf.getNumPages()
#print("inputFilePages=>",inputFilePages)

watermark_page = watermark_pdf.getPage(0)
watermark_page.compressContentStreams()

#페이지마다 읽어들여서 합치기
x = 0
while x < inputFilePages:
    print("",round((x/inputFilePages) * 100,2),"% completed" )
    pdf_page = input_pdf.getPage(x)    
    pdf_page.compressContentStreams()
    pdf_page.mergePage(watermark_page)
    #pdf.filters.compress(output)
    output_pdf.addPage(pdf_page)
    x = x + 1

output_pdf.write(merged_file)

merged_file.close()
watermark_file.close()
input_file.close()
