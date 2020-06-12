ldamodel = gensim.models.wrappers.ldamallet.malletmodel2ldamodel(ldamallet)
dictionary = id2word
corpus_csc = gensim.matutils.corpus2csc(corpus, num_terms=len(dictionary))
import numpy as np
vocab = list(dictionary.token2id.keys())
vocab = pd.Series(vocab, name='vocab')
fnames_argsort = np.asarray(list(dictionary.token2id.values()), dtype=np.int_)
term_frequency = corpus_csc.sum(axis=1).A.ravel()[fnames_argsort]
term_frequency = pd.Series(term_frequency,name='term_frequency')
doc_length = corpus_csc.sum(axis=0).A.ravel()
doc_length = pd.Series(doc_length, name='doc_length')
# topic weights for each document in the corpus
doc_topic_weights = ldamodel.inference(corpus)[0]
doc_topic_dists = doc_topic_weights / doc_topic_weights.sum(axis=1)[:, None]
# put data into dataframe
doc_topic_dists = pd.DataFrame(doc_topic_dists)
doc_topic_dists.index.name = 'doc'
doc_topic_dists.columns.name = 'topic'
topic_term = ldamodel.state.get_lambda() # topics term matrix: https://stackoverflow.com/questions/42289858/extract-topic-word-probability-matrix-in-gensim-ldamodel
topic_term_dists = topic_term / topic_term.sum(axis=1)[:, None]
topic_term_dists = topic_term_dists[:, fnames_argsort]
topic_term_dists = pd.DataFrame(topic_term_dists)
topic_term_dists.index.name = 'topic'
topic_term_dists.columns.name = 'term'
topic_freq = (doc_topic_dists.T * doc_length).T.sum()
topic_proportion = (topic_freq / topic_freq.sum()).sort_values(ascending=False)
topic_order = topic_proportion.index
topic_freq = topic_freq[topic_order]
topic_term_dists = topic_term_dists.iloc[topic_order]
doc_topic_dists = doc_topic_dists[topic_order]
# token counts for each term-topic combination (widths of red bars)
term_topic_freq = (topic_term_dists.T * topic_freq).T
term_frequency = np.sum(term_topic_freq, axis=0)
term_proportion = term_frequency / term_frequency.sum()
topic_given_term = topic_term_dists / topic_term_dists.sum()
kernel = (topic_given_term * np.log((topic_given_term.T / topic_proportion).T))
distinctiveness = kernel.sum()
saliency = term_proportion * distinctiveness
default_term_info = pd.DataFrame({
  'saliency': saliency,
  'Term': vocab,
  'Freq': term_frequency,
  'Total': term_frequency,
  'Category': 'Default'})
# Sort terms for the "default" view by decreasing saliency and display only the R first lines:
default_term_info = default_term_info.sort_values(
  by='saliency', ascending=False).head(R).drop('saliency', 1)
# Rounding Freq and Total to integer values
default_term_info['Freq'] = np.floor(default_term_info['Freq'])
default_term_info['Total'] = np.floor(default_term_info['Total'])
ranks = np.arange(R, 0, -1)
default_term_info['logprob'] = default_term_info['loglift'] = ranks
log_lift = np.log(topic_term_dists / term_proportion)
log_ttd = np.log(topic_term_dists)
lambda_seq = np.arange(0, 1 + 0.01, 0.01) # lambda_step=0.01
def topic_top_term_df(tup):
        new_topic_id, (original_topic_id, topic_terms) = tup
        term_ix = topic_terms.unique()
        return pd.DataFrame({'Term': vocab[term_ix],
                             'Freq': term_topic_freq.loc[original_topic_id, term_ix],
                             'Total': term_frequency[term_ix],
                             'logprob': log_ttd.loc[original_topic_id, term_ix].round(4),
                             'loglift': log_lift.loc[original_topic_id, term_ix].round(4),
                             'Category': 'Topic%d' % new_topic_id})
from joblib import Parallel, delayed, cpu_count
# Technical parameters for further processing
lambda_step = 0.01 #interstep distance on which to iterate when computing relevance
n_jobs = -1 #number of cores to be used to do the computations (-1 = all cores)
lambda_seq = np.arange(0, 1 + lambda_step, lambda_step)
def _chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]

def _job_chunks(l, n_jobs):
    n_chunks = n_jobs
    if n_jobs < 0:
        n_chunks = cpu_count() + 1 - n_jobs

    return _chunks(l, n_chunks)

def _find_relevance_chunks(log_ttd, log_lift, R, lambda_seq):
    return pd.concat([_find_relevance(log_ttd, log_lift, R, l) for l in lambda_seq])

def _find_relevance(log_ttd, log_lift, R, lambda_):
    relevance = lambda_ * log_ttd + (1 - lambda_) * log_lift
    return relevance.T.apply(lambda s: s.sort_values(ascending=False).index).head(R)
top_terms = pd.concat(Parallel(n_jobs=-1)
                          (delayed(_find_relevance_chunks)(log_ttd, log_lift, R, ls)
                          for ls in _job_chunks(lambda_seq, n_jobs))) #n jobs = -1
topic_dfs = map(topic_top_term_df, enumerate(top_terms.T.iterrows(), 1))
topic_info = pd.concat([default_term_info] + list(topic_dfs), sort=True)
topic_proportion_df = pd.DataFrame(topic_proportion, columns = ['proportion'])
topic_proportion_df.index.name = 'topic_id'
import csv
topic_info.to_csv('topic_info.csv')
topic_proportion_df.to_csv('topic_proportion.csv')