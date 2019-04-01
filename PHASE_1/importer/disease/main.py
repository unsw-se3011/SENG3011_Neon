#!python3

# prompts:
from json import loads
import requests
import threading
import time
import fileinput

# auth by the default admin user
response = requests.post(
    'http://localhost:8000/v0/jwt/',
    data={"username": "neon", "password": "apple123"}
)
token = "JWT " + response.json()['token']


def mk_request(endpoint, data):
    req = requests.post(
        'http://localhost:8000/v0/'+endpoint + '/',
        json=data,
        headers={'Authorization': token, 'Content-Type': 'application/json'}
    )
    # raise if there's an error
    req.raise_for_status()


class Worker(threading.Thread):
    def __init__(self, iteratable, endpoint):
        threading.Thread.__init__(self)
        self.it = iteratable
        self.endpoint = endpoint

    def run(self):
        try:
            while True:
                j_dict = loads(next(self.it))
                print("push " + self.endpoint+" with " + j_dict['name'])
                mk_request(self.endpoint, j_dict)
                time.sleep(1)
        except StopIteration as e:
            # we expect this error, do nothing
            pass


if __name__ == "__main__":
    # import argparse

    # # get input of command line arguement
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     'file',
    #     help="File of json line input.",
    #     type=str,
    #     default="disease.jl"
    # )
    # args = parser.parse_args()

    # # change it to an iterator to enable setting up multi-thread
    # # without dealing with lock
    # print(args.file)

    workers = []

    # # import disease
    it = iter(fileinput.input(files='disease.jl'))
    for i in range(4):
        workers.append(Worker(it, 'diseases'))

    # import syndromes
    it = iter(fileinput.input(files='syndrome.jl'))
    for i in range(4):
        workers.append(Worker(it, 'syndromes'))

    for w in workers:
        w.start()
        time.sleep(0.5)
