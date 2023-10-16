import pandas as pd
import os


saved_files = {
    'bd_1':'/Users/ankitaich/Documents/SSPA Project/Context Files/bd_scene_1/',
    'bd_2':'/Users/ankitaich/Documents/SSPA Project/Context Files/bd_scene_2/',
    'sz_1':'/Users/ankitaich/Documents/SSPA Project/Context Files/sz_scene_1/',
    'sz_2':'/Users/ankitaich/Documents/SSPA Project/Context Files/sz_scene_2/',
    'hc_1':'/Users/ankitaich/Documents/SSPA Project/Context Files/hc_scene_1/',
    'hc_2':'/Users/ankitaich/Documents/SSPA Project/Context Files/hc_scene_2/'
}

#these are list of files in each list
bd_1 = os.listdir(saved_files['bd_1'])
bd_2 = os.listdir(saved_files['bd_2'])
sz_1 = os.listdir(saved_files['sz_1'])
sz_2 = os.listdir(saved_files['sz_2'])
hc_1 = os.listdir(saved_files['hc_1'])
hc_2 = os.listdir(saved_files['hc_2'])

#take 75 files from each list
#add text to one list
#target to other list
#make dataframe -> csv
#same for 25

text_train = []
target_train = []

#train on all - therefore every subject speech gets in train set
#inference happens individually so we build that separately



'''
for i in [bd_1, bd_2, sz_1, sz_2, hc_1, hc_2]:
    for j in range(75):
        if i == bd_1:
            #print(i[j])
            text_train.append(list(pd.read_csv(saved_files['bd_1']+i[j])['text']))
            target_train.append(list(pd.read_csv(saved_files['bd_1']+i[j])['target']))
        elif i == bd_2:
            #print(i[j])
            text_train.append(list(pd.read_csv(saved_files['bd_2']+i[j])['text']))
            target_train.append(list(pd.read_csv(saved_files['bd_2']+i[j])['target']))
        elif i == sz_1:
            #print(i[j])
            text_train.append(list(pd.read_csv(saved_files['sz_1']+i[j])['text']))
            target_train.append(list(pd.read_csv(saved_files['sz_1']+i[j])['target']))
        elif i == sz_2:
            #print(i[j])
            text_train.append(list(pd.read_csv(saved_files['sz_2']+i[j])['text']))
            target_train.append(list(pd.read_csv(saved_files['sz_2']+i[j])['target']))
        elif i == hc_1:
            #print(i[j])
            text_train.append(list(pd.read_csv(saved_files['hc_1']+i[j])['text']))
            target_train.append(list(pd.read_csv(saved_files['hc_1']+i[j])['target']))
        else:
            #print(i[j])
            text_train.append(list(pd.read_csv(saved_files['hc_2']+i[j])['text']))
            target_train.append(list(pd.read_csv(saved_files['hc_2']+i[j])['target']))

#now text train and target train have lists in them
#where each list is one CSV file of conversation
#we need to unravel all the lists

train_text = [item for sublist in text_train for item in sublist]
train_tgt =  [item for sublist in target_train for item in sublist]

#now these two lists above have K items where the ith text in train_text expects the ith item in train_tgt
#we can make a CSV for Seq2Seq SFT

data = {
    'text': train_text,
    'target': train_tgt
}

df = pd.DataFrame(data)
df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_train.csv', index=False)

'''


#creating test sets
#initialize empty lists for text and target

bd_1_test_text = []
bd_1_test_tgt = []

sz_1_test_text = []
sz_1_test_tgt = []

hc_1_test_text = []
hc_1_test_tgt = []


bd_2_test_text = []
bd_2_test_tgt = []

sz_2_test_text = []
sz_2_test_tgt = []

hc_2_test_text = []
hc_2_test_tgt = []


#process similarly, from 75-100 index for each scene
#take in text and target from original data frame and append

for i in [bd_1, bd_2, sz_1, sz_2, hc_1, hc_2]:
    for j in range(70, 99):
        if i == bd_1:
            #print(i[j])
            bd_1_test_text.append(list(pd.read_csv(saved_files['bd_1']+i[j])['text']))
            bd_1_test_tgt.append(list(pd.read_csv(saved_files['bd_1']+i[j])['target']))
        elif i == bd_2:
            #print(i[j])
            bd_2_test_text.append(list(pd.read_csv(saved_files['bd_2']+i[j])['text']))
            bd_2_test_tgt.append(list(pd.read_csv(saved_files['bd_2']+i[j])['target']))
        elif i == hc_1:
            #print(i[j])
            hc_1_test_text.append(list(pd.read_csv(saved_files['hc_1']+i[j])['text']))
            hc_1_test_tgt.append(list(pd.read_csv(saved_files['hc_1']+i[j])['target']))
        elif i == hc_2:
            #print(i[j])
            hc_2_test_text.append(list(pd.read_csv(saved_files['hc_2']+i[j])['text']))
            hc_2_test_tgt.append(list(pd.read_csv(saved_files['hc_2']+i[j])['target']))
        elif i == sz_1:
            #print(i[j])
            sz_1_test_text.append(list(pd.read_csv(saved_files['sz_1']+i[j])['text']))
            sz_1_test_tgt.append(list(pd.read_csv(saved_files['sz_1']+i[j])['target']))
        else:
            #print(i[j])
            sz_2_test_text.append(list(pd.read_csv(saved_files['sz_2']+i[j])['text']))
            sz_2_test_tgt.append(list(pd.read_csv(saved_files['sz_2']+i[j])['target']))


#make test dictionaries and directly flatten the above lists into them

bd_1_test = {
    'text': [item for sublist in bd_1_test_text for item in sublist],
    'target': [item for sublist in bd_1_test_tgt for item in sublist]
}

bd_2_test = {
    'text': [item for sublist in bd_2_test_text for item in sublist],
    'target': [item for sublist in bd_2_test_tgt for item in sublist]
}

hc_1_test = {
    'text': [item for sublist in hc_1_test_text for item in sublist],
    'target': [item for sublist in hc_1_test_tgt for item in sublist]
}

hc_2_test = {
    'text': [item for sublist in hc_2_test_text for item in sublist],
    'target': [item for sublist in hc_2_test_tgt for item in sublist]
}

sz_1_test = {
    'text': [item for sublist in sz_1_test_text for item in sublist],
    'target': [item for sublist in sz_1_test_tgt for item in sublist]
}

sz_2_test = {
    'text': [item for sublist in sz_2_test_text for item in sublist],
    'target': [item for sublist in sz_2_test_tgt for item in sublist]
}


#make dataframes and write to CSV

bd_1_df = pd.DataFrame(bd_1_test)
bd_1_df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_BD_Scene_1.csv', index=False)

bd_2_df = pd.DataFrame(bd_2_test)
bd_2_df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_BD_Scene_2.csv', index=False)

hc_1_df = pd.DataFrame(hc_1_test)
hc_1_df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_HC_Scene_1.csv', index=False)

hc_2_df = pd.DataFrame(hc_2_test)
hc_2_df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_HC_Scene_2.csv', index=False)

sz_1_df = pd.DataFrame(sz_1_test)
sz_1_df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_SZ_Scene_1.csv', index=False)

sz_2_df = pd.DataFrame(sz_2_test)
sz_2_df.to_csv('/Users/ankitaich/Documents/SSPA Project/context_SFT_SZ_Scene_2.csv', index=False)
