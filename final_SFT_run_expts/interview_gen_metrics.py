import pandas as pd
import numpy as np
from rouge_score import rouge_scorer
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
    return sim

def rouge(str_1, str_2):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(str_1, str_2)

    return scores

def bert(list_1, list_2):

    bertscore = load("bertscore")
    predictions = list_1
    references =list_2
    results = bertscore.compute(predictions=predictions, references=references, lang="en", model_type='microsoft/deberta-large-mnli')
    return results

