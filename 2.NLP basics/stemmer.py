# _________POrter Stemming______________

from nltk.stem.porter import PorterStemmer

p_stem = PorterStemmer()

box = ['play','played','plays','playing','player']
for words in box:
    print( words + '--->' + p_stem.stem(words))
    
    
#__________Snowball Stemming____________

from nltk.stem.snowball import SnowballStemmer

s_stem = SnowballStemmer(language = 'english')


for words in box:
    print(words + '>>>' + s_stem.stem(words))