import os
import generate_feature_vector as gf
import docxTOtxt as dt
import readFromTranscription as rt

path = '/Users/ankit/Documents/SSPA Project/CSV Files/Bipolar Disorder_scene2/'

files = os.listdir(path)


def text_maker(filepath):
    files = os.listdir(path)
    for f in files:
        temp = path + f
        dt.process(temp)


def csv_maker(filepath):
    files = os.listdir(filepath)
    for f in files:
        temp = path + f
        rt.remote(temp)


def json_maker(filepath, label):

    files = os.listdir(filepath)
    for f in files:
        temp = path + f
        try:
            gf.makeJSON(temp, label)
        except ZeroDivisionError:
            print(f)
    

