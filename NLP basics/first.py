import spacy

nlp = spacy.load('en_core_web_sm')

message = nlp(u'This is a text to the president of U.A.E . Hey!!! why dont u receive this')

#message = nlp(u'This is a text to the president of U.A.E . Hey!!! why dont u receive this')
for token in message:
    print(token.text,token.pos_,token.dep_)
    
message[3].pos_


email_text = nlp(u'This is the Bangladesh Programmers Team. Contact us as bd_programmers2@gmail.com')
for token in email_text:

    
len(email_text)

len(email_text.vocab) #it will say the vocab of the library we loaded....

# Name entities..... 

name_ent = nlp(u'Samsung is about to launch their very latest phone s10+ in Bangladesh')


for entity in name_ent.ents:
    print(entity,end = ' ')
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))

    
#NOun chunks --- mean an extra word describing the noun

noun_chunk = nlp(u'An automobile company is about to start up with their business in Bangladesh')

for chunk in noun_chunk.noun_chunks:
    print(chunk)





