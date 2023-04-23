# link to custom stop words: https://drive.google.com/file/d/1VVfW6AKPbb7_fICOG73lEgkXmmZ6BkpC/view?usp=sharing
# Upload stop words list into Colab files before proceeding with the next cells

import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
import gensim
from gensim import models

corpus_df = pd.read_csv('subset.csv')

# add tokenized documents in dataframe
corpus_df['tokens'] = corpus_df['file_content'].apply(lambda x: nltk.word_tokenize(x))

# add new column in df with processed tokens (here: keeping only alpha tokens longer than 3 characters + lowercasing)
corpus_df['doc_prep'] = corpus_df['tokens'].apply(lambda x: [w.lower() for w in x if (w.isalpha() and len(w) > 2 )])

ital_stopwords = stopwords.words('italian')
en_stopwords = stopwords.words('english')

# import custom stop words list
stop_words = pd.read_csv('stop_words.csv')

stopwords = stop_words['stopword'].values.tolist()

# add english and italian stop words list to custom stopwords 
stopwords.extend(en_stopwords)
stopwords.extend(ital_stopwords)

# add column with preprocessed corpus
corpus_df['doc_prep_nostop'] = corpus_df['doc_prep'].apply(lambda x: [w for w in x if not w in stopwords])


# bigrams

# to be adjusted to the corpus
threshold = 20
min_count = 3

# apply to the whole corpus
bigram = gensim.models.Phrases(corpus_df['doc_prep_nostop'], min_count=min_count, threshold=threshold)
bigram_mod = gensim.models.phrases.Phraser(bigram)

corpus_df['bigrams'] = [bigram_mod[doc] for doc in corpus_df['doc_prep_nostop']]

corpus_model = corpus_df['bigrams']

corpus_model.to_csv('corpus_model.csv')