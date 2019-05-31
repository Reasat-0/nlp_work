#Creating a file 

%%writefile Note.txt
This is my file containing a lots of notes

myfile = open('Note.txt') #the myfile object here is storing the file 


#reading the file 

myfile.read()  #but it reads just a single time. if i write it again. it wont work...cause it will start reading from the end of file..
myfile.read() #it will show a null character

#Reseting the character of read()

myfile.seek(0) #now it will start from the 0 index of myfile

#closing the file...

myfile.close() '''Closing is necessry because..if i dont close it.. it will not be usable by other programs.or apps '''


mylines = myfile.readline() ''' it will show the lines separately in a text file'''

for line in mylines:
	print (line[0]) #it will print all the first letter of each line

for line in mylines:
	print (line.split()[0]) 

'''===========Writing the file================='''

myfile = open('Note.txt','w+')   #it will clear the file 

myfile.write("This is new text")


#appending texts in a file 

myfile = open('Note.txt','a+')
myfile.write("This is newly added text")