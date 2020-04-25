from nltk.corpus import reuters
import nltk
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

nltk.download()

# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance
for sentence in reuters.sents():
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        model[w1][w2] += 1

# Let's transform the counts to probabilities
for w1 in model:
    total_count = float(sum(model[w1].values()))
    for w2 in model[w1]:
        model[w1][w2] /= total_count