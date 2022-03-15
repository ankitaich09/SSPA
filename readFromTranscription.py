#take in a text file and convert to pandas
#we need time stamps - identified by +++ +++ signs
#dialogues
#ultimate file should look like
#time_stamp interviewer patient
#3 columns
#if one of the two did not speak it should enter blank string there

#Approach 1 - split at new line
'''
these cases can follow if we split at new line

we have a string that begins and ends in +++ - in this case we read the string between the 3rd and 4th + and trim spaces - this is timestamp

we have a string that starts with the word patient or interviewer - bucket into relevant group

we have a blank string - discard

something else - like reference number - we can store this to be used a primary key

Mass produce for all files
'''


#case 1 - time stamps - strings that follow the pattern +++ timestamp +++
#use Regular Expression - ^\+.+\+$
#^ matches start of string
#\+ matches + since + is a control sequence; .+ accepts any string >=1 ; \+ encloses between two + signs ; $ is the end of string


#case 2 - patient or interviewer - strings that follow the pattern Patient: or Interviewer:
#use RegEx - ^Patient:.+$
#use RegEx - ^Interviewer:.+$

#case 3 - Blank line - use string matching to find new line or blank line

#store into three lists - fourth list will have processed file name - to be used as primary key

import re
import pandas as pd
from itertools import groupby


def read_file_fron_path(filepath):
    with open(filepath) as fp:
        data = fp.readlines()

    return data

#for each string we need to remove \n from the end before sorting

#the function below returns an integer number, to see how many timestamps, the patient doesn't say anything at the start.
def blank_patient_counts(data):
    times = []
    i=0
    while re.compile('^Patient:.+$').findall(data[i]) == []:
        if not(re.compile('^\+.+\+$').findall(data[i])==[]):
            times.append(data[i])
        i=i+1
    return len(times)



def find_type(data_point):
    timestamp_pattern = re.compile('^\+.+\+$')
    patient_pattern = re.compile('^Patient:.+$')
    interviewer_patten = re.compile('^Interviewer:.+$')
    if timestamp_pattern.findall(str(data_point)):
        return 'T'
    elif patient_pattern.findall(str(data_point)):
        return 'P'
    else:
        return 'I'


#changing this function
'''
Earlier this function was taking each input in the file and sorting it into one of three buckets, either a timestamp, or a patient or an interviewer dialogue. however
this misses some edge cases. For instance there are times when only one person speaks. 

Now we try to return an array which is full of subarrays. Each subarray is a triad, timestamp, patient, interviewer. For the missing part it can substitute a blank.

'''
def pre_process(data):

    data_to_be_used = []

    #only to be used as a comparitive tool
    timestamp_pattern = re.compile('^\+.+\+$')
    patient_pattern = re.compile('^Patient:.+$')
    interviewer_patten = re.compile('^Interviewer:.+$')
    #we need to figure out number of timestamps before the patient speaks
    #that many blank spaces need to be appended before this loop runs

    for each_point in data:
        if (timestamp_pattern.findall(each_point)):
            data_to_be_used.append(each_point.rstrip())
        elif (patient_pattern.findall(each_point)):
            data_to_be_used.append(each_point.rstrip())
        elif (interviewer_patten.findall(each_point)):
            data_to_be_used.append((each_point.rstrip()))


    #we need to figure out number of timestamps before the patient speaks
    #that many blank spaces need to be appended before this loop runs
    #data to be used now consists solely of these three kinds of things
    return data_to_be_used

def make_subarrays(processed_data):

    timestamps = []
    dialogues = []

    timestamps = [list(group) for k, group in groupby(processed_data, lambda x: find_type(x) == 'T') if k]
    dialogues = [list(group) for k, group in groupby(processed_data, lambda x: find_type(x) == 'T') if  not k]

    for each_d in dialogues:
        if len(each_d) == 1:
            if find_type(each_d[0]) == 'P':
                each_d.append('Interviewer: ')
            else:
                each_d.append('Patient: ')

    return timestamps, dialogues

#check if the first time people speak there's no time stamp
#if so return True
def condition(time, p, t):
    if time == p and time == t:
        return False
    else:
        return True


def make_dataframe(times, dialogues):
    time = []
    p = []
    i = []
    for t in times:
        time.append(t[0][3:12])
        #Getting rid of the plus signs
    for d in dialogues:
       d.sort()
       p.append(d[1][8:])
       i.append(d[0][12:])
       #getting rid of the words Patient : and Interviewer :



    if condition(len(time),len(p),len(i)) == True:
        time.insert(0, '00:00:00')


    dataframe = pd.DataFrame(
        {
            'timestamp': time,
            'patient_dialogue': p,
            'interviewer_dialogue': i
        }
    )

    return dataframe

def namemaker(filepath):
    pos1 = filepath.rfind('/')
    pos2 = filepath.rfind('.')
    return filepath[pos1+1:pos2]+'.csv'


def remote(filepath):
    name = namemaker(filepath)
    data = read_file_fron_path(filepath)
    processed_data = pre_process(data)
    times, dialogues = make_subarrays(processed_data)
    dataframe = make_dataframe(times, dialogues)
    dataframe.to_csv(name)
    print(dataframe)


def main():
    filepath = input('Enter Text File Path ')
    name = namemaker(filepath)
    data = read_file_fron_path(filepath)
    processed_data = pre_process(data)
    times, dialogues = make_subarrays(processed_data)
    dataframe = make_dataframe(times, dialogues)
    dataframe.to_csv(name)
    print(dataframe)


if __name__ == '__main__':
    main()


#issues 1 - combine speeches beyond time stamps
