import pandas as pd
import numpy as np
from rouge_score import rouge_scorer
import os
from evaluate import load
from sentence_transformers import SentenceTransformer, util


def cosine_sim(str_1, str_2):

    #get a huggingface model
    model = SentenceTransformer('embedding-data/deberta-sentence-transformer')
    # Compute embedding for both lists
    embedding_1 = model.encode(str_1, convert_to_tensor=True)
    embedding_2 = model.encode(str_2, convert_to_tensor=True)
    #get cosine sim
    sim =  util.pytorch_cos_sim(embedding_1, embedding_2)
    #sim is a tensor object - we use numpy to convert scalar tensor to scalar variable
    sim_score = sim.numpy()[0][0]
    return sim_score

def rouge(str_1, str_2):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(str_1, str_2)
    #access scores as
    # scores['rouge1'].precision or recall or fmeasure
    return scores

def bert(list_1, list_2):

    #pass two strings as list objects
    #or pass two lists of strings - if using this - use a mean function somewhere
    bertscore = load("bertscore")
    predictions = list_1
    references =list_2
    results = bertscore.compute(predictions=predictions, references=references, lang="en", model_type='microsoft/deberta-large-mnli')
    return results['precision'][0], results['recall'][0], results['f1'][0]

def process(filepath):
    i=0
    scores = []
    df = pd.read_csv(filepath)
    actual = list(df['GOLD'])
    predicted = list(df['PREDICTED'])
    for k in range(len(actual)):
        try:
            scores.append(cosine_sim(actual[k], predicted[k]))
            print('Line Number', i)
        except:
            pass
        i = i+ 1

    return scores
