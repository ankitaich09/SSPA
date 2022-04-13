import subprocess
import pandas as pd
import time

input_string = "Hi, I'm your new neighbor, my name is Baal Bichi, please help me with the clinical task"

output_loc = '/Users/ankit/Documents/SSPA Project/Analysis_Codes/sample_result.ndjson'

cmd_to_execute = ["LIWC-22-cli",
                  "--mode", "wc",
                  "--input", "console",
                  "--console-text", input_string,
                  "--output", output_loc]

subprocess.call(cmd_to_execute)


time.sleep(2)

#adding a 2 second wait - to let each process finish

temp_df = pd.read_json(output_loc, lines=True)
#this contains the LIWC output of the string that was just processed.
#this is as a dataframe
