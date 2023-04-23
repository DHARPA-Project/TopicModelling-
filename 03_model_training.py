import pandas as pd
import gensim
from gensim import corpora
from gensim.models import LdaModel
from gensim.test.utils import datapath
from ast import literal_eval


corpus_model = pd.read_csv('corpus_model.csv')

# la ligne suivante est nécessaire car la conversion en csv transforme les arrays en string, ce qui est problématique car ensuite le id2word ne marche pas
# on pourra enlever cela quand on passera avec un ystème BDD
# le temps de processing est assez long
bigrams = corpus_model['bigrams'].apply(literal_eval)

#LDA prep

id2word = corpora.Dictionary(bigrams)

id2word.filter_extremes(no_below=5)

corpus = [id2word.doc2bow(text) for text in bigrams]

num_topics = 7

model = LdaModel(corpus, id2word=id2word, num_topics=num_topics, random_state=100, eval_every = None)

#saving model to file

model_file = datapath("/Users/mariellacc/Documents/GitHub/MLOps-TopicModeling/lda_model")

model.save(model_file)