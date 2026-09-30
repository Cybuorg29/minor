import PyPDF2
 
#open the pdf
pdfFileObj = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
#get the text from the specified page
pageObj = pdfReader.getPage(0)
 
#print the text from the page
print(pageObj.extractText())