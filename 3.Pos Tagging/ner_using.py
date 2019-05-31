#________Name Entity Relationship_________

doc_ner = nlp(u'Apple is going to start their business in Chicago')

doc_non_ner = nlp(u'Hey..how r u ??')
def show_entities(doc):
    if doc.ents:
        for entities in doc.ents:
            print(entities.text + '-' + entities.label_ + '-' + str(spacy.explain(entities.label_)))
    else:
        print('No entities found')

        
show_entities(doc_ner)
    
        #______________Entering value into an entity__________________
        
doc = nlp(u"Tesla is starting their business in Dhaka") #we will enter Tesla as an ORG entity

from spacy.tokens import Span
ORG = nlp.vocab.strings[u"ORG"]

new_span = Span(doc,0,2,label=ORG)

doc.ents = list(doc.ents) + [new_span]


        #____________Entering a phrase value in our Entity list________
#--- To do this we will need to create a matcher

doc = nlp(u"We are about to launch our new product vacuum cleaner as titles vacuum-cleaner")

phrase_list = ['vacuum cleaner','vacuum-cleaner']

phrase = [nlp(text) for text in phrase_list]

from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

matcher.add('Product',None,*phrase)

found = matcher(doc)
print(found)

#-- now we will import the phrases into our entity

from spacy.tokens import Span
product = nlp.vocab.strings[u"PRODUCT"]

new_span = [Span(doc,match[1],match[2],label = product) for match in found ]

doc.ents = list(doc.ents) + new_span

show_entities(doc)

        #_________TO check how many times an entity is there in a doc__________
doc2 = nlp(u'Bangladesh is keeping a good relation with Japan, Korea , China and India')
[entities for entities in doc2.ents if ents.label = "GPE"]    # it will show the GPE entities 
len([entities for entities in doc2.ents if ents.label = "GPE"]) # it will show the GPE entities number