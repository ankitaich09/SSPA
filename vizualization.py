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


def example_violin(feature):
        # Configure the options common to all layers
    #change the X using find and replace (cmd+R) in PyCharm
    chart = alt.Chart(data).transform_density(
    'feature',
    as_=['feature', 'density'],
    extent=[5, 50],
    groupby=['label']
).mark_area(orient='horizontal').encode(
    y='feature:Q',
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
