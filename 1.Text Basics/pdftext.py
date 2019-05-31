import PyPDF2

mypdf = open('Neuro.pdf',mode='rb') 

pdf_reader = PyPDF2.PdfFileReader(mypdf)

pdf_reader.numPages

page = pdf_reader.getPage(0)

text = page.extractText()

print(text)


#Creating a new pdf

new = open('MyPdf.pdf','wb')

#writing in the new pdf

fetch = open('Neuro.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(fetch)

page = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(page)

pdf_writer.write(new)


#Copying A whole pdf to a list...or box

fetching = open('SVM.pdf','rb') #get the pdf from where we can read
read_pdf = PyPDF2.PdfFileReader(fetching)


text_box = []   #creating an empty box



for p in range(read_pdf.numPages):
    page = read_pdf.getPage(p)    
    text_box.append(page.extractText)
fetching.close()