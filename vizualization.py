import altair as alt
import pandas as pd


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

    return X_BPD, X_Schizo, X_HC


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
    row=['WPS', 'Linguistic', 'Clout'],
    column=['Clout', 'Linguistic', 'WPS']
).interactive()
    return chart
