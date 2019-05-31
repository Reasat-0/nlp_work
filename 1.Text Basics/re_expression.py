import re


text = "Search any word of this text...lets see what text u gonna find"

pattern = "text"

search = re.search(pattern,text) #this wont show that the text is here ffor 2 times


search.span()


search2 = re.findall(pattern,text)

len(search2)

###Diffrent pattern 

mobile = "Call me here 880 1818-90 82 89"

pattern = r'\d\d\d\s\d\d\d\d-\d\d\s\d\d\s\d\d'

phone_number_searched = re.search(pattern,mobile)

print(phone_number_searched)

phone_number_searched.group()    #it will show tthe found thing separately


