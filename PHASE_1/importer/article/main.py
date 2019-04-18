#! python3
from nlpe import Nlpe
import fileinput
from json import loads
import json
import threading
import time
import multiprocessing


def parse_article(article):
    article = loads(article)
    nl = Nlpe(article['headline']+" "+article['main_text'])

    # get those values
    places = nl.get_places()
    syndrome = nl.get_syndrome()
    disease = nl.get_disease()
    event_type = nl.get_event()
    country = nl.get_country()
    people = nl.get_people()
    date = nl.get_date()

    return json.dumps(
            {
                'article': article,
                'date': date,
                'country': places,
                'Type': event_type,
                'people': people,
                'syndrome': syndrome,
                'disease': disease
            }
        )


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

    p =  multiprocessing.Pool()
    res = p.map(parse_article, it)
    for r in res:
        print(r)