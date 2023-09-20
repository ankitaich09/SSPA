import random
from transformers import AutoModelForCausalLM, AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import T5ForConditionalGeneration
import torch
import pandas as pd
import sys

def initialize_model(checkpoint, model_type="ED"):

    if model_type == 't5':
        model = T5ForConditionalGeneration.from_pretrained(checkpoint, device_map="auto")
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    if model_type == 'D':
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype="auto", device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, torch_dtype="auto", device_map="auto")

    return model, tokenizer

def draw_inference(input_list, model, tokenizer):

    count = 0
    prediction = []
    for each_prompt in input_list:
        print('Starting ' + str(count) + '\n')
        inputs = tokenizer(each_prompt, return_tensors="pt").input_ids.to('cuda')
        outputs = model.generate(inputs, max_new_tokens=100)
        predicted = (tokenizer.decode(outputs[0]).replace('<pad>', '').replace('</s>', '').strip())
        # detach previous tensor from GPU
        inputs = inputs.to('cpu')
        print(predicted)
        prediction.append(predicted)
        print('Finishing ' + str(count) + '\n')
        count += 1

    return prediction

#for best results run in a notebook
#create prompts and add to a list called input_list
#initialize model and tokenizer
#run draw_inference