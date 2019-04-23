#!/usr/bin/python3

# prompts:
from json import loads, dumps
import requests
import threading
import time
import fileinput
from traceback import print_exc

# BASE_URL = 'http://neon.whiteboard.house/v0/'
BASE_URL = 'http://localhost:8000/v0/'

THREAD_COUNT = 1


PRESENCE = "P"
DEATH = "D"
INFECTED = "I"
HOSPITALISED = "H"
RECOVERED = "R"

EVENT_TYPE_MAP = {
    'presence': PRESENCE,
    'death': DEATH,
    'infected': INFECTED,
    'hospitalised': HOSPITALISED,
    'recovered': RECOVERED,
}

SYNDROME_MAP = {
    'encephalitis': 'Encephalitis',
    'meningitis': 'Meningitis',
}


token = ""
timer = None

input_lock = threading.Lock()
input_count = 0

request_sem = threading.Semaphore(THREAD_COUNT)


def refresh_token():
    global token, request_sem, timer

    # hold the lock to refresh the token
    for i in range(THREAD_COUNT):
        print("acuireing lock - " + str(i))
        request_sem.acquire()

    response = requests.post(
        BASE_URL+'jwt/',
        data={"username": "neon", "password": "apple123"}
    )
    old_token = token
    token = "Bearer " + response.json()['access']

    if old_token != token:
        print("get Refreshed token")

    # release the lock for thead to make request
    for i in range(THREAD_COUNT):
        print("releasing - " + str(i))
        request_sem.release()

    print("set up another timer")
    # set up another timer for next refresh
    timer = threading.Timer(270, refresh_token)
    timer.start()


def mk_request(endpoint, data):
    global token

    request_sem.acquire()

    # making the request
    req = requests.post(
        BASE_URL+endpoint + '/',
        json=data,
        headers={'Authorization': token, 'Content-Type': 'application/json'}
    )
    request_sem.release()

    # raise if there's an error
    req.raise_for_status()

    return req


def mk_article(data: dict):
    article = data
    return {
        'date_of_publication': article['date_of_publication'],
        'p_fuzz': 'H',
        "url": article['url'],
        "headline": article['headline'],
        "main_text": article['main_text'],
        "img": ""
    }


def mk_report(data: dict, article_id: int):
    # remap some filed and deleteit
    data['article_id'] = article_id
    # data['sd_fuzz'] = data['start_date_fuzz']
    # data['ed_fuzz'] = data['end_date_fuzz']
    # del data['start_date_fuzz']
    # del data['end_date_fuzz']
    return data


class Worker(threading.Thread):
    def __init__(self, iteratable):
        global request_locks
        threading.Thread.__init__(self)
        self.it = iteratable

    def run(self):
        global input_lock, input_count, timer
        try:
            while True:
                # locking it to prevent some issue
                input_lock.acquire()
                self.j_dict = next(self.it)
                counter = input_count
                input_count += 1
                input_lock.release()

                self.j_dict = loads(self.j_dict)
                # print(self.j_dict)
                if counter % 100 == 0:
                    print(
                        str(counter) + ": with " +
                        self.j_dict['url']
                    )

                try:
                    # send the article
                    self.send_article()
                    # send the report && report event
                    self.send_report()
                except requests.HTTPError as e:
                    print(str(counter) + ": " + self.j_dict['url'])
                    print(dumps(self.j_dict))
                    print_exc()
                    # time.sleep(1)
        except StopIteration as e:
            input_lock.release()
            # we expect this error, do nothing
            timer.cancel()

    def send_article(self):
        # lock this request
        # make up the article object
        article = mk_article(self.j_dict)

        # send the request through the network
        ret = mk_request('articles', article)

        # print(dumps(report))
        # exit()
        self.id = ret.json()['id']

    def send_report(self):
        for report in self.j_dict['report']:
            # there's value in report

            # push request
            try:
                mk_request(
                    'reports',
                    mk_report(report, self.id)
                )
            except Exception as e:
                print_exc()
                print(dumps(report))


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
    # import argparse
    workers = []
    # start the timer to refresh the token
    refresh_token()

    time.sleep(2)

    # import disease
    it = iter(fileinput.input(files=args.file))

    for i in range(THREAD_COUNT):
        workers.append(Worker(it))

    # print(mk_report(loads(next(it))))

    # start up the sender
    for w in workers:
        w.start()
        time.sleep(0.5)
