# SSPA
Collaborative Project - UIC - UCSD - UTD - UMiami

Meeting notes in trello 

Next steps to extract features. Update 24th Feb 2022


25th Feb update - Added code for visualizing ngrams and extracting ngrams

25th Feb update - Added code to extract keywords

28th Feb - update to Ngrams - better extractions - update emolex - emotion scores and affect details

1st March - Conversions to csv - starting feature vector generation - added ngrams

2nd March - Feature Vectors being generated - emolex, utterance features added, ngrams added into json

3rd March - Features of lexical richness added

3rd March - Lexical Richness Features Explanations

words = w
unique words = t

ttr = t/w - (Chotlos 1944, Templin 1957)

rttr = t/sqrt(w) - (Guiraud 1954, 1960)

cttr = t/sqrt(2w) - (Carrol 1964)

Herdan = log(t)/log(w) -- (Herdan 1960, 1964)

Summer = log(log(t))/ log(log(w)) - Summer (1966)

Dugast = 	(log(w) ** 2) / (log(w) - log(t) Dugast (1978)

Maas  = (log(w) - log(t)) / (log(w) ** 2) Maas (1972)


Binary Classification Working 

Multi class w/ healthy controls giving VERY low F1 scores - on classical models.

Added LIWC for string level classification

Added json formatting for LIWC - need to add feature vector



April 28th 

Start writing first paper - 

feature analysis
LDA
cluster feature analysis
dataset validity proof
test models on 1v1 schizo vs health or bpd vs health


December update

Paper Published

workingo n proposal and next paper

for code refer to


demographic_extract.ipynb 
make combined data.ipynb

on Colab
