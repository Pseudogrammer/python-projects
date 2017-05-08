import nltk
import nltk.data
import random
from nltk import word_tokenize, sent_tokenize

def main():
    tagmap = {"NN": "a noun", "NNS": "a plural noun", "NNP": "a proper noun", "NNPS": "a plural proper noun",
              "JJ": "an adjective", "JJR": "a comparative adjective (ex: 'larger')",
              "JJS": "a superlative adjective (ex: 'largest')"}
    final_words = []
    text_data = open("gutenberg.txt").read()
    tokens = nltk.word_tokenize(text_data)
    tagged_tokens = nltk.pos_tag(tokens)
    none=[]
    adj=[]
    for item in tagged_tokens:
        if item[1] in ["NN","NNS","NNP","NNPS"]:
            none.append(item[0])
        elif item[1] in ["JJ","JJR","JJS"]:
            adj.append(item[0])
    print("Nones:",none)
    print("Adjectives:",adj)

    sel_nouns=random.choices(none,k=2)
    sel_adjs=random.choices(adj,k=2)

    print("Selected Nouns:",sel_nouns)
    print("Selected Adjectives:",sel_adjs)
    n=0
    for (word, tag) in tagged_tokens:
        if (word not in sel_nouns and word not in sel_adjs) or n>=4:
            final_words.append(word)
        else:
            if word in sel_nouns:
                final_words.append(input("Please enter a noun:"))
            else:
                final_words.append(input("Please enter a adjective:"))
            n=n+1


    print("******* OLD TEXT *******")
    print(" ".join(tokens))

    print("\n\n******* NEW TEXT *******")
    print(" ".join(final_words))

main()
