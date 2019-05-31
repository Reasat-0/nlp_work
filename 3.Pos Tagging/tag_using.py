import spacy
nlp = spacy.load('en_core_web_sm')


doc = nlp(u'This is the doc object sentence')


doc[1].pos_
doc[1].tag_


print(f'Token_name--------  Pos --------------- Tag ------- Tag explanation\n' )
for token in doc:
    print(f'{token.text:{20}}{token.pos_:{20}}{token.tag_:{10}}{spacy.explain(token.tag_)}')


doc2 = nlp(u'I read a book on nlp')


for token in doc2:
    print(f'{token.text:{20}}{token.pos_:{20}}{token.tag_:{10}}{spacy.explain(token.tag_)}') #it will get that its a singular present 


#_______Counting The parts of speech in a sentence_________

count = doc.count_by(spacy.attrs.POS)

count


doc.vocab[85].text   

#_____Showing the list of the pos tags______
print('Tag_Number', '|Tag_Name' , '|Tag_Occured')
for tag_num,tag_occured in sorted(count.items()):
    print(f'{tag_num:<{10}} | {doc.vocab[tag_num].text:{8}}|{tag_occured:<{10}}')