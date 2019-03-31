#! python3
from new_nltk import match_pub_date, match_places, initial_text, noun_text, country_text, match_syndrome, match_disease, match_event, match_country, match_people, match_date
import fileinput
import json
from json import loads
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.stem import *
from nltk.corpus import *
from nltk.tokenize import *  # sent_tokenize, word_tokenize
# print("imhere")
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
        places1 = list()
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
        print({'date': pub_date, 'location': places, 'Type': event_type,
               'people': people, 'syndrome': syndrome, 'disease': disease})
