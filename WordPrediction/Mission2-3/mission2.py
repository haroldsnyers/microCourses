from nltk import bigrams, tokenize, everygrams
from nltk.lm.preprocessing import flatten, pad_both_ends
import random
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline

from nltk.tokenize.treebank import TreebankWordDetokenizer
import copy

detokenize = TreebankWordDetokenizer().detokenize


def generate_sentence(model, num_words, random_seed=42):
    """
    :param model: An ngram language model from `nltk.lm.model`.
    :param num_words: Max no. of words to generate.
    :param random_seed: Seed value for random.
    """
    content = []
    for token in model.generate(num_words, random_seed=random_seed):
        if len(content) > 20:
            break
        if token != '</s>' and token != '<s>':
            content.append(token)
    return detokenize(content)


def print_sentences(model, list_tokens, n_gram, number_of_sentences, text_begin_init, maxi=True):
    """

    :param model: model from which to generate
    :param list_tokens:
    :param n_gram:
    :param number_of_sentences:
    :param text_begin_init:
    :param maxi:
    """
    list_sentences = []
    i = 0
    while i < number_of_sentences:
        sentence_finished = False

        # starting words
        text_begin_p = list(text_begin_init)  # otherwise give same pointer to both lists
        while not sentence_finished:
            if n_gram == 2:
                param = [text_begin_p[-1]]
            elif n_gram == 3:
                param = [text_begin_p[-2], text_begin_p[-1]]
            else:
                param = [text_begin_p[-3], text_begin_p[-2], text_begin_p[-1]]
            probabilities = [model.score(i, param) for i in list_tokens]

            if max(probabilities) != 0:
                if maxi:
                    text_begin_p += [tokens_list[probabilities.index(max(probabilities))]]
                else:
                    probable_words = [index for index, prob in enumerate(probabilities) if prob != 0]
                    # print([tokens_list[i] for i in probable_words])
                    next_word = random.choice(probable_words)
                    text_begin_p += [tokens_list[next_word]]
            # Stop the text prediction after 10 word
            if len(text_begin_p) > 20 or max(probabilities) == 0:
                sentence_finished = True
        i += 1
        if text_begin_p not in list_sentences:
            list_sentences.append(text_begin_p)
            print(' '.join([word for word in text_begin_p if word != "</s>" or word != "<s>"]))
    print("number of sentences found: " + str(len(list_sentences)))


def score(start_phrase, word, model):
    phrase = ' '.join(start_phrase)
    print("probability \"" + phrase + "\" is followed by \"" + word + "\" " + str(model.score(word, start_phrase) * 100) + "%")


def generate_model(n, tokens_list):
    train_data, padded_sents = padded_everygram_pipeline(n, tokens_list)
    """Default preprocessing for a sequence of sentences.

        Creates two iterators:
        - sentences padded and turned into sequences of `nltk.util.everygrams`
        - sentences padded as above and chained together for a flat stream of words

        :param order: Largest ngram length produced by `everygrams`.
        :param text: Text to iterate over. Expected to be an iterable of sentences:
        Iterable[Iterable[str]]
        :return: iterator over text as ngrams, iterator over text as vocabulary data
        """
    model = MLE(n)
    model.fit(train_data, padded_sents)
    return model


def prepare_text(text, text_file=1):
    """
    :param text: corpus text to train model from
    :param text_file: 0 or 1 to see if text si from a textfile (thus continuous text) or already a formatted list of sentences
    :return: token_list (flat list of every words inside the corpus) and tokenized_text (sentences split split by words)
    """
    if text_file == 1:
        text = text.split(".")
    text = [i for i in text if i != ""]

    tokenized_text = [i.split(" ") for i in text]
    tokens_list = list(set(flatten(tokenized_text)))
    """
        #example tokenized_text: [['i', 'like', 'chinese', 'food'], ['chinese', 'people', 'like', 'food'], 
                    ['people', 'like', 'dogs', 'and', 'cats'], ['dogs', 'like', 'to', 'be', 'walked']]
        #example tokens_list : ['chinese', 'like', 'cats', 'people', 'walked', 'i', 'dogs', 'and', 'to', 'food', 'be']       
    """
    return tokens_list, tokenized_text


def print_out_results(tokenized_text_out, tokens_list_out, n, text_begin_out, start_phrase, word, number_sentences=3, maxi=True):
    model = generate_model(n, tokenized_text_out)
    # give probability score that a word follows a given start phrase
    score(start_phrase, word, model)
    print("\nPhrases generated by model")
    print(generate_sentence(model, 20, random_seed=0))
    print(generate_sentence(model, 20, random_seed=30))
    print("\nPhrases generated by model by hand")
    print_sentences(model, tokens_list_out, n, number_sentences, text_begin_out, maxi=maxi)
    return model


def test_PP(n_gram, model, test_file=1):
    if test_file == 1:
        test_sentences = ['he thought about a spoon', 'the eggs with dishwashing soap', "a plate with a spoon", "he thought about"]
    else:
        test_sentences = ['people like chinese food', 'chinese people like dogs', 'i like chinese people', 'dogs like food and cats']

    test_data = [list(everygrams(t.lower().split(" "), min_len=n_gram, max_len=n_gram)) for t in test_sentences]

    for test in test_data:
        test_1 = list(test)
        print("\n" + str(test_1))
        # gives the score for every bigram generated from the test sentences given the model
        print("MLE Estimates for {0} with score: {1}".format([(ngram[-1], ngram[:-1]) for ngram in test_1],
                                                             [model.score(ngram[-1], ngram[:-1]) for ngram in
                                                              test_1]))

        # calculates the perplexity
        print("Perplexity (PP): ({0}) : {1}".format([(ngram[-1], ngram[:-1]) for ngram in test_1],
                                                    model.perplexity(test_1)))


######################################
#  --- MISSION 2 ------ #
######################################
print("\n" + "#"*40 + "\n ----- MISSION 2 -----" + "\n" + "#"*40)

# Chinese
text_chinese = ['i like chinese food', 'chinese people like food', 'people like dogs and cats', 'dogs like to be walked']
tokens_list, tokenized_text = prepare_text(text_chinese, text_file=0)

print("\n" + "#"*100)

print("\nModel Bigram")

n = 2
# text to generate phrases from
text_begin = ["i", "like"]
# start phrase and word to follow
start_phr = ["like"]
word_end = "chinese"

# by hand
# 25% chance that 'like' is followed by chinese as like can be followed by chinese, people, dogs and to
# (all only one occurrence -> thus probability divided by 4 -> 100% / 4 = 25%

model_2_food = print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=20, maxi=False)
test_PP(n, model_2_food, test_file=0)

print("\n" + "#"*100)

print("\nModel Trigram")
n = 3
text_begin = ["i", "like"]
start_phr = ['i', "like"]
word_end = "chinese"
model_3_food = print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=20, maxi=False)
test_PP(n, model_3_food, test_file=0)

print("\n" + "#"*100)

print("\nModel 4-gram")

n = 4
text_begin = ["i", "like", "chinese"]
start_phr = ['i', "like"]
word_end = "chinese"
model_4_food = print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=20, maxi=False)
test_PP(n, model_4_food, test_file=0)






######################################
#  --- MISSION 3 ------ #
######################################
print("\n" + "#"*40 + "\n ----- MISSION 3 -----" + "\n" + "#"*40)

# food
text_food = open("text.txt").read().replace(". ", ".").lower().replace("\n", " ")
tokens_list, tokenized_text = prepare_text(text_food)

print("\n" + "#"*100)

print("\nModel Bigram - food")
n = 2
text_begin = ["thought"]
start_phr = ["thought"]
word_end = "about"
model_2 = print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=20, maxi=False)
# model_2 = print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=10, maxi=True)
test_PP(n, model_2)

print("\n" + "#"*100)

print("\nModel Trigram - food")
n = 3
text_begin = ["he", "poured"]
start_phr = ['he', "thought"]
word_end = "about"
model_3 = print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=20, maxi=False)
test_PP(n, model_3)

print("\n" + "#"*100)

print("\nModel Quatrogram - food")
n = 4
text_begin = ["thought", "about", "the"]
start_phr = ['the', "large", "wooden"]
word_end = "chair"
print_out_results(tokenized_text, tokens_list, n, text_begin, start_phr, word_end, number_sentences=20, maxi=False)



