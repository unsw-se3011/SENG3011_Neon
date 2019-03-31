#! python3
from nlpe import Nlpe
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

    # while is here

    it = iter(fileinput.input(files=args.file))

    j_dict = loads(next(it))
    # print(j_dict['main_text'])

    nl = Nlpe(j_dict['main_text'])

    pub_date = j_dict['date_of_publication']
    # print(TEXTS)
    places1 = list()
    places = nl.get_places()

    pos_tags = nl.initial_text()
    event_tags = nl.noun_text()
    country_tags = nl.country_text()
    people_tags = nl.noun_text()
    date_tags = nl.noun_text()

    # print(pos_tags)

    syndrome = nl.get_syndrome(pos_tags)
    disease = nl.get_disease(pos_tags)
    event_type = nl.get_event(event_tags)
    country = nl.get_country(country_tags)
    people = nl.get_people(people_tags)
    date = nl.get_date(date_tags)
    print({'date': pub_date, 'location': places, 'Type': event_type,
           'people': people, 'syndrome': syndrome, 'disease': disease})
