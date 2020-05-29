from nltk import bigrams, ConditionalFreqDist, FreqDist, Text
from nltk.lm.preprocessing import flatten, pad_both_ends
import random

# text = ['i like chinese food', 'chinese people like food']
text = open("text.txt").read().replace(". ", ".").lower().replace("\n", " ")
text = text.split(".")
text = [i for i in text if i != ""] # generates a list of the phrases found in the text
print(text)

preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
tokens = list(flatten(preprocessed)) # flatten list of text
tokens_list = list(set(tokens))  # set doesn't allow duplicates, list of all different words found in text

fd = FreqDist(tokens)
print(fd['took'])

model = bigrams(tokens)
cfd = ConditionalFreqDist(model)
print(cfd['took']['out'])

list_sentences = []
while len(list_sentences) < 6:
    sentence_finished = False
    # starting words
    text_begin = ["<s>", "took"]

    while not sentence_finished:
        probabilities = [cfd[text_begin[-1]][i] for i in tokens_list]
        if max(probabilities) != 0:
            probable_words = [index for index, prob in enumerate(probabilities) if prob != 0]
            print(probable_words)
            next_word = random.choice(probable_words)
            print(next_word)
            # print([tokens_list[next] for next in probable_words])
            # print([probabilities[next] for next in probable_words])
            text_begin += [tokens_list[probabilities.index(max(probabilities))]]
            # text_begin += [tokens_list[next_word]]
        # Stop the text prediction after 10 word
        if len(text_begin) > 20:
            sentence_finished = True
    print(' '.join([word for word in text_begin if word != "</s>" or word != "<s>"]))
    list_sentences.append(text_begin)
    sentence_finished = False

