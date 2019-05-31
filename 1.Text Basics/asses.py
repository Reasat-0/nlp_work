#1. 
fir = "NLP"
sec = "Natural Language Processing"

print(f'{fir} stands for {sec}')

#2.
%%writefile assesfile.txt
first_name,last_name,email...etc

#3. 
with open('assesfile.txt') as f:
    file_object = f.read()s
    print(file_object)

#4.
import PyPDF2

file = open('Neuro.pdf')

pdf_reader = PyPDF2.PdfFileReader(file)

page_num = pdf_reader.getPage(0).extractText()

print(page_num)

#5.

with open('assesfile.txt','a+')as f:
    f.write(page_num)
    f.seek(0)
    print(f.read())
    
#to take from a position of a page...
    f.write(page_num[8:]
            
#6. regular expression to find email

pattern = r'[\w]
    
    

    
 