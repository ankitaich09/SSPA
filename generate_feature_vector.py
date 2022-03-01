'''

Take a csv dialogue file - create two feature vector files -

Naming conventions - <patient/interviewer>_feature_vector_of_<original filename>.csv

features can be stored in a file specific folder for analysis - ngram vis + sentiment + emolex scores

calculate pauses
'''

import re
import numpy as np
import pandas as pd
from datetime import datetime
import extract_linguistic_features as lf
import pickle


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


def generateVector(data):
    #this function takes in the pandas series of a scene
    #extracts ngrams, emolex features, max time spoken, average time per dialogue
    patient_dialogue = list(data['patient_dialogue'])
    unigrams = list(lf.getWords(patient_dialogue, limit=1))
    bigrams = list(lf.getWords(patient_dialogue, limit=2))
    trigrams = list(lf.getWords(patient_dialogue, limit=3))
    #here we make one string so we can do things like find average sentiment, keywords, emolex etc
    all_dialogues_as_string = ''.join(patient_dialogue)
    positive, negative, subjective = lf.extract_avg_sentiment(all_dialogues_as_string)
    top_emotions, all_emotions, scores = lf.return_emolex(all_dialogues_as_string)
    max, mean = maxTime(data)
    write_dict = {
        'list_of_unigrams' : unigrams,
        'list_of_bigrams' : bigrams,
        'list_of_trigrams': trigrams,
        'max_time' : max,
        'mean_time' : mean,
        'positive_score' : positive,
        'negative_score' : negative,
        'subjective_score' : subjective,
        'top_emotions': top_emotions,
        'emotion_scores': scores
    }

    return write_dict

def process(filepath):


    pos2 = filepath.rfind('.')
    pos1 = filepath.rfind('/')
    name = 'PICKLE_'+filepath[pos1+1:pos2]
    return name

def makePickle(filepath_to_initial_file):
    data = pd.read_csv(filepath_to_initial_file)
    output = generateVector(data)
    name = process(filepath_to_initial_file)
    pickle_open = open(name+'.pickle', 'wb')
    pickle.dump(output, pickle_open)
    pickle_open.close()

def main():
    filepath = input('Enter the path to the CSV file: ')
    makePickle(filepath)

if __name__ == '__main__':
    main()
