from nltk.lm.preprocessing import flatten, pad_both_ends

text_init = ["Chinese people like food", "people like dogs", "dogs like people and food"]

# bigram 
text = [i for i in text_init if i != ""]

preprocessed = [pad_both_ends(s.split(' '), n=2) for s in text]
tokens = list(flatten(preprocessed)) # flatten list of text
tokens_list = list(set(tokens))
print(str(tokens) + "\n" + str(tokens_list))

bigram = []
trigram = []
for index, elem in enumerate(tokens):
    if index == 0:
        pass
    elif index == 1:
        bigram.append((tokens[index], tokens[index-1] ))
    else :
        bigram.append((tokens[index] , tokens[index-1] ))
        trigram.append((tokens[index] , (tokens[index-2], tokens[index-1])))
    
print(bigram)
print("\n")
print(trigram)

