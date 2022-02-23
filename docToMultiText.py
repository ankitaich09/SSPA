#In this file we're trying to split a large document into multiple text files.
'''

Our approach is to break the initial file into one big text file. To read this text file into one large array, and then break that into subarrays, using groupings and regex.

'''

import docx2txt
import re
from itertools import groupby

def process(filepath):

    text = docx2txt.process(filepath)
    pos2 = filepath.rfind('.')
    pos1 = filepath.rfind('/')
    name = 'output_'+filepath[pos1+1:pos2]+'.txt'
    with open(name, 'w') as tf:
        print(text, file=tf)

def is_Break_Point(data_point):
    #We're matching the string File Identifier to identify points. We're also allowing any number of preceding characters before File Idenfitier bc there're inconsistencies.
    breaking_pattern = re.compile('^.*File Identifier.+$')
    if breaking_pattern.findall(str(data_point)):
        return True
    return False


def pre_process(data):

    data_to_be_used = []

    #only to be used as a comparitive tool
    timestamp_pattern = re.compile('^\+.+\+$')
    patient_pattern = re.compile('^Patient:.+$')
    interviewer_patten = re.compile('^Interviewer:.+$')
    file_pattern = re.compile('^.*File Identifier.+$')
    #we need to figure out number of timestamps before the patient speaks
    #that many blank spaces need to be appended before this loop runs

    for each_point in data:
        if (timestamp_pattern.findall(each_point)):
            data_to_be_used.append(each_point.rstrip())
        elif (file_pattern.findall(each_point)):
            data_to_be_used.append((each_point.rstrip()))
        elif (patient_pattern.findall(each_point)):
            data_to_be_used.append(each_point.rstrip())
        elif (interviewer_patten.findall(each_point)):
            data_to_be_used.append((each_point.rstrip()))


    #we need to figure out number of timestamps before the patient speaks
    #that many blank spaces need to be appended before this loop runs
    #data to be used now consists solely of these three kinds of things
    return data_to_be_used


def return_a_list_of_file_indetifiers(initial_file_path):
    files = []
    file_ids = []
    with open(initial_file_path) as fp:
        data = fp.readlines()
    processed_data = pre_process(data)
    file_ids = [list(group) for k, group in groupby(processed_data, lambda x: is_Break_Point(x) == True) if k]
    files = [list(group) for k, group in groupby(processed_data, lambda x: is_Break_Point(x) == False) if k]
    for i in range(len(files)):
        temp = file_ids[i] + files[i]
        with open(str(file_ids[i])+'.txt','w') as tfp:
            for element in temp:
                tfp.write(element+'\n')
        temp=[]




