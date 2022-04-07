import pandas as pd

def make_one_hot(label):
    vec = []
    if label == 0:
        vec = [1,0,0]
    elif label == 1:
        vec = [0,1,0]
    elif label == 2:
        vec = [0,0,1]

    return vec


def reformat_data(path_to_data):
    data = pd.read_csv(path_to_data)
