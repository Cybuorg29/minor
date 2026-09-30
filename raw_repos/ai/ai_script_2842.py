# install the required package
pip install pdfminer.six

# importing all the required modules 
from pdfminer.pdfparser import PDFParser 
from pdfminer.pdfdocument import PDFDocument 

# open the pdf file 
fp = open('sample_form.pdf', 'rb') 

# create parser object 
parser = PDFParser(fp) 

# create pdf document object 
doc = PDFDocument(parser) 

# get the text data from pdf file 
data = doc.get_data() 

# print the text extracted 
print(data)