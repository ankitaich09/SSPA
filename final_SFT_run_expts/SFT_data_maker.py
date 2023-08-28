import pandas as pd
import os
import copy
import re


#func to read and return dataframe from csv file
def get_data_from_file(filename):
    return pd.read_csv(filename)


#func to return list of files in a folder
def get_list_of_files(dirname):
    return os.listdir(dirname)


#func to open SSPA file
def open_sspa_file(filepath):
    return pd.read_csv(filepath)

#func to get SSPA scores given a patient ID
def get_sspa_values(data, pat_ID):

    filter = data['ID'] == pat_ID
    copy_df = data.where(filter).dropna()
    score_dict = {

        'Interest':copy_df['SSPA1_1'].to_string(index=False, header=False),
        'Fluency':copy_df['SSPA1_2'].to_string(index=False, header=False),
        'Clarity':copy_df['SSPA1_3'].to_string(index=False, header=False),
        'Focus':copy_df['SSPA1_4'].to_string(index=False, header=False),
        'Affect':copy_df['SSPA1_5'].to_string(index=False, header=False),
        'Overall':copy_df['SSPA1_6'].to_string(index=False, header=False),
        'Grooming':copy_df['SSPA1_7'].to_string(index=False, header=False),
        'Social Apt':copy_df['SSPA1_8'].to_string(index=False, header=False)

    }
    return score_dict


#func to take all the text from the data frame and process it as one text
#this would serve as input to our SFT LLM - P+I ==> SSPA score sequence
def process_as_one(filename):
    regex = "\d{4}"
    patID = re.findall(regex, filename)[0]
    df = pd.read_csv(filename)
    pat_dialogues = list(df['patient_dialogue'])
    int_dialogues = list(df['interviewer_dialogue'])

    temp = ''
    for i in range(len(pat_dialogues)):
        temp += pat_dialogues[i] + int_dialogues[i]

    



#test case

process_as_one('/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/Complete transcript CSVs/HC_SC_1/outputUTD_SCOPE_1225_Scene 1.csv')