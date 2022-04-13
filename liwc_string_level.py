import subprocess

input_string = "Hi, I'm your new neighbor, my name is Baal Bichi, please help me with the clinical task"

output_loc = '/Users/ankit/Documents/SSPA Project/Analysis_Codes/sample_result.ndjson'

cmd_to_execute = ["LIWC-22-cli",
                  "--mode", "wc",
                  "--input", "console",
                  "--console-text", input_string,
                  "--output", output_loc]

subprocess.call(cmd_to_execute)
