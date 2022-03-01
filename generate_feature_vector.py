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


#function takes in two time strings and returns second - first as seconds
def timeDifference(t1,t2):
    format = '%H:%M:%S'
    return (datetime.strptime(t2, format) - datetime.strptime(t2, format)).total_seconds()



