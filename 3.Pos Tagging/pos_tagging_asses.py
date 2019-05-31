import spacy
nlp = spacy.load('en_core_web_sm')

from spacy import displacy

with open('text file/test_file.txt') as f:
    doc = nlp(f.read())
    
    
#####_________Showing the pos_ , tag_ , explain_ __________##############

for token in list(doc.sents)[0]:
    print(f'{token.text:{15}}{token.pos_:{15}}{token.tag_:{15}}{str(spacy.explain(token.tag_))}')
    
    
#####_______Showing the frequency list__________ ##########

print('Tag_Number', '|Tag_Name' , '|Tag_Occured')
for tag_num,tag_occured in sorted(count.items()):
    print(f'{tag_num:<{10}} | {doc.vocab[tag_num].text:{8}}|{tag_occured:<{10}}')
    
    
#####_______Showing the percentage of noun__________ ##########

len(doc)
count[92]
(count[92]/len(doc)) *100

#####_______Displaying the pos dependency__________ ##########

displacy.render(list(doc.sents)[0],style:'dep', jupyter = True)

#######_______SHowing first two entities in doc_________#########

doc.ents

for ents in doc.ents[:4]: # first four entities
    print(ents.text + ' ---------------' + ents.label_ + '-----------' + str(spacy.explain(ents.label_)))
    
#############_______How many senteces contain name entities____________############

list_of_sents = [nlp(sents.text) for sents in doc]

list_of_sen_with_entities = [doc for doc in list_of_sents if doc.ents]
len(list_of_sen_with_entities)    
