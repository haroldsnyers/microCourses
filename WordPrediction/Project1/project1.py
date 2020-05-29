from nltk import bigrams, tokenize, everygrams, trigrams, ConditionalFreqDist
from nltk.lm.preprocessing import flatten, pad_both_ends
import random
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline

from nltk.tokenize.treebank import TreebankWordDetokenizer
import copy

detokenize = TreebankWordDetokenizer().detokenize


class WordPrediction:
    def __init__(self, text, ngram=2):
        self.tokens_list, self.tokenized_text = self.__prepare_text(text)
        self._model = self.__generate_model(ngram)
        self.cfd = self.__condition(ngram)
        self._ngram = ngram

    def __condition(self, ngram):
        if ngram == 3:
            condition_pairs = (((w0, w1), w2) for w0, w1, w2 in self._model)
            return ConditionalFreqDist(condition_pairs)
        else:
            return ConditionalFreqDist(self._model)

    def __prepare_text(self, text_to_prepare, text_file=1):
        """
        :param text: corpus text to train model from
        :param text_file: 0 or 1 to see if text si from a textfile (thus continuous text) or already a formatted list of sentences
        :return: token_list (flat list of every words inside the corpus) and tokenized_text (sentences split split by words)
        """
        if text_file == 1:
            text_to_prepare = text_to_prepare.split(".")
        text = [i for i in text_to_prepare if i != ""]

        preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
        tokenized_text = list(flatten(preprocessed))  # flatten list of text
        tokens_list = list(set(tokenized_text))

        return tokens_list, tokenized_text

    def __generate_model(self, ngram):
        if ngram == 2:
            model = bigrams(self.tokenized_text)
        else:
            model = trigrams(self.tokenized_text)
        return model

    def start_writing(self, start_phrase):
        continue_writing = True
        while continue_writing:
            if self._ngram == 2:
                param = start_phrase[-1]
            else:
                param = (start_phrase[-2], start_phrase[-1])
            probabilities = [self.cfd[param][i] for i in self.tokens_list]
            if max(probabilities) != 0:
                probable_words = [index for index, prob in enumerate(probabilities) if prob != 0]
                list_words = [self.tokens_list[next] for next in probable_words]
                list_frequencies = [probabilities[next] for next in probable_words]
                for index, word in enumerate(list_words):
                    print(str(index) + ": " + word + " - freq : " + str(list_frequencies[index]))
                while True:
                    try:
                        word_input = input("Choose word (from index (number) or Quit(Q):")
                        if word_input == "Q":
                            break
                        next_word = probable_words[int(word_input)]
                        start_phrase += [self.tokens_list[next_word]]
                        print(' '.join([word for word in start_phrase if word != "</s>" or word != "<s>"]))
                        break
                    except:
                        print("That's not a valid option! Choose an index from list only! ")
            cont = str(input("Continue writing? y/N "))
            if cont == 'N':
                continue_writing = False

        print("final sentence : " + ' '.join([word for word in start_phrase if word != "</s>" or word != "<s>"]))


text_food = open("text1.txt").read().replace(". ", ".").lower().replace("\n", " ")
text_begin = ["<s>", "i"]

print("\n" + "#"*100)
print("\nModel Bigram")
wordpredictor_2 = WordPrediction(text_food, 2)

wordpredictor_2.start_writing(text_begin)

print("\n" + "#"*100)
print("\nModel Trigram")
wordpredictor_2 = WordPrediction(text_food, 3)

wordpredictor_2.start_writing(text_begin)
