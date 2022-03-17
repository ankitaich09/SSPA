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
            #Because if there are inconsistencies in the doc file - that will flow down to the final csv file being blank - because regex won't work
            #This means JSON will incur a zero division error trying to process logarithmic and division formulae using a blank string (NULL VALUE)
            #At that point we return the value of the iterator - which has the file name in it - and helps us understand which file has inonsistencies
            print(f)


