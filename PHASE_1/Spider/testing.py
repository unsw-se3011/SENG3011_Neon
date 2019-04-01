#!python3

# prompts:

# python3 testing.py
# import nltk
# nltk.download(all)

from nltk.tokenize import *  # sent_tokenize, word_tokenize
from nltk.corpus import *
from nltk.stem import *


from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg
from json import loads

import fileinput


# # sample text
# sample = gutenberg.raw(
#     "/Users/iriszhang/Desktop/ProjectNeon-w1-nltk/scraper/oubreak.jl")

# tok = sent_tokenize(sample)

# for x in range(5):
#     print(tok[x])
#     print('\n')

if __name__ == "__main__":
    import argparse

    # get input of command line arguement
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        help="File of json line input.",
        type=str,
        default="outbreak.jl"
    )
    args = parser.parse_args()

    # change it to an iterator to enable setting up multi-thread
    # without dealing with lock
    print(args.file)

    it = iter(fileinput.input(files=args.file))

    while True:
        j_dict = loads(next(it))
        print(j_dict['main_text'])
# sentence = "Hello, this is a test for nltk testing"
# s1 = "This is a sample sentence, showing off the stop words filtration."
# stop_words = set(stopwords.words('english'))


# filtered_sentence = []

# for w in word_tokenize(s1):
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(filtered_sentence)


# filtered_sentence = []

# new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
# ps = PorterStemmer()

# for w in word_tokenize(new_text):
#     filtered_sentence.append(ps.stem(w))

# print(filtered_sentence)


# print(sent_tokenize(sentence))
# print(word_tokenize(sentence))