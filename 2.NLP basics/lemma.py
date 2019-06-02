import spacy

nlp = spacy.load('en_core_web_sm')

test_string = nlp(u'This is a running space where I used to run a race with my running partners who ran with me')

for token in test_string:
    print(token.text,' | ' token.pos , ' | ' , token.lemma_)
    
    
    
# ----------- DOing this using a function----------------

def lemmati(text):
    for token in text:
        print(f'{token.text:{8}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_:}' )

                
lemmati(test_string)