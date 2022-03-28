

#take in a list of pathnames -- which point to JSON files
#combine all json's to make dataset
#length of list (number of diseases) can be used to one-hot encode labels
#applicable for more than 2 classes.


import json, pandas as pd, numpy as np
import os, csv


def json_to_csv(data):

    #data has to be of type dict
    features = []
    label = data['label']
    if label == 'Schizophrenia':
        label = 1
    else:
        label = 0

    #all features in order

    features.append(np.abs(data['Feature_set_1']['max_time']))
    features.append(np.abs(data['Feature_set_1']['mean_time']))
    features.append(data['Feature_set_1']['positive_score'])
    features.append(data['Feature_set_1']['negative_score'])
    features.append(data['Feature_set_1']['subjective_score'])


    expected_emos = ['negative', 'positive',
                     'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']

    emos_found = list(data['Feature_set_1']['emotion_scores'].keys())

    emo_dict = []

    for each_expect in expected_emos:
        if each_expect in emos_found:
            temp = {
                each_expect : data['Feature_set_1']['emotion_scores'][each_expect]
            }
        else:
            temp = {
                each_expect : 0
            }
        emo_dict.append(temp)

    for each_emo in emo_dict:
        features.append(list(each_emo.values())[0])


    features.append(data['lexical_features']['ttr'])
    features.append(data['lexical_features']['cttr'])
    features.append(data['lexical_features']['diversity'])
    features.append(data['lexical_features']['herdan'])
    features.append(data['lexical_features']['summer'])
    features.append(data['lexical_features']['dugast'])
    features.append(data['lexical_features']['maas'])
    features.append(data['utterance_features']['num_utterances'])
    features.append(data['utterance_features']['total_words'])
    features.append(data['utterance_features']['total_unique_words'])
    features.append(data['utterance_features']['avg_word_per_utter'])


    features.append(label)

    return features


def build(list_of_paths_to_folder):
    headers = ['max_time', 'mean_time', 'positive_score', 'negative_score', 'subjective_score',
               'negative', 'positive',
                     'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust',
               'ttr','cttr','diversity','herdan','summer','dugast','maas',
               'utterances', 'WC', 'unique', 'word_per_utter',
               'label']


    files1 = os.listdir(list_of_paths_to_folder[0])
    files2 = os.listdir(list_of_paths_to_folder[1])


    if '.DS_Store' in files1:
        files1.remove('.DS_Store')

    if '.DS_Store' in files2:
        files2.remove('.DS_Store')



    feature_set_1 = []

    feature_set_2 = []

    for each_file in files1:
        pathname = list_of_paths_to_folder[0] + str(each_file)
        print(pathname)
        with open(pathname, 'r', encoding='utf-8') as jp:
            data = json.load(jp)

        features = json_to_csv(data)

        feature_set_1.append(features)

    for each_file in files2:
        pathname = list_of_paths_to_folder[1] + str(each_file)
        print(pathname)
        with open(pathname, 'r', encoding='utf-8') as jp:
            data = json.load(jp)

        features = json_to_csv(data)

        feature_set_2.append(features)



    with open('bpd_schizo.csv', 'w' ) as f:
        write = csv.writer(f)

        write.writerow(headers)
        write.writerows(feature_set_1+feature_set_2)




