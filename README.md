# Topic Modelling with Python - A workflow for the Humanities

As digitally available textual repositories are becoming larger and larger, the relevance of distant reading for the humanities has grown exponentially. Traditional close reading methods are no longer sufficient to analyse such unprecedented mass of digital data, therefore humanities scholars are confronted more and more with the challenge of having to apply quantitative approaches in their research. One such quantitative approach is Topic Modelling (TM), a computational, statistical method to discover patterns and topics in large collections of unstructured text. With this repository, the [**DHARPA Project**](dharpa-project.github.io) (Digital History Advanced Research Projects Accelerator) aims to offer a step-by-step guide to a comprehensive and generalizable TM workflow that could be applied transversely across different datasets. The intention is to make the TM technique more transparent and accessible for humanities scholars, assisting them in taking up an active role in the digital analysis process and claiming ownership of their interventions. This workflow is partially based on [Viola and Verheul](https://academic.oup.com/dsh/advance-article/doi/10.1093/llc/fqz068/5601610) (2019).

## Table of contents

1. [The DHARPA Project](#1-the-dharpa-project)
2. [Topic Modelling](#2-topic-modelling)

   2.1 [What is a topic?](#21-what-is-a-topic)
   
   2.2 [When should I use it?](#22-when-should-i-use-it)
  
3. [Getting started](#3-getting-started)
4. [Installation](#4-installation)
5. [A critical approach to preparing the data](#5-a-critical-approach-to-preparing-the-data)
6. [Preparing the data for Gensim](#6-preparing-the-data-for-Gensim)
7. [Determining the number of topics](#7-determining-the-number-of-topics)
8. [Running topic modelling](#8-running-topic-modelling)
9. [Categorising the topics](#9-categorising-the-topics)
10. [Historicise the topics](#10-historicise-the-topics)
11. [Visualise the topics](#11-visualise-the-topics)
12. [Remarks](#remarks)
13. [License](#license)
14. [Links](#links)
15. [References](#references)
16. [The team](#the-team)
17. [How to cite](#how-to-cite)

## 1. The DHARPA Project
While the ‘digital humanities moment’ has yielded great accomplishments and enthusiastic interdisciplinary cooperations across the humanities and between the humanities and the sciences, concerns have been raised about the little transparency in digital practices as well as the difficulty of replicating studies due to the lack of data access or standardised practices as well as unclear methodological processes (Faull et al 2016; Jakacki et al 2016, 2015; O’ Sullivan 2019). Such concerns have for instance led scholars to claim that digital humanities is still in “search of a methodology” (Dobson 2019) and the metaphor of the 'black box' has started to be used (Smith 2014) to describe the apparent loss of human agency in the digital reseach process. This could be to some extent due to the fact that traditional historical inquiry itself has in some ways been like a “Mechanical Turk,” with the decisions and interventions made by the researcher hidden from view and only the well-oiled and seemingly autonomous product on display. The DHARPA Project aims to reverse this trend. We want to encourage historians and digital humanities scholars to lift the lid, to show how the application of their expertise works in tandem with technology to produce knowledge, how even digitally enabled research is not a product but a process, reliant on the critical engagement of the scholar. In this workflow, we aim to promote a self-reflective analysis of the interaction of technology and humanities practice and we use TM as a case study.   

## 2. Topic Modelling
Before talking about TM and how it works, it is worth spending a few words on what is intended by *topic*. This will also help to clarify how the TM algorithm works, when researchers could consider apply it to their data and how they should understand the output.

## 2.1 What is a topic?
A topic is understood as a set of terms that occur together in a statistically significant way to form a cluster of words. According to this logic, a text can be understood as the combination of such clusters of words, where each cluster is made of words mathematically likely to appear together (Steyvers and Griffiths 2007). The model assumes that a corpus has a fixed number of founding topics and that these topics compose each document of the corpus to varying degrees (Lee 2019). Using contextual information, topic models distinguish when words are used with multiple meanings in different contexts; this ultimately means that the words are also clustered according to similar uses. What happens in practice is that TM runs statistical calculations multiple times until it determines the most likely distribution of words into clusters, i.e. into topics. The procedure guarantees impartial results in terms of which words will appear in each topic, as the topics emerge from the algorithm’s identification of patterns and trends in the texts, rather than the potentially subjective interpretation of the semantic meaning of the words in each document. In this sense, there is no intervention from the researcher. 

## 2.2 When should I use it?
This analytical tool works the best with large collections of unstructured text (i.e., without any machine-readable annotations) and when the main purpose is to obtain a general overview of the topics discussed in the corpus. As long as it is unstructured, the corpus can be just about anything (e.g., emails, newspapers' headlines, newspapers' articles, a standard .txt document). For this, TM is an excellent distant reading tool that may be used as a data exploration technique, for instance to quickly categorise documents within a collection without having to read them all. A practical example of its use may be libraries that need to label digital collections for archiving purposes. Its potential, however, is most fully reached when working in tandem with expert knowledge. To help clarify the application of TM and show how it works in practice, in this workflow we will apply TM to answer a real research question. As daset, we will use *ChroniclItaly 3.0* (Viola 2020), a collection of Italian immigrant newspapers published in the United States between 1898 and 1930.

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
This step is concerned with tokenization, lowercasing, stemming, lemmatization, removing stopwords and words with less than three characters, removing noise (e.g., numbers, punctuation marks, special characters). In principle, the step is optional as the train-topic command will work on whichever version of the dataset is used. In reality, pre-processing the data is key to the analysis for several reasons. First and foremost, it will likely make the TM results more reliable and more interpretable. For instance, running TM on languages that are rich in articles, pronouns, prepositions, etc., will almost certainly result in poorly interpretable topics. Second, pre-processing the data will remove most OCR mistakes which are always present in digital textual collections to various degrees. This is especially true for corpora such as historical datasets, repositories of underdocumented languages, or digitised archives from handwritten texts. Third, it will reduce the size of the collection thus decreasing the required processing power. Fourth, it is *de facto* a data exploration step which will allow the researcher to look more closely at their data.

Deciding which of the pre-processing operations should be performed depends on many factors such as the language of the dataset, the type of data, the individual research questions. It is therefore paramount that this step is tackled **critically** by the researcher as each one of their interventions will have consequences on how the TM algorithm will process the data and therefore on the results. Here's a short explanation of each operation:
- **Tokenization**: Split the text into sentences and the sentences into words. In other words, this operation establishes the word boundaries (i.e., tokens) a very helpful way of finding patterns. It is also the typical step prior to stemming and lemmatization; 
- **Lowercasing**: Lowercase the words. This operation is a double-edged sword. It can be effective at yielding potentially better results in the case of relatively small datasets or datatsets with a high percentage of OCR mistakes. For instance, if lowercasing is not performed, the algorithm will treat *USA*, *Usa*, *usa*, *UsA*, *uSA*, etc. as distinct tokens, even though they may all refer to the same entity. On the other hand, if the dataset does not contain such OCR mistakes, then it may become difficult to distinguish between homonyms which will make interpreting the topics much harder;
- **Stemming/Lemmatization**: Reduce inflection in words (e.g. states --> state). Although similar, stemming should not be confused with lemmatization. While the latter reduces the inflected word to the actual root form (e.g., better --> good), the former outputs a canonical form of the original word (e.g., past and future tense --> present tense), and not the grammatical root. Performing or not either of these operations is very much dependant on the dataset's language as in terms of TM, they may not affect the output *per se*;
- **Removing stopwords and words with less than three characters**: Remove low information words. These are typically words such as articles, pronouns, prepositions, conjunctions, etc. which are not semantically salient. There are numerous stopword lists available for many, though not all, languages which can be easily adapted to the individual researcher's needs. Removing words with less than three characters may additionally remove many OCR mistakes. Both these operations have the dual advantage of yielding more reliable results while reducing the size of the dataset, thus in turn reducing the required processing power. This step can therefore hardly be considered optional in TM;
- **Noise removal**: Remove elements such as punctuation marks, special characters, numbers, html formatting, etc. This operation is again concerned with removing elements that may not be relevant to the text analysis and in fact interfere with it. Depending on the dataset and research question, this operation can become essential.

Each one of these interventions will need to be quantitatively and qualitatively tested and assed by the researcher every time before deciding which ones to actually perform. This is of course true not just for TM, but in general for all NLP tasks. It is important to remember that each one of these steps is an additional layer of text manipualation and has direct, heavy consequences on the data and therefore on the results. It is critical that researchers assess carefully to what degree they want to intervene on their data. For this reason, this part of the digital analysis should not be considered as separate from the analysis of the results or from the results themselves. On the contrary, it is an **integral part** of the entire digital research process. 

## 6. Preparing the data for Gensim
This step is concerned with transforming the textual data in a format that will serve as an input for training the LDA model. What happens in practice is that the documents in the collection are converted into a vector representation called Bag of Words (BOW). A BOW is a way to represent the occurrence of words within a document without considering any structural information (e.g., grammar) other than whether known words occur or not in the documents. The intuition behind the BOW model is based on the semantic theory of language usage (Harris, 1954: 156) according to which words that are used and occur in the same contexts tend to purport similar meanings. If the meaning of a word can be inferred by its context, the opposite is true as well; words found in different contexts tend to purport different meanings.

A BOW model involves two things: **1) a vocabulary of known words** and **2) a measure of the presence of such known words**. How to design the vocabulary of known words (i.e., tokens) and how to measure their presence (e.g., frequency, inverse of document frequency) ultimately determines the complexity of the model.  



