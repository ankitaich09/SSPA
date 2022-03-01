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

    #start point now holds the start of patient dialogue
