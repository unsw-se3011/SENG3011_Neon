#!/usr/bin/python3

"""
randomly fetch the test article 
"""
import os
import fileinput
from json import loads, dumps


def get_line_count(file_name):
    output = os.popen('wc ' + file_name).read()
    # read the output as an array
    output = [t for t in output.split(' ') if t != '']
    return int(output[0])


need_fetch = set()


if __name__ == "__main__":
    import argparse
    import random

    # get input of command line arguement
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        help="File of json line input.",
        type=str,
        default="outbreak.jl"
    )
    parser.add_argument(
        'article_count',
        help="How many article need to fetch.",
        type=int,
        default=20
    )
    args = parser.parse_args()

    lines = get_line_count(args.file)

    while len(need_fetch) < args.article_count:
        need_fetch.add(random.randrange(lines))

    # sort the randomly generated number to increase the fetch performance
    lines = [t for t in need_fetch]
    lines.sort()

    it = iter(fileinput.input(files=args.file))
    i = 0

    article_arr = []

    while True:
        # fetch the correspond lines
        try:
            article = next(it)
            if i in lines:
                # we need this article
                article = loads(article)
                report = {
                    'disease': ['sss'],
                    'syndrome': ['sss'],
                    'reported_events': [
                        {
                            'type': 'Recovered',
                            'start_date': '2018-12-01T00:00:00',
                            'end_date': '2018-12-01T00:00:00',
                            'location': '',
                            'number-affected': 10
                        }
                    ]
                }
                article['reports'] = [report]
                article_arr.append(article)
        except StopIteration as e:
            # end of iteration, we don't need to do anything
            break

        i += 1
    # dump the random article
    print(dumps(article_arr))
