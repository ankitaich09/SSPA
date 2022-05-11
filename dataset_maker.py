

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
    if label == 'schizophrenia':
        label = 1
    elif label == 'healthy':
        label = 0
    else:
        label = 2
        #bpd


    #all features in order

    features.append(np.abs(data['Feature_set_1']['max_time']))
    features.append(np.abs(data['Feature_set_1']['mean_time']))
    features.append(data['Feature_set_1']['positive_score'])
    features.append(data['Feature_set_1']['negative_score'])
    features.append(data['Feature_set_1']['subjective_score'])

    #adding LIWC features

    try:

        headers = list(data['LIWC'].keys())



        for each_key in headers:
            #each key would be an LIWC category
            features.append(data['LIWC'][each_key]['0'])

    except KeyError:
        print('No Key in File')
        pass

    #adding emolex features
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

    #adding lexical features

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
               'negative', 'positive', 'Segment', 'WC', 'Analytic', 'Clout',
               'Authentic', 'Tone', 'WPS', 'BigWords', 'Dic', 'Linguistic', 'function', 'pronoun',
               'ppron', 'i', 'we', 'you', 'shehe', 'they', 'ipron', 'det', 'article', 'number', 'prep',
               'auxverb', 'adverb', 'conj', 'negate', 'verb', 'adj', 'quantity', 'Drives', 'affiliation',
               'achieve', 'power', 'Cognition', 'allnone', 'cogproc', 'insight', 'cause', 'discrep', 'tentat',
               'certitude', 'differ', 'memory', 'Affect', 'tone_pos', 'tone_neg', 'emotion', 'emo_pos', 'emo_neg',
               'emo_anx', 'emo_anger', 'emo_sad', 'swear', 'Social', 'socbehav', 'prosocial', 'polite',
               'conflict', 'moral', 'comm', 'socrefs', 'family', 'friend', 'female', 'male', 'Culture',
               'politic', 'ethnicity', 'tech', 'Lifestyle', 'leisure', 'home', 'work', 'money', 'relig',
               'Physical', 'health', 'illness', 'wellness', 'mental', 'substances', 'sexual', 'food', 'death',
               'need', 'want', 'acquire', 'lack', 'fulfill', 'fatigue', 'reward', 'risk', 'curiosity', 'allure',
               'Perception', 'attention', 'motion', 'space', 'visual', 'auditory', 'feeling', 'time', 'focuspast',
               'focuspresent', 'focusfuture', 'Conversation', 'netspeak', 'assent', 'nonflu', 'filler', 'AllPunc',
               'Period', 'Comma', 'QMark', 'Exclam', 'Apostro', 'OtherP',
                     'anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust',
               'ttr','cttr','diversity','herdan','summer','dugast','maas',
               'utterances', 'WC', 'unique', 'word_per_utter',
               'label']


    files1 = os.listdir(list_of_paths_to_folder[0]) #path to BPD
    files2 = os.listdir(list_of_paths_to_folder[1]) #path to Schizo
    files3 = os.listdir(list_of_paths_to_folder[2]) #path to healthy

    if '.DS_Store' in files1:
        files1.remove('.DS_Store')

    if '.DS_Store' in files2:
        files2.remove('.DS_Store')

    if '.DS_Store' in files3:
        files3.remove('.DS_Store')

    names = []
    feature_set_1 = []

    feature_set_2 = []

    feature_set_3 = []

    for each_file in files1:
        pathname = list_of_paths_to_folder[0] + str(each_file)
        print(pathname)
        names.append('BPD'+str(each_file))
        print(names)
        with open(pathname, 'r', encoding='utf-8') as jp:
            data = json.load(jp)

        features = json_to_csv(data)

        feature_set_1.append(features)

    for each_file in files2:
        pathname = list_of_paths_to_folder[1] + str(each_file)
        print(pathname)
        names.append('schizo'+str(each_file))
        with open(pathname, 'r', encoding='utf-8') as jp:
            data = json.load(jp)

        features = json_to_csv(data)

        feature_set_2.append(features)


    for each_file in files3:
        pathname = list_of_paths_to_folder[2] + str(each_file)
        print(pathname)
        names.append('HC'+str(each_file))
        with open(pathname, 'r', encoding='utf-8') as jp:
            data = json.load(jp)

        features = json_to_csv(data)

        feature_set_3.append(features)


    with open('all_features_300.csv', 'w' ) as f:
        write = csv.writer(f)

        write.writerow(headers)
        write.writerows(feature_set_1+feature_set_2+feature_set_3)


    with open('file_identifiers.txt', 'w') as fid:
        for a in names:
            fid.write(a[:a.find('J')])
            fid.write('+')
            fid.write(a[a.find('_'):a.rfind('.')])
            fid.write('\n')


