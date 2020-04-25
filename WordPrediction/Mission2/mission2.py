from nltk import bigrams, ConditionalFreqDist, FreqDist, Text
from nltk.lm.preprocessing import flatten, pad_both_ends
import random
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline

from nltk.tokenize.treebank import TreebankWordDetokenizer

detokenize = TreebankWordDetokenizer().detokenize


def generate_sent(model, num_words, random_seed=42):
    """
    :param model: An ngram language model from `nltk.lm.model`.
    :param num_words: Max no. of words to generate.
    :param random_seed: Seed value for random.
    """
    content = []
    for token in model.generate(num_words, random_seed=random_seed):
        # if token == '<s>':
        #     continue
        # if token == '</s>':
        #     break
        if len(content) > 20:
            break
        if token != '</s>' and token != '<s>':
            content.append(token)
    return detokenize(content)


# text = ['i like chinese food', 'chinese people like food']
text = open("text.txt").read().replace(". ", ".").lower().replace("\n", " ")
text = text.split(".")
text = [i for i in text if i != ""]

preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
tokens = list(flatten(preprocessed))
# print(tokens)
tokens_list = list(set(tokens))  # set doesn't allow duplicates

tokenized_text = [i.split(" ") for i in text]

n = 2
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
model = MLE(n)
model.fit(train_data, padded_sents)
print(model.score("plate", ["with"]))
# like chinese: 1/2
# like food: 1/2

print(generate_sent(model, 20, random_seed=0))
print(generate_sent(model, 20, random_seed=30))

n = 3
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
model = MLE(n)
model.fit(train_data, padded_sents)
print(model.score("chinese", ["i", "like"]))
# i like chinese: 1/1

print(generate_sent(model, 20, random_seed=10))
