import spacy
nlp = spacy.load('en_core_web_sm')

with open('text file/test_file.txt') as f:
    doc = nlp(f.read())
    
    
len(doc)


#_____Counting Sentece in a doc_____

doc_sent = [sent for sent in doc.sents] #[ ] creates a list

len(doc_sent)

#_____Grabbing the 2nd sentence in the doc________

second_sent = doc_sent[1]

print(second_sent.text)

#_____finding the token text,pos,dep and lemmas
for token in doc:
    print(f'{token.text:{10}},{token.pos_:{10}},{token.dep_:{10}},{token.lemma_:{10}}')
    
    
#------------Using Matcher find a word otherwise making

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

pattern = [{'LOWER': 'otherwise'},{'IS_SPACE': True, 'OP': '*'},{'LOWER': 'making'}]

matcher.add('c_version',None,pattern)

searched = matcher(doc)

print(searched)


#____________Finding the surrounding of the found things___________[(16255491138983776732, 24, 26)]

def surrounding(doc,start,end):
    print(doc[start-5:end+5]) # +5 means 5 words after the end... -5 means 5 words befor the start
    
surrounding(doc,24,26)

#__________printing the sentence that contains the things found

for sentence in doc_sent:
    if searched[0][1] < sentence.end:
        print(sentence)
        break


