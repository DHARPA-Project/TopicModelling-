import pandas as pd
import gensim
from gensim.models import LdaModel
from gensim.models.coherencemodel import CoherenceModel
from gensim.test.utils import datapath
from ast import literal_eval
from gensim import corpora

corpus_model = pd.read_csv('corpus_model.csv')

# la ligne suivante est nécessaire car la conversion en csv transforme les arrays en string, ce qui est problématique car ensuite le id2word ne marche pas
# on pourra enlever cela quand on passera avec un ystème BDD
# le temps de processing est assez long
bigrams = corpus_model['bigrams'].apply(literal_eval)
id2word = corpora.Dictionary(bigrams)
id2word.filter_extremes(no_below=5)
corpus = [id2word.doc2bow(text) for text in bigrams]

# examples to load presaved model https://radimrehurek.com/gensim/models/ldamodel.html

lda_model = datapath("/Users/mariellacc/Documents/GitHub/MLOps-TopicModeling/lda_model")
dictionary = datapath("/Users/mariellacc/Documents/GitHub/MLOps-TopicModeling/lda_model.id2word")

#loading model from disk
lda = LdaModel.load(lda_model)

coherencemodel = CoherenceModel(model=lda, texts=bigrams, corpus=corpus, dictionary=dictionary, coherence='u_mass')
coherence_value = coherencemodel.get_coherence()

print(coherence_value)



