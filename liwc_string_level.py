import subprocess
import pandas as pd
import time

def get_liwc_dict(input_str):

    output_loc = '/Users/ankit/Documents/SSPA Project/Analysis_Codes/temp_liwc.ndjson'

    cmd_to_execute = ["LIWC-22-cli",
                      "--mode", "wc",
                      "--input", "console",
                      "--console-text", input_str,
                      "--output", output_loc]

    subprocess.call(cmd_to_execute)


    time.sleep(2)
    print('------waiting to process------')
    #adding a 2 second wait - to let each process finish

    temp_df = pd.read_json(output_loc, lines=True)
    #this contains the LIWC output of the string that was just processed.
    #this is as a dataframe


    #add pandas to JSON

    #pipeline - read file with text - join text as one string - find liwc features - add to JSON file - add to feature vector

    return temp_df.to_dict()
