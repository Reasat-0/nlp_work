
#search one of these... known as pipe operator

re.search(r"boy|girl","The boy is here")

#searching for a digit at start or end of a sentence

re.findall(r'\d$','Count 6')
re.findall(r'^\d','5 boys r there')


#excluding digit from a text

text = 'Hey!!!!!!!There i m having 3 pipes fitted into 5 and entertaining my 4 boys. '
re.findall(r'[^\d+ ]',text)


#excluding digit from a text

text = 'Hey!!!!!!!There i m having 3 pipes fitted into 5 and entertaining my 4 boys...Do u wanna join guyssss??????'
excluding = re.findall(r'[^\!.? ]',text)  #it will store the words in a list

#joining the list words
' '.join(excluding)

sen = "This a sentence where i m going to check the + sign works for hyphen...it will take once-or more...from both side"
re.search(r'[\w]+-[\w]+',sen)

