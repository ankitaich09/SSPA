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

def read_file_fron_path(filepath):
    with open(filepath) as fp:
        data = fp.readlines()

    return data

#for each string we need to remove \n from the end before sorting

def pre_process(data):
    times = []
    patients = ['']
    interviewers = []
    blank_output = []
    #only to be used as a comparitive tool
    timestamp_pattern = re.compile('^\+.+\+$')
    patient_pattern = re.compile('^Patient:.+$')
    interviewer_patten = re.compile('^Interviewer:.+$')
    for each_point in data:
        if not (timestamp_pattern.findall(each_point) == blank_output):
            times.append(timestamp_pattern.findall(each_point)[0][3:12])
        if not(patient_pattern.findall(each_point) == blank_output):
            patients.append(patient_pattern.findall(each_point)[0][8:])
        if not(interviewer_patten.findall(each_point) == blank_output):
            interviewers.append(interviewer_patten.findall(each_point)[0][12:])


    print(len(times))
    print(len(patients))
    print(len(interviewers))

    dataframe = pd.DataFrame(
        {
            'timestamp': times,
            'patient_dialogue': patients,
            'interviewer_dialogue': interviewers
        }
    )
    return dataframe

def namemaker(filepath):
    pos1 = filepath.rfind('/')
    pos2 = filepath.rfind('.')
    return filepath[pos1+1:pos2]+'.csv'


def main():
    filepath = '/Users/ankit/Documents/SSPA Project/output_UCSD_IA_3011.txt'
    name = namemaker(filepath)
    data = read_file_fron_path(filepath)
    frame = pre_process(data)
    frame.to_csv(name)
    print(frame)


if __name__ == '__main__':
    main()
