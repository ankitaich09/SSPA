import json
import numpy as np
import matplotlib.pyplot as plt

'''

IN THIS CODE WE'RE TRYING TO SEE IF THE FEATURES WE'RE EXTRACTING MAKES LEGITIMATE SENSE IN TERMS OF MACHINE LEARNING MODELS.
SO FAR THE FEATURES WE HAVE CAN BE CLASSIFIED AS FEATURES OF SENTIMENT, FEATURES OF UTTERANCE, FEATURES OF LEXICAL RICHNESS, AND NON NUMERIC FEATURES.
WE NEED TO VISUALIZE THE CORRELATION AND CHANGE IN THESE FEATURES TO EITHER PRIOITIZE BRINGING IN MORE FEATURES FIRST, OR BRINGING IN MORE DATA FIRST.

'''


def read_file(filepath):
    with open (filepath) as fp:
        data = json.load(fp)
    return data

def get_lexical_features(data):
    return data['lexical_features']

def get_utterance_features(data):
    return data['utterance_features']

def get_sentiment_scores(data):
    return data['Feature_set_1']

def compare_time_features(data_1, data_2):
    d1_senti_scores = get_sentiment_scores(data_1)
    d2_senti_scores = get_sentiment_scores(data_2)

    #calculating mean times, and max times

    max_1 = d1_senti_scores['max_time']
    max_2 = d2_senti_scores['max_time']

    mean_1 = d1_senti_scores['mean_time']
    mean_2 = d2_senti_scores['mean_time']

    return max_1, max_2, mean_1, mean_2


def return_list_of_files():
    list_of_healthy = ['/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1233_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1285_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1297_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1323_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1324_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1452_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1455_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1675_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1679_Scene 1.json',
                       '/Users/ankit/Documents/SSPA Project/JSON/healthy control_scene1/JSON_outputUTD_IA_1682_Scene 1.json']

    list_of_schizophrenic = [
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1002_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1027_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1039_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1056_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1060_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1071_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1107_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1154_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1168_Scene 1.json',
        '/Users/ankit/Documents/SSPA Project/JSON/Schizophrenia_Scene1/JSON_outputUTD_IA_1219_Scene 1.json'
    ]
    return list_of_healthy, list_of_schizophrenic

def populate_list_of_time():

    list_of_healthy, list_of_schizophrenic = return_list_of_files()
    healthy_max_times = []
    healthy_mean_times = []
    schizo_max_times = []
    schizo_mean_times = []

    for i in range(0,len(list_of_healthy)):
        data_1 = read_file(list_of_healthy[i])
        data_2 = read_file(list_of_schizophrenic[i])
        #m = max me = mean
        m1,m2,me1,me2 = compare_time_features(data_1, data_2)
        healthy_max_times.append(m1)
        healthy_mean_times.append(me1)
        schizo_max_times.append(m2)
        schizo_mean_times.append(me2)

    print(healthy_mean_times)
    print(schizo_mean_times)

    print('---------------MAX----------------------')

    print(healthy_max_times)
    print(schizo_max_times)

    return healthy_max_times, healthy_mean_times, schizo_max_times, schizo_mean_times


def populate_list_of_sentiments():

    healthy, schizo = return_list_of_files()

    pos_scores_h = []
    neg_scores_h = []

    pos_scores_d = []
    neg_scores_d = []

    for i in range(0, len(healthy)):
        data_1 =  read_file(healthy[i])
        data_2 = read_file(schizo[i])
        pos_scores_h.append(data_1['Feature_set_1']['positive_score'])
        neg_scores_h.append(data_1['Feature_set_1']['negative_score'])
        pos_scores_d.append(data_2['Feature_set_1']['positive_score'])
        neg_scores_d.append(data_2['Feature_set_1']['negative_score'])


    plt.figure()
    #-go signifies connect points with lines '-' which are green 'g' and have dots at points 'o'
    plt.plot(pos_scores_h, '-go', pos_scores_d, '-ro')
    plt.xlabel('Participant Number')
    plt.ylabel('Positive Scores')
    plt.title('Comparing positive sentiment scores in healthy and schizophrenic')
    plt.legend(['Healthy', 'Schizophrenic'], loc='upper left')
    plt.show()


    plt.figure()
    #-go signifies connect points with lines '-' which are green 'g' and have dots at points 'o'
    plt.plot(neg_scores_h, '-go', neg_scores_d, '-ro')
    plt.xlabel('Participant Number')
    plt.ylabel('Negative Scores')
    plt.title('Comparing negative sentiment scores in healthy and schizophrenic')
    plt.legend(['Healthy', 'Schizophrenic'], loc='upper left')
    plt.show()





def visualize_lexical_features():


    healthy, schizo = return_list_of_files()

    div_scores_h = []
    her_scores_h = []

    div_scores_d = []
    her_scores_d = []

    for i in range(0, len(healthy)):
        data_1 =  read_file(healthy[i])
        data_2 = read_file(schizo[i])
        div_scores_h.append(data_1['lexical_features']['diversity'])
        her_scores_h.append(data_1['lexical_features']['herdan'])
        div_scores_d.append(data_2['lexical_features']['diversity'])
        her_scores_d.append(data_2['lexical_features']['herdan'])


    plt.figure()
    #-go signifies connect points with lines '-' which are green 'g' and have dots at points 'o'
    plt.plot(div_scores_h, '-go', div_scores_d, '-ro')
    plt.xlabel('Participant Number')
    plt.ylabel('Diversity Scores')
    plt.title('Comparing linguistic diversity scores in healthy and schizophrenic')
    plt.legend(['Healthy', 'Schizophrenic'], loc='upper left')
    plt.show()


    plt.figure()
    #-go signifies connect points with lines '-' which are green 'g' and have dots at points 'o'
    plt.plot(her_scores_h, '-go', her_scores_d, '-ro')
    plt.xlabel('Participant Number')
    plt.ylabel('Herdan Scores')
    plt.title('Comparing Herdan\'s Lexical Richness scores in healthy and schizophrenic')
    plt.legend(['Healthy', 'Schizophrenic'], loc='upper left')
    plt.show()


def visualize(h,d, comparison='mean time'):
    ylab = comparison + ' spent'
    title = 'comparing ' + comparison + ' by healthy vs diseased person'
    # H or D signifies healthy or diseased - max and mean signify names
    plt.figure()
    #-go signifies connect points with lines '-' which are green 'g' and have dots at points 'o'
    plt.plot(h, '-go', d, '-ro')
    plt.xlabel('Participant Number')
    plt.ylabel(ylab)
    plt.title(title)
    plt.legend(['Healthy', 'Schizophrenic'], loc='upper left')
    plt.show()


