#!python3
from json import loads, dumps
import fileinput


url_set = set()
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

    it = iter(fileinput.input(files=args.file))

    while (True):
        j_dict = loads(next(it))
        if j_dict['url'] not in url_set:
            print(dumps(j_dict))
            url_set.add(j_dict['url'])
