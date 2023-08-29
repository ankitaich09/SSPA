import pandas as pd
from sklearn.metrics import mean_squared_error
import math

def load_data(filepath):
    return pd.read_csv(filepath)

data = load_data('/Users/ankitaich/Documents/Final Disseration Experiments/Inference Results/healthy_scene_1_inference.csv')

def get_predicted_scores_as_dict(string):
    interest = string.split('Interest: ')[-1].split(' ')[0]
    fluency = string.split('Fluency: ')[-1].split(' ')[0]
    clarity = string.split('Clarity: ')[-1].split(' ')[0]
    focus = string.split('Focus: ')[-1].split(' ')[0]
    social = string.split('Social Apt: ')[-1].strip()

    scores = {

        'Interest': interest,
        'Fluency': fluency,
        'Clarity': clarity,
        'Focus': focus,
        'Social Apt': social
    }

    return scores

def get_gold_scores_as_dict(string):
    interest = string.split('Interest: ')[-1].split('\n')[0]
    fluency = string.split('Fluency: ')[-1].split('\n')[0]
    clarity = string.split('Clarity: ')[-1].split('\n')[0]
    focus = string.split('Focus: ')[-1].split('\n')[0]
    social = string.split('Social Apt: ')[-1].strip()

    scores = {

        'Interest': interest,
        'Fluency': fluency,
        'Clarity': clarity,
        'Focus': focus,
        'Social Apt': social
    }

    return scores

def get_score_set_from_index(index, variable):

    predicted = (get_predicted_scores_as_dict(data['PREDICTED'][index]))
    gold = (get_gold_scores_as_dict(data['GOLD'][index]))
    try:
        return float(predicted[variable]), float(gold[variable])
    except:
        return 0, float(gold[variable])

def get_distributions():
    sspa = ['Interest', 'Fluency', 'Clarity', 'Focus', 'Social Apt']
    interest = {'GOLD':[],'PREDICTED':[]}
    focus = {'GOLD': [], 'PREDICTED': []}
    fluency = {'GOLD': [], 'PREDICTED': []}
    clarity = {'GOLD': [], 'PREDICTED': []}
    social = {'GOLD': [], 'PREDICTED': []}
    for k in range(0, 18):
        pred, gold = get_score_set_from_index(k, 'Interest')
        interest['GOLD'].append(gold)
        interest['PREDICTED'].append(pred)

    for k in range(0, 18):
        pred, gold = get_score_set_from_index(k, 'Focus')
        focus['GOLD'].append(gold)
        focus['PREDICTED'].append(pred)

    for k in range(0, 18):
        pred, gold = get_score_set_from_index(k, 'Clarity')
        clarity['GOLD'].append(gold)
        clarity['PREDICTED'].append(pred)

    for k in range(0, 18):
        pred, gold = get_score_set_from_index(k, 'Fluency')
        fluency['GOLD'].append(gold)
        fluency['PREDICTED'].append(pred)

    for k in range(0, 18):
        pred, gold = get_score_set_from_index(k, "Social Apt")
        social['GOLD'].append(gold)
        social['PREDICTED'].append(pred)

        return interest, focus, fluency, clarity, social



def get_rmse(y_actual, y_predicted):
    mse = mean_squared_error(y_actual, y_predicted, squared=False)
    rmse = math.sqrt(mse)
    return rmse

def simple_acc(gold, pred):
    c = 0
    for i in range(len(gold)):
        if gold[i] == pred[i]:
            c+=1
    return c/len(gold)