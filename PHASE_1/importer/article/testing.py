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
    # print(args.file)

    # while is here

    it = iter(fileinput.input(files=args.file))

    j_dict = loads(next(it))
    # print(j_dict['main_text'])

    nl = Nlpe(j_dict['main_text'])

    places1 = list()

    # get those values
    places = nl.get_places()
    syndrome = nl.get_syndrome()
    disease = nl.get_disease()
    event_type = nl.get_event()
    country = nl.get_country()
    people = nl.get_people()
    date = nl.get_date()

    # print the output
    print(
        json.dumps(
            {
                'date': date,
                'country': places,
                'Type': event_type,
                'people': people,
                'syndrome': syndrome,
                'disease': disease
            }
        )
    )
