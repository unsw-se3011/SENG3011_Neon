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
import json
import fileinput
from new_nltk import match_pub_date, match_places, initial_text, noun_text, country_text, match_syndrome, match_disease, match_event, match_country, match_people, match_date

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
        # print(j_dict['main_text'])

        TEXTS = []
        TEXTS = j_dict['main_text']

        pub_date = match_pub_date(j_dict['date_of_publication'])
        # print(TEXTS)
        places = match_places(TEXTS)
        pos_tags = initial_text(TEXTS)
        # print(pos_tags)
        event_tags = noun_text(TEXTS)
        country_tags = country_text(TEXTS)
        people_tags = noun_text(TEXTS)
        date_tags = noun_text(TEXTS)

        syndrome = match_syndrome(pos_tags)
        disease = match_disease(pos_tags)
        event_type = match_event(event_tags)
        country = match_country(country_tags)
        people = match_people(people_tags)
        date = match_date(date_tags)

        report = list()
        report.append(people)
        if len(date) == 0:
            report.append(pub_date)
        if len(date) != 0:
            report.append(date)
        report.append(syndrome)
        report.append(disease)
        if len(country) == 0:
            report.append(places.countries)
        if len(country) != 0:
            report.append(country)
        report.append(event_type)
        print(json.dumps(report, sort_keys=True,
                         indent=4, separators=(',', ': ')))
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
