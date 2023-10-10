import pandas as pd
import os

sample_path = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Bipolar Disorder_scene1/outputUM_IA_2010_Scene 1.csv'

def read_df(filepath):
    return pd.read_csv(filepath)

def return_pi_lists(dataframe):
    return list(dataframe['patient_dialogue']), list(dataframe['interviewer_dialogue'])

def list_of_files(folderpath):
    return list(os.listdir(folderpath))


def process(pat_list, int_list):
    length = max(len(pat_list), len(int_list))
    text = []
    tgt = []
    for i in range(length):

        if i ==0:
            text.append(pat_list[i])
            tgt.append(int_list[i])
            continue
        else:
            text.append(text[i-1] + tgt[i-1] + pat_list[i])
            tgt.append(int_list[i])

    processed_dict = {
        'text': text,
        'target': tgt
    }



    return processed_dict

def select_save_path(input_path):
    if input_path == '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Bipolar Disorder_scene1/':
        return '/Users/ankitaich/Documents/SSPA Project/Context Files/bd_scene_1/'
    elif input_path == '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Bipolar Disorder_scene2/':
        return '/Users/ankitaich/Documents/SSPA Project/Context Files/bd_scene_2/'
    elif input_path == '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Schizophrenia_Scene1/':
        return '/Users/ankitaich/Documents/SSPA Project/Context Files/sz_scene_1/'
    elif input_path == '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Schizophrenia_Scene2/':
        return '/Users/ankitaich/Documents/SSPA Project/Context Files/sz_scene_2/'
    elif input_path == '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Healthy Control_Scene1/':
        return '/Users/ankitaich/Documents/SSPA Project/Context Files/hc_scene_1/'
    else:
        return '/Users/ankitaich/Documents/SSPA Project/Context Files/hc_scene_2/'

def main():

    bd_1 = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Bipolar Disorder_scene1/'
    bd_2 = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Bipolar Disorder_scene2/'
    sz_1 = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Schizophrenia_Scene1/'
    sz_2 = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Schizophrenia_Scene2/'
    hc_1 = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Healthy Control_Scene1/'
    hc_2 = '/Users/ankitaich/Documents/SSPA Project/Processing Files and Folders/CSV Files/Healthy Control_Scene2/'

    #test case

    '''
    files = list_of_files(hc_2)
    df = read_df(hc_2 + files[0])
    pat_dials, int_dials = return_pi_lists(df)
    processed_df = process(pat_dials, int_dials)
    print(df)
    print('---')
    print(pd.DataFrame(processed_df))
    '''

    #make save paths

    bd_1_save = '/Users/ankitaich/Documents/SSPA Project/Context Files/bd_scene_1/'
    bd_2_save = '/Users/ankitaich/Documents/SSPA Project/Context Files/bd_scene_2/'
    sz_1_save = '/Users/ankitaich/Documents/SSPA Project/Context Files/sz_scene_1/'
    sz_2_save = '/Users/ankitaich/Documents/SSPA Project/Context Files/sz_scene_2/'
    hc_1_save = '/Users/ankitaich/Documents/SSPA Project/Context Files/hc_scene_1/'
    hc_2_save = '/Users/ankitaich/Documents/SSPA Project/Context Files/hc_scene_2/'

    #process files

    for i in [bd_1,bd_2,sz_1,sz_2,hc_1,hc_2]:
        current_files = list_of_files(i)
        savepath = select_save_path(i)
        for j in current_files:
            filename = i + j
            curr_df = read_df(filename)
            pat_dials, int_dials = return_pi_lists(curr_df)
            processed_dict = process(pat_dials, int_dials)
            new_df = pd.DataFrame(processed_dict)
            new_df.to_csv(savepath+'context aware'+j)


if __name__ == "__main__":
    main()