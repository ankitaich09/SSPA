'''

Take a csv dialogue file - create two feature vector files -

Naming conventions - <patient/interviewer>_feature_vector_of_<original filename>.csv

features can be stored in a file specific folder for analysis - ngram vis + sentiment + emolex scores

calculate pauses
'''

import re
import sys

import numpy as np
import pandas as pd
from datetime import datetime
import extract_linguistic_features as lf
import pickle
from nltk.tokenize import RegexpTokenizer
import json
from lexicalrichness import LexicalRichness
import liwc_str as ls


#function takes in two time strings and returns first - second time as seconds
def timeDifference(t1,t2):
    FMT = '%H:%M:%S'
    t1 = t1
    t2 = t2
    return (datetime.strptime(t1, FMT) - datetime.strptime(t2, FMT)).total_seconds()


#returns max time spoken by patient
def maxTime(data):
    times = []
    patient_dialogues = []
    #record start of dialogue time stamp
    #record end of dialogue timestamp
    #record difference as seconds
    #continue till patient has finished speaking
    times = list(data['timestamp'])
    patient_dialogues = list(data['patient_dialogue'])
    for i in range(len(patient_dialogues)):
        if not(patient_dialogues[i] == ' '):
            start_point = times[i]
            start_point_pos = i
            break
    #start point now holds the timestamp for the start of patient dialogue
    #run a loop from start point to end point
    #if i is in pos 0 to n-1 there exists i-1 and i+1 => if dialogue exists we store difference of i+1 and i
    #if dialogue does not exist we move until there is a dialogue
    list_of_differences_in_seconds = []
    for i in range(start_point_pos, len(patient_dialogues)):
        #if Iterator has reached end of list - then we skip this because that end time is not specified
        if i == len(patient_dialogues)-1:
            break
        else:
            #check exists condition
            if not(patient_dialogues[i] == ' '):
                #formatting errors can cause issues so we remove leading whitespace
                diff = timeDifference(times[i+1].lstrip(), times[i].lstrip())
                list_of_differences_in_seconds.append((diff))
    return sum(list_of_differences_in_seconds), np.mean(list_of_differences_in_seconds)

def lexicalFeatures(data):
    pd = data['patient_dialogue']
    text = ' '.join(pd)
    lex = LexicalRichness(text)
    ttratio = lex.ttr
    cttration = lex.cttr
    #The TTR value which a sequence of contiguous text units must maintain to constitute a 'factor'. It should be comprised between 0 and 1 exclusive. Default is 0.72.
    mtld = lex.mtld(threshold=0.72)
    herdan = lex.Herdan
    summer = lex.Summer
    dug = lex.Dugast
    mas = lex.Maas
    lexical = {
        'ttr': ttratio,
        'cttr': cttration,
        'diversity' : mtld,
        'herdan':herdan,
        'summer': summer,
        'dugast': dug,
        'maas' : mas

    }
    return lexical


#return number of utterances
#return word count
#return number of unique words
#return avg words per utterance
def utteranceFeatures(data):
    patient_dialogues = list(data['patient_dialogue'])
    #remove all blank dialogues from list
    patient_dialogues = list(filter((' ').__ne__, patient_dialogues))
    count = 0
    unique_count = 0
    num_words_per_sentence = []
    for each_lint in patient_dialogues:
        tokenizer = RegexpTokenizer(r'\w+')
        temp_list_of_words = tokenizer.tokenize(each_lint)
        count = count + len(temp_list_of_words)
        num_words_per_sentence.append(len(temp_list_of_words))
    num_utterances = len(patient_dialogues)
    unique_count = len(list(set(' '.join(patient_dialogues))))
    return num_utterances, count, unique_count, np.mean(num_words_per_sentence)



def liwcDic(data):
    patient_dialogue = list(data['patient_dialogue'])
    string_data = ' '.join(patient_dialogue)
    output_dict = ls.get_liwc_dict(string_data)
    return output_dict

def generateVector(data):
    #this function takes in the pandas series of a scene
    #extracts ngrams, emolex features, max time spoken, average time per dialogue
    patient_dialogue = list(data['patient_dialogue'])
    unigrams = dict(lf.getWords(patient_dialogue, limit=10, number=1))
    bigrams = dict(lf.getWords(patient_dialogue, limit=10, number=2))
    trigrams = dict(lf.getWords(patient_dialogue, limit=10, number=3))
    #here we make one string so we can do things like find average sentiment, keywords, emolex etc
    all_dialogues_as_string = ' '.join(patient_dialogue)
    positive, negative, subjective = lf.extract_avg_sentiment(all_dialogues_as_string)
    top_emotions, all_emotions, scores = lf.return_emolex(all_dialogues_as_string)
    max, mean = maxTime(data)
    write_dict = {
        'max_time' : max,
        'mean_time' : mean,
        'positive_score' : positive,
        'negative_score' : negative,
        'subjective_score' : subjective,
        'top_emotions': top_emotions,
        'emotion_scores': scores
    }
    num_utter, total_words, total_unique_words, avg_word_per_utter = utteranceFeatures(data)
    utterance_dict = {
        'num_utterances' : num_utter,
        'total_words' : total_words,
        'total_unique_words' : total_unique_words,
        'avg_word_per_utter' : avg_word_per_utter
    }

    return write_dict, utterance_dict, unigrams, bigrams, trigrams

def process(filepath):


    pos2 = filepath.rfind('.')
    pos1 = filepath.rfind('/')
    name = 'JSON_'+filepath[pos1+1:pos2]
    return name



def makeJSON(filepath_to_initial_data, label_of_health):
    data = pd.read_csv(filepath_to_initial_data)
    output_dict, utterance_features, unigrams, bigrams, trigrams = generateVector(data)
    lexical = lexicalFeatures(data)
    liwc = liwcDic(data)
    #fixing the ngrams bc they are procuded as tuples and digits
    #this way we make them into phrases and integers using json format
    unigrams = {k[0]:int(v) for k,v in unigrams.items()}
    bigrams = {str(' '.join(k[0:])):int(v) for k,v in bigrams.items()}
    trigrams = {str(' '.join(k[0:])):int(v) for k,v in trigrams.items()}
    json_object = {
        'label' : label_of_health,
        str('Feature_set_1'): output_dict,
        str('LIWC'): liwc,
        'lexical_features' : lexical,
        'utterance_features': utterance_features,
        'unigrams':unigrams,
        'bigrams':bigrams,
        'trigrams':trigrams
    }
    name = process(filepath_to_initial_data)+'.json'
    with open(name, 'w') as jf:
        json.dump(json_object, jf, indent=4)




def main():
    filepath = input('Enter the path to the CSV file: ')
    #CHANGE THE LABEL BEFORE YOU RUN THE CODE !!!!!!!
    label_of_health = 'bipolar'
    makeJSON(filepath, label_of_health)



if __name__ == '__main__':
    main()
