import altair as alt
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

'''
sample code to vizualize data

from vega_datasets import data

url = data.cars.url

alt.renderers.enable('altair_viewer')

chart = alt.Chart(url).mark_point().encode(
    x='feature:Q',
    y='unique:Q'
)

chart.show()
'''

path_scene_2 = '/Users/ankit/Documents/SSPA Project/Data_Building_Codes/all_features_300_scene_2.csv'

data = pd.read_csv(path_scene_2)


#method to get a certain feature for a grouped labels
#takes in feature name & returns 3 vectors per group

def get_X_Y(feature):
    X_BPD = data.groupby('label').get_group(2)[feature]
    X_Schizo = data.groupby('label').get_group(1)[feature]
    X_HC = data.groupby('label').get_group(0)[feature]

    return list(X_BPD), list(X_Schizo), list(X_HC)


def example_violin():
        # Configure the options common to all layers
    #change the X using find and replace (cmd+R) in PyCharm
    chart = alt.Chart(data).transform_density(
    'unique',
    as_=['unique', 'density'],
    extent=[25, 55],
    groupby=['label']
).mark_area(orient='horizontal').encode(
    y='unique:Q',
    color='label:N',
    x=alt.X(
        'density:Q',
        stack='center',
        impute=None,
        title=None,
        axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
    ),
    column=alt.Column(
        'label:N',
        header=alt.Header(
            titleOrient='bottom',
            labelOrient='bottom',
            labelPadding=0,
        ),
    )
).properties(
    width=100
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)
    return chart



def example_scater_matrix():
    source = data
    chart = alt.Chart(source).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='label:N'
).properties(
    width=150,
    height=150
).repeat(
    row=['positive_score', 'negative_score', 'subjective_score'],
    column=['positive_score', 'negative_score', 'subjective_score']
).interactive()
    return chart


#this method takes in the name of a feature like 'positive score' and 'negative score'
# BPD HC = 20
# BPD Schizo = 21
# Schizo HC = 10
#method takes in a code comprised of two numbers N_1 is code for label 1 and N_2 for label 2 - see above
# returns the vectors of feature A and B for N_1 and feature A and B for N_2
#so if code is 20 or 02 i.e. you want to find the difference between BPD and HC people for let's assume positive and negative scores
#you enter differences('positive_score', 'negative_score', '02')
#the method returns vectors of (pos_score - neg_score for BPD) and (pos_score - neg_score for HC)
#hypothetically BPD should have a higher differences than let's say HC - a scatter plot can showcase this


def differences(featureA, featureB, diff_code):
    fA_bpd, fA_schizo, fA_hc = get_X_Y(featureA)
    fB_bpd, fB_schizo, fB_hc = get_X_Y(featureB)
    if diff_code == '20' or diff_code == '02':
        diff_group_1 = [abs(fA_bpd[i] - fB_bpd[i]) for i in range(0, len(fA_bpd))]
        diff_group_2 = [abs(fA_hc[i] - fB_hc[i]) for i in range(0, len(fA_hc))]
    elif diff_code == '21' or diff_code == '12':
        diff_group_1 = [abs(fA_bpd[i] - fB_bpd[i]) for i in range(0, len(fA_bpd))]
        diff_group_2 = [abs(fA_schizo[i] - fB_schizo[i]) for i in range(0, len(fA_schizo))]
    elif diff_code == '10' or diff_code == '01':
        diff_group_1 = [abs(fA_hc[i] - fB_hc[i]) for i in range(0, len(fA_hc))]
        diff_group_2 = [abs(fA_schizo[i] - fB_schizo[i]) for i in range(0, len(fA_schizo))]
    else:
        return 0
    return diff_group_1, diff_group_2


def correlation_matrix_plot(features_you_want):
    data_bpd = {}
    data_schizo = {}
    data_hc = {}
    for each_f in features_you_want:
        temp_B, temp_S, temp_H = get_X_Y(each_f)
        data_bpd = {
            each_f:temp_B
        }
        data_schizo = {
            each_f:temp_S
        }
        data_hc = {
            each_f: temp_H
        }
    df_bpd = pd.DataFrame(data_bpd, columns=list(data_bpd.keys()))
    df_schizo = pd.DataFrame(data_schizo, columns=list(data_schizo.keys()))
    df_health = pd.DataFrame(data_hc, columns=list(data_hc.keys()))
    
