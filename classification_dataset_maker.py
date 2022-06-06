#code to take two scenes of 3 classes and break them into
# 6 scenes of 2 classes
# dataset 1 - BPD vs Schizo
# D2 - BPD vs HC
# D3 - HC vs Schizo
# 3 datasets for 2 scenes
#We take both scenes (dataframes) and split them into A B C * 2 (for each condition and each scene) then we combine

import pandas as pd

scene1_path = '/Users/ankit/Documents/SSPA Project/Datasets/all_features_300_scene_1.csv'

scene2_path = '/Users/ankit/Documents/SSPA Project/Datasets/all_features_300_scene_2.csv'

df_sc1 = pd.read_csv(scene1_path)

df_sc2 = pd.read_csv(scene2_path)

#for scene 1

'''

This is similar to doing 

SELECT *
FROM df_sc1
WHERE label = 1;

in SQL 

'''

bpd = df_sc1['label'] == 2
schizo = df_sc1['label'] == 1
hc = df_sc1['label'] == 0

bpd_sc1 = df_sc1[bpd]
schizo_sc1 = df_sc1[schizo]
hc_sc1 = df_sc1[hc]

#for scene 2

bpd2 = df_sc2['label'] == 2
schizo2 = df_sc2['label'] == 1
hc2 = df_sc2['label'] == 0

bpd_sc2 = df_sc2[bpd2]
schizo_sc2 = df_sc2[schizo2]
hc_sc2 = df_sc2[hc2]

#creating the 6 datasets for classification here

sc1_bpd_schizo = pd.concat([bpd_sc1, schizo_sc1])
sc1_bpd_hc = pd.concat([bpd_sc1, hc_sc1])
sc1_hc_schizo = pd.concat([hc_sc1, schizo_sc1])


sc2_bpd_schizo = pd.concat([bpd_sc2, schizo_sc2])
sc2_bpd_hc = pd.concat([bpd_sc2, hc_sc2])
sc2_hc_schizo = pd.concat([hc_sc2, schizo2])

