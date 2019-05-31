        #______________Segmentation of seneteces___________
import spacy 
nlp = spacy.load('en_core_web_sm')

doc = nlp(u"Yes I am in, with your corporation and I will work with the thinds. So what about you?")

for sents in doc.sents:
    print(sents)
    
#__________Creating new segmentation RUle___________
''' Let I want to make a new segment after the commas'''

def new_seg_rule(doc):
    for token in doc:
        if token.text == ',':
            doc[token.i+1].is_sent_start = true
    return doc
nlp.add_pipe(new_seg_rule,before = 'Parser')

     
