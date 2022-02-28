'''

In this code we define methods which allow us to extract linguistic features given a string

The goal is to make it re-usable so we can use this across dataframes and datasets

extract unigrams, bigrams, trigrams

average sentiment scores from sentiwordnet (SWN)

top keywords from document;

Not removing a lot of punctuations or stopwords because transformer architecture might need them

'''

import re
import unicodedata
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import sentiment_analysis as sa
from nltk.corpus import stopwords
from rake_nltk import Rake
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

#Any stopwords in context can be added here
ADDITIONAL_STOPWORDS = []

def basic_clean(text):
  """
  A simple function to clean up the data. All the words that
  are not designated as a stop word is then lemmatized after
  encoding and basic regex parsing are performed.

  If using a lot of transformer arch - we may not use it
  """
  wnl = nltk.stem.WordNetLemmatizer()
  stopwords = nltk.corpus.stopwords.words('english') + ADDITIONAL_STOPWORDS
  text = (unicodedata.normalize('NFKD', text)
    .encode('ascii', 'ignore')
    .decode('utf-8', 'ignore')
    .lower())
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words if word not in stopwords]

#input list of words and n for ngram (uni,bi, tri) limit = number of ngrams
#returns list of ngrams


def getWords(data_object, number=1, limit=10):
  temp = basic_clean(''.join(str(data_object)))
  words = (pd.Series(nltk.ngrams(temp, number)).value_counts())[:limit]
  return words


#small visualization code for ngrams
#input words as a list of string (or document)
def visualize(words, limit):
  if limit == 1:
    c = 'red'
    s = 'unigrams'
  elif limit == 2:
    c = 'blue'
    s = 'bigrams'
  else:
    c = 'black'
    s = 'ngrams'
  plt.figure()
  series_of_words = getWords(words, limit)
  series_of_words.sort_values().plot.barh(color=c, width=.9, figsize=(12, 8))
  title = ' most frequently occuring ' + str(s)
  plt.title(title)
  plt.ylabel(s)
  plt.xlabel('# of occurences')

#inpout document as string
#output tuple with double values of average positive, negative, and subject score
def extract_avg_sentiment(document):
    return sa.get_sentiment(document)

#input document as string
#return keywords as list
def return_keywords(text):
    rake_nltk_var = Rake()
    words = rake_nltk_var.extract_keywords_from_text(text)
    keywords = rake_nltk_var.get_ranked_phrases()
    return keywords


