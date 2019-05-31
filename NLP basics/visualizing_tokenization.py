import spacy 
from spacy import displacy

nlp= spacy.load('en_core_web_sm')


vis = nlp(u'Samsung is about to launch their very latest phone s10+ in Bangladesh')


displacy.render(vis,style='dep',jupyter=True,options = {'distance':100}) #here dep means dependency showing

displacy.render(vis,style='ent',jupyter=True, options = {'distance':100})


# Whn u r working in other server except jupyter notebook

displacy.serve(vis,style='dep')