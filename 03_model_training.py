import pandas as pd
import gensim
from gensim import corpora


corpus_model = pd.read_csv('corpus_model.csv')

#LDA prep

id2word = corpora.Dictionary(corpus_model)

id2word.filter_extremes(no_below=5)

corpus = [id2word.doc2bow(text) for text in corpus_model]

num_topics = 7

model = gensim.models.ldamulticore.LdaMulticore(corpus, id2word=id2word, num_topics=num_topics, eval_every = None)

