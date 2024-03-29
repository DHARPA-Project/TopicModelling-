# Topic Modelling with Gensim - A workflow for the Humanities

As digitally available textual repositories are becoming larger and larger, the relevance of distant reading for the humanities has grown exponentially. Traditional close reading methods are no longer sufficient to analyse such unprecedented mass of digital data, therefore humanities scholars are confronted more and more with the challenge of having to use quantitative techniques in their research. One such quantitative technique is Topic Modelling (TM), a computational, statistical method to discover patterns and topics in large collections of unstructured text. With this repository, the [**DHARPA Project**](https://dharpa-project.github.io/) (Digital History Advanced Research Projects Accelerator) aims to offer a step-by-step guide to a comprehensive and generalizable TM workflow that could be applied transversely across different datasets. The intention is to make the TM technique more transparent and accessible for humanities scholars, assisting them in taking up an active role in the digital analysis process and claiming ownership of their interventions. This workflow is partially based on [Viola and Verheul](https://academic.oup.com/dsh/advance-article/doi/10.1093/llc/fqz068/5601610) (2019).

*Workflow created by [Dr Lorella Viola](https://www.c2dh.uni.lu/de/people/lorella-viola) and [Mariella de Crouy-Chanel](https://www.c2dh.uni.lu/people/mariella-de-crouy-chanel)*

## Table of contents

1. [The DHARPA Project](#1-the-dharpa-project)
2. [Topic Modelling](#2-topic-modelling)

   2.1 [What is a topic?](#21-what-is-a-topic)
   
   2.2 [When should I use TM?](#22-when-should-i-use-tm)
  
3. [Getting started](#3-getting-started)
4. [Installation](#4-installation)
5. [A critical approach to preparing the data](#5-a-critical-approach-to-preparing-the-data)

   5.1 [Preparing the data (1 of 2)](#51-preparing-the-data-1-of-2)
   
   5.2 [Preparing the data (2 of 2)](#52-preparing-the-data-2-of-2)
   
6. [Building the topic model](#6-building-the-topic-model)

   6.1 [Determining the 'optimal' number of topics](#61-determining-the-optimal-number-of-topics)
   
   6.2 [Perplexity and coherence](#62-perplexity-and-coherence)
   
7. [Understanding the topics through visualisation](#7-understanding-the-topics-through-visualisation)
8. [Topics' distribution](#8-topics-distribution)
9. [Historicise the topics](#9-historicise-the-topics)

   9.1 [Time is continuous (there are no gaps in my data)](#91-time-is-continuous-there-are-no-gaps-in-my-data)
   
   9.2 [Time is discrete (there are gaps in my data)](#92-time-is-discrete-there-are-gaps-in-my-data)
   
10. [Conclusions](#10-conclusions)
11. [Remarks](#11-remarks)
12. [License](#12-license)
13. [Links](#13-links)
14. [References](#14-references)
15. [The team](#15-the-team)
16. [How to cite](#16-how-to-cite)

## 1. The DHARPA Project
While the ‘digital humanities moment’ has yielded great accomplishments and enthusiastic interdisciplinary cooperations across the humanities and between the humanities and the sciences, concerns have been raised about the little transparency in digital practices as well as the difficulty of replicating studies due to the lack of data access or standardised practices as well as unclear methodological processes (Faull et al 2016; Jakacki et al 2016, 2015; O’ Sullivan 2019). Such concerns have for instance led scholars to claim that digital humanities is still in “search of a methodology” (Dobson 2019) and the metaphor of the 'black box' has started to be used (Smith 2014) to describe the apparent loss of human agency in the digital reseach process. This could be to some extent due to the fact that traditional historical inquiry itself has in some ways been like a “Mechanical Turk,” with the decisions and interventions made by the researcher hidden from view and only the well-oiled and seemingly autonomous product on display. The DHARPA Project aims to reverse this trend. We want to encourage historians and digital humanities scholars to lift the lid, to show how the application of their expertise works in tandem with technology to produce knowledge, how even digitally enabled research is not a product but a process, reliant on the critical engagement of the scholar. In this workflow, we aim to promote a self-reflective analysis of the interaction of technology and humanities practice and we use TM as a case study.   

## 2. Topic Modelling
Before talking about TM and how it works, it is worth spending a few words on what is intended by *topic*. This will also help to clarify how the TM algorithm works, when researchers could consider apply it to their data and how they should understand the output.

## 2.1 What is a topic?
A topic is understood as a set of terms that occur together in a statistically significant way to form a cluster of words. According to this logic, a text can be understood as the combination of such clusters of words, where each cluster is made of words mathematically likely to appear together (Steyvers and Griffiths 2007). The model assumes that a corpus has a fixed number of founding topics and that these topics compose each document of the corpus to varying degrees (Lee 2019). Using contextual information, topic models distinguish when words are used with multiple meanings in different contexts; this ultimately means that the words are also clustered according to similar uses. What happens in practice is that TM runs statistical calculations multiple times until it determines the most likely distribution of words into clusters, i.e. into topics. The procedure guarantees impartial results in terms of which words will appear in each topic, as the topics emerge from the algorithm’s identification of patterns and trends in the texts, rather than the potentially subjective interpretation of the semantic meaning of the words in each document. In this sense, there is no intervention from the researcher. 

## 2.2 When should I use TM?
This analytical tool works best with large collections of unstructured text (i.e., without any machine-readable annotations) and when the main purpose is to obtain a general overview of the topics discussed in a corpus. As long as it is unstructured, the corpus can be just about anything (e.g., emails, newspapers' headlines, newspapers' articles, a standard .txt document). For this, TM is an excellent distant reading technique that may be used as a data exploration method, for instance to categorise documents within a collection without having to read them all. A practical example of its use may be libraries that need to label digital collections for archiving purposes. Its potential, however, is most fully reached when working in tandem with expert knowledge. To help clarify the application of TM and show how it works in practice, in this workflow we will apply TM to real data. Specifically, we will use a subset of *ChroniclItaly 3.0* (Viola 2020), a collection of Italian immigrant newspapers published in the United States between 1898 and 1936.

## 3. Getting started
There are many variations of the TM algorithm and numerous programs and techniques to implement them. The rationale behind all of them, however, is the same: using statistical modelling to discover topics in a textual collection. Among these very many techniques, Latent Dirichlet Allocation (LDA - [Blei, Ng and Jordan 2003](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)) is perhaps the most widely used. In this workflow, we show two ways of using LDA with Python: Gensim, a Python library for topic modelling, document indexing and similarity retrieval which also implements LDA and the Gensim's implementation of Mallet [(McCallum, 2002)](http://mallet.cs.umass.edu), a natural language processing toolkit that uses machine learning applications to work with unstructured texts. Mallet as a software is a widely used TM tool both for research and teaching purposes (Nelson 2010; Graham et al., 2012, 2016), especially in the humanities. In this way, we aim to offer researchers a way to engage critically with the TM methodology; by comparing techniques and results, we promote the full critical engagement of the scholar along each step of the digital research process.

Gensim depends on the Python packages NumPy and Scipy, which must be installed prior to installing Gensim. Although in principle scholars are free to use whichever TM program they feel more comfortable with, a major advantage of using Gensim is its memory efficiency, significantly higher than other software which have often issues handling big data. More information about Gensim, including the offical documentation, can be found [here](https://pypi.org/project/gensim/).

## 4. Installation
Please install Python 3.6 or higher to run the notebook. The notebook makes use
of the dependencies found in `requirements.txt`. Install the dependencies with 
pip by running the following line of code in your terminal.

```sh
pip install -r requirements.txt
```
## 5. A critical approach to preparing the data
Deciding which of the pre-processing operations should be performed depends on many factors such as the language of the dataset, the type of data, the individual research question(s). It is therefore paramount that this step is tackled **critically** by the researcher as each one of their interventions will have consequences on how the TM algorithm will process the data and therefore on the results.

## 5.1 Preparing the data (1 of 2)
This step is concerned with tokenization, lowercasing, stemming, lemmatization, removing stopwords and words with less than three characters, removing noise (e.g., numbers, punctuation marks, special characters). In principle, the entire step is optional as the train-topic command will work on whichever version of the dataset is used. In reality, however, pre-processing the data is key to the analysis for several reasons. First and foremost, it will likely make the TM results more reliable and more interpretable. For instance, running TM on languages that are rich in articles, pronouns, prepositions, etc., will almost certainly result in poorly interpretable topics. Second, pre-processing the data will remove most OCR mistakes which are always present in digital textual collections to various degrees. This is especially true for corpora such as historical datasets, repositories of underdocumented languages, or digitised archives from handwritten texts. Third, it will reduce the size of the collection thus decreasing the required processing power. Fourth, it is *de facto* a data exploration step which will allow the researcher to look more closely at their data.

 Here's a short explanation of each operation:
- **Tokenization**: Split the text into sentences and/or the sentences into words. In other words, this operation establishes the word boundaries (i.e., tokens) a very helpful way of finding patterns. It is also the typical step prior to stemming and lemmatization; 
- **Lowercasing**: Lowercase the words. This operation is a double-edged sword. It can be effective at yielding potentially better results in the case of relatively small datasets or datatsets with a high percentage of OCR mistakes. For instance, if lowercasing is not performed, the algorithm will treat *USA*, *Usa*, *usa*, *UsA*, *uSA*, etc. as distinct tokens, even though they may all refer to the same entity. On the other hand, if the dataset does not contain such OCR mistakes, then it may become difficult to distinguish between homonyms and make interpreting the topics much harder;
- **Stemming/Lemmatization**: Reduce inflection in words (e.g. states --> state). Although similar, stemming should not be confused with lemmatization. While the latter reduces the inflected word to the actual root form (e.g., better --> good), the former outputs a canonical form of the original word (e.g., past and future tense --> present tense), and not the grammatical root. Performing or not either of these operations is very much dependant on the dataset's language as in terms of TM, they may not affect the output *per se*;
- **Removing stopwords and words with less than three characters**: Remove low information words. These are typically words such as articles, pronouns, prepositions, conjunctions, etc. which are not semantically salient. There are numerous stopword lists available for many, though not all, languages which can be easily adapted to the individual researcher's needs. Removing words with less than three characters may additionally remove many OCR mistakes. Both these operations have the dual advantage of yielding more reliable results while reducing the size of the dataset, thus in turn reducing the required processing power. This step can therefore hardly be considered optional in TM;
- **Noise removal**: Remove elements such as punctuation marks, special characters, numbers, html formatting, etc. This operation is again concerned with removing elements that may not be relevant to the text analysis and in fact interfere with it. Depending on the dataset and research question, this operation can become essential.

Each one of these interventions will need to be quantitatively and qualitatively tested and assed by the researcher every time before deciding which ones to actually perform. This is of course true not just for TM, but in general for all NLP tasks. It is important to remember that each one of these steps is an additional layer of text manipualation and has direct, heavy consequences on the data and therefore on the results. It is critical that researchers assess carefully to what degree they want to intervene on their data. For this reason, this part of the digital analysis should not be considered as separate from the analysis of the results or from the results themselves. On the contrary, it is an **integral part** of the entire digital research process. 

## 5.2 Preparing the data (2 of 2)
This step is concerned with transforming the textual data in a format that will serve as an input for training the Gensim LDA model. What happens in practice is that the documents in the collection are converted into a vector representation called Bag of Words (BOW). A BOW is a way to represent the occurrence of words within a document without considering any structural information (e.g., grammar) other than whether known words occur or not in the documents. The intuition behind the BOW model is based on the semantic theory of language usage (Harris, 1954: 156) according to which words that are used and occur in the same contexts tend to purport similar meanings. If the meaning of a word can be inferred by its context, the opposite is true as well: words found in different contexts tend to purport different meanings.

A BOW model involves two things: **1) a dictionary** of known words (i.e., tokens) and **2) a measure** of the presence of such known words. In practice, the dictionary converts the text into numbers by indexing the words. Consider the following example: let's assume I want to create a dictionary for BOW of the following sentence:

```sh
My name is Lorella. What is your name
```
The dictionary will be

```sh
My name is Lorella. What is your name
0   1    2    3      4    2   5    1
```

Now the BOW model will be a list of (word_id, word_frequency) 2-tuples like this:

```sh
[[(0, 1), (1, 2), (2, 2), (3, 1), (5, 1)]]
```

There are different ways to design the dictionary and to calculate the presence of words. For instance, it is possible to map the text as it is by using sheer frequency (as in the example above), by calculating  inverse of document frequency (TF–IDF) or by using collocations (bigrams). **TF-IDF** is a statistical calculation that aims to reflect how important a word is (i.e., weight) to a document in a collection of texts (Rajaraman & Ullman 2011). The TF–IDF value increases proportionally to the number of times a word appears in the document in relation to the number of documents in the corpus that contain that word. This calculation accounts for the fact that some words appear more frequently in general and therefore, their weight is relative. **Bigrams** are contiguous sequences of two items from a text and they may provide a way to identify meaningful collocations. It should be said, however, that bigrams *per se* do not necessairily entail meaningful results, as not all consecutive words automatically reflect phrases. Thus, they need to be paired with methods to filter for the most meaningful sequences that will then be more likely to be collocations. 

Choosing one method over another determines the complexity of the model and, as any other step, ultimately impacts the results. In this workflow, we will experiment with both TF-IDF and bigrams to compare the different outputs and critically assess each method.

## 6. Building the topic model
Once the corpus and the dictionary have been created, the LDA model can be trained. The only parameter that still needs to be provided is the number of topics, which of course is not known in advance and therefore, the first time, will be arbitrary. 

## 6.1 Determining the 'optimal' number of topics
In literature, there is disagreement about how the number of topics should be determined. Some researchers confide in statistical methods (i.e. perplexity, coherence score) to determine the number of topics that is mathematically more accurate. However, some have found that 'mathematically more accurate' does not automatically entail that the topics will be more interpretable (Jacobi et al., 2015, p. 7). Other researchers prefer running the train-topics command multiple times with a different number of topics and then compare the different models' composition and topics' variety before settling for a more interpretable number (i.e., model). The latter approach allows the researcher to examine the various topic structures carefully before determining the number of topics that seems to offer the most coherent thematic breakdown of the corpus. In this sense, this approach relies heavily on the expert's knowledge. Others yet build many LDA models with different numbers of topics and simply pick the one that gives the highest coherence value. Once more, the critical understanding of how each choice will impact on the results is essential for informed and responsible decision making.   

## 6.2 Perplexity and coherence
Model perplexity and topic coherence are two ways to measure the statistical quality of a topic model as it is believed, though not unanimously, that a higher statistical quality would yield more interpretable topics. **Model perplexity** (also known as predictive likelihood) predicts the likelihood of new (unseen) text to appear based on a pre-trained model. The lower the perplexity value, the better the model predicts the sample, in this case, the words that appear in each topic. However, studies have shown that optimizing a language model for perplexity does not necessairily increase interpretability, as perplexity and human judgment are often not correlated, and sometimes even slightly anti-correlated (Jacobi et al., 2015, p. 7). **Topic Coherence** was developed to compensate for this shortcoming and it has become popular over the years. In reality, what the method does is modelling human judgement by scoring the composition of the topics based on how interpretable they are, i.e., coherent  (Röder, Both and Hinneburg 2015). If the coherence score increases as the number of topics increases, for example, that would suggest that the most interpretable model is the one that gave the highest coherence value before flattening out. In this workflow, we are using the topic coherence method.

## 7. Understanding the topics through visualisation
An effective way to analyse and interpret the topics is by visualising the terms' distributions associated with each topic. In this notebook, we implemented an interactive visualisation tool that helps users to assess the *quality* of individual topics and facilitates the overall interpretability. 

In order to interpret the topics, the first thing to consider is that each topic is a combination of keywords and that each keyword contributes a certain 'weight' to that topic. Understanding the weight of each keyword is crucial to understand how important that keyword is to that topic. The tool provides this information by visualising each keyword's *saliency* (Chuang et. al 2012), defined as the relationship between the likelihood that the observed word *w* was generated by the latent topic T and the likelihood that any randomly-selected word *w'* was generated by topic T. In other words, the saliency represents how informative a specific term is for interpreting a topic, versus a randomly-selected term. The way saliency is visualised is by showing each keyword's overall frequency (in blue) in comparison with the estimated term frequency within the selected topic (in orange). Filtering terms by saliency is helpful for a relatively rapid classification and disambiguation of the topics (ibid.) as well as for the identification of non-informative topics lacking salient terms. 

The terms are also ranked according to *relevance* (Sievert & Shirley 2014). Relevance takes into account the ratio between the probability of a term occurring in a topic and its marginal probability across the corpus (called *lift*). The quantification of the relevance measure results in a value (called apha value) and it ranges from 0 to 1. Setting the alpha value to 1 results in the ranking of terms in decreasing order according to their topic-specific probability. Setting the alpha value to 0 ranks terms solely by their *lift*. Observations conducted by Sievert & Shirley (2014) have shown that setting the alpha value to 0.6, that is in decreasing order of probability, increases the topics' interpretability. In this notebook, the alpha value is therefore set to 0.6.

Finally, it is also possible to obtain a general visualisation of the topics' weight. This is indicated by the size of the circles' areas (i.e., the larger the areas, the higher the weight of the topics in the corpus). The combined visualisation of information about saliency, relevance and weight allows for a relatively rapid and finer analysis of the semantic space shared by the topics, ultimately improving interpretability. 

## 8. Topics' distribution
Once the topics have been interpreted and possibly labeled for convenience, the next natural step would be to examine their distribution per document and over the collection. This allows the researcher to identify discursive patterns thoughout the documents, for instance to discover how widely certain topics were or were not discussed. If the visualisation provided a general overview of the structural composition of the topics - instrumental to their understanding and interpretation - the topics' distribution will reveal their discursive and 'behavioural' quality, for instance by evidencing potential over- or underrepresentations of some topics over others as well as their different distribution within each document and over the whole corpus. Potentially meaningful insights can also be obtained by calculating the distribution across subcollections (e.g., different newspapers' titles, different books) and comparing the results. 

In this notebook, the topics' distribution for each document is calculated through the Gensim's function *inference*

```sh
gensim.models.LdaModel.inference
```

This is calculated by dividing a topic's weight by the weight of all the topics for each document. 

For the topics' distribution over the entire collection, this is 'normalised' in the sense that it is calculated by taking into account the lenght of each document (i.e., number of words). The calculation yields more accurate results, especially when working with collections from different sources with heterogenous documents. 

## 9. Historicise the topics
When working with historical collections of timestamped documents, a step that bears great relevant for humanities scholars who try to answer historical questions is the possibility to plot the topics' distribution over time, i.e., historicise the topics. This truly effective operation in terms of revealing patterns and continuities over time can be performed in various ways depending on a number of factors of both technical and theoretical nature. For instance, standard LDA modelling tools such as MALLET or Gensim do not provide this functionality; sometimes, the nature of the data itself may not allow for meaningful historicisations (e.g., many time gaps in the collection); moreover, the way time is understood by the researcher (either as continuous or discrete) will determine the way the topics can be historicised. Thus, depending on these determining factors, there are different strategies to perform and visualise this step which necessarily require the critical intervention of the researcher.

## 9.1 Time is continuous (there are no gaps in my data)
In this case, lines would be a good way for identifying spikes in discourse and for depicting the relationship between the various discourses in a corpus. The lines visualise the average topic weight aggregated over time, that is it is computed by adding all of the weights for a given topic in a time period and dividing by the total number of documents in that time period. The avearge so calculated will likely show sharp peaks and falls and could be recommended for instance in the case of research questions aiming to identify specific sudden changes in a type of discourse. 

In the case of timeseries data, or data that is produced on regular intervals, the method of a rolling mean is typically used for capturing the general trend of a topic over time. If on the one hand this technique is very helpful for finding a time trend, on the other it flattens the topics' evolution to a smooth, possibly artificial, trend. So once again, the choice of one calculation over another depends on the dataset and the research question. As a rule of thumb, if the research enquiry relates to the long-term trend of a topic, then the rolling mean serves the purpose. If the research question is about a type of discourse at a particular point in time or over shorter periods, then computing the average would be recommended.

## 9.2 Time is discrete (there are gaps in my data)
Like in the case of time as continuous, if there are gaps in the dataset or time is conceived as discrete, the aggregation over time should be computed by calculating the average topic weight aggregated over time. The difference with the previous approach concerns the way the averages are displayed which could for instance be done by choosing to use a bar chart instead of lines. This would still show peaks and discontinuities in the topics' trends while encouraging to think of time as discrete. For the same reason, the rolling mean would not be recommended.

## 10. Conclusions
## 11. Remarks
## 12. License
## 13. Links
## 14. References
## 15. The team
## 16. How to cite
To cite the repository, please use the following format according to the APA style guide:

Viola, Lorella and de Crouy-Chanel, Mariella. 2020. *Topic Modelling with Gensim. A workflow for the Humanities* (v. 1.0.0). University of Luxembourg. https://github.com/DHARPA-Project/TopicModelling-
