import nltk
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn
import numpy as np

#nltk.download("sentiwordnet")
#nltk.download("stopwords")
nltk.download('averaged_perceptron_tagger')

flatten = lambda l: [item for sublist in l for item in sublist]
english_stopwords = set(stopwords.words("english"))

nltk_to_sentiwordnet = {
    "NN": "n",
    "VB": "v",
    "JJ": "a",
    "RB": "r",
}

def get_sentiment(article):

    sentences = nltk.sent_tokenize(article)
    sentence_words = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentence_words = flatten(nltk.pos_tag_sents(sentence_words))

    # Filter stopwords
    tagged_sentence_words = [word for word in tagged_sentence_words if word[1] not in english_stopwords]

    pos_scores = []
    neg_scores = []
    subj_scores = []

    for word, pos in tagged_sentence_words:

        swn_pos = nltk_to_sentiwordnet.get(pos[:2], None)

        if swn_pos == None:
            continue

        synsets = list(swn.senti_synsets(word.lower(), pos=swn_pos))

        if len(synsets) == 0:
            continue

        #print("{}:".format(word))
        for synset in synsets[:1]:
            pos_scores.append(synset.pos_score())
            neg_scores.append(synset.neg_score())
            subj_scores.append(1 - synset.obj_score())

    return np.average(pos_scores, weights=subj_scores) , np.average(neg_scores, weights=subj_scores), np.mean(subj_scores)
