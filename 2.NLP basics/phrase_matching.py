import spacy
nlp = spacy.load('en_core_web_sm')


from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

pattern1 = [{'Lower':'solarpower'}]
pattern2 = [{'Lower': 'solar'}, {'IS_PUNC': True}, {'Lower':'power'}]
pattern3 = [{'Lower': 'solar'},{'Lower':'power'}]


matcher.add('Solar',None,pattern1,pattern2,pattern3)

doc = nlp(u'The solar-power industry is growing up now-a-days. Solar Power distribution is invlolving by govt and now solarpower is getting polpular day by day')


find = matcher(doc)

#print(find)


for matched_id,start,end in find:
    string_id = nlp.vocab.strings[matched_id] #-----------------Finding the matched pattern name
    span = doc[start: end] # -----------------------------------Finding the pattern matched pattern string
    print(matched_id,string_id,start,end,span)

#--------To remove the saved pattern form the matcher object....

matcher.remove('Solar')

pattern1 = [{'Lower':'solarpower'}]
pattern2 = [{'Lower': 'solar'}, {'IS_PUNC': True,'OP':'*'}, {'Lower':'power'}] #-------thE '*' means punctuation can be zero or more times