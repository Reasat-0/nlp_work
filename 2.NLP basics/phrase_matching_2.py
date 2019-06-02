import spacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)


with open('text file/test_file.txt') as f:
    doc = nlp(f.read())
    
phrases_to_find = ['Contributor','License','Code','means']
#----------Changing the phrase to a nlp object----------------

phrase_doc_obj = [nlp(text) for text in phrases_to_find]

matcher.add('File_text_finder',None,phrase_doc_obj)