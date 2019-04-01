#!python3

# prompts:
from json import loads
import requests
import threading
import time
import fileinput


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


BASE_URL = 'http://neon.whiteboard.house/v0/'
# # auth by the default admin user
# response = requests.post(
#     BASE_URL+'jwt/',
#     data={"username": "neon", "password": "apple123"}
# )
token = ""

input_lock = threading.Lock()
input_count = 0

request_locks = []


def mk_request(endpoint, data):
    global token
    # making the request
    req = requests.post(
        BASE_URL+endpoint + '/',
        json=data,
        headers={'Authorization': token, 'Content-Type': 'application/json'}
    )
    # raise if there's an error
    req.raise_for_status()

    return req


def refresh_token():
    global token, request_locks

    # acquire lock
    [l.acquire() for l in request_locks]

    response = requests.post(
        BASE_URL+'jwt/',
        data={"username": "neon", "password": "apple123"}
    )
    token = "JWT " + response.json()['token']
    # release the lock for request
    [l.release() for l in request_locks]

    # set up another timer for next refresh
    threading.Timer(240, refresh_token)


def mk_report(j_dict):
    """
    Selection of the result,
    make the best choice of the data
    change the output format when the version is changed
    """

    data = {
        'disease': j_dict['disease'],
        'syndrome': [SYNDROME_MAP[s] for s in j_dict['syndrome']]
    }
    if j_dict['Type']:
        public_date = j_dict['article']['date_of_publication']

        report_event = {
            'e_type': EVENT_TYPE_MAP[j_dict['Type'][0]],
            'start_date': public_date[:10] + 'T00:00',
            'sd_fuzz': "H",
            'end_date': public_date[:10] + 'T00:00',
            'ed_fuzz': "H",
        }

        # parse the people
        if j_dict['people']:
            report_event['number_affected'] = min(j_dict['people'])

        # parse the country
        if j_dict['country']:
            country_list = [t for t in j_dict['country'] if
                            'country' in t]
            state_list = [t for t in j_dict['country'] if
                          'state' in t]
            city_list = [t for t in j_dict['country'] if
                         'city' in t]
            if city_list:
                report_event['location'] = city_list[0]
            elif state_list:
                report_event['location'] = state_list[0]
            elif country_list:
                report_event['location'] = country_list[0]
        data['report_event'] = [report_event]
    for key, value in data.items():
        # check all the field has data
        if value:
            return data
    return {}


class Worker(threading.Thread):
    def __init__(self, iteratable):
        global request_locks
        threading.Thread.__init__(self)
        self.it = iteratable
        # add my lock to global stage
        self.my_lock = threading.Lock()
        request_locks.append(self.my_lock)

    def run(self):
        global input_lock, input_count
        try:
            while True:
                # locking it to prevent some issue
                input_lock.acquire()
                self.j_dict = next(self.it)
                counter = input_count
                input_count += 1
                input_lock.release()

                self.j_dict = loads(self.j_dict)

                if counter % 100 == 0:
                    print(
                        str(counter) + ": with " +
                        self.j_dict['article']['url']
                    )

                try:
                    # send the article
                    self.send_article()
                    # send the report && report event
                    self.send_report()
                except requests.HTTPError as e:
                    print(str(counter) + ": " + self.j_dict['article']['url'])
                    self.my_lock.release()
                # time.sleep(1)
        except StopIteration as e:
            # we expect this error, do nothing
            pass

    def send_article(self):
        # lock this request
        # print(self.j_dict['article'])
        self.j_dict['article']['publish'] = \
            self.j_dict['article']['date_of_publication'][:10] + 'T00:00'

        self.j_dict['article']['p_fuzz'] = 'H'

        self.my_lock.acquire()
        ret = mk_request('articles', self.j_dict['article'])
        self.my_lock.release()
        self.id = ret.json()['id']

    def send_report(self):
        report = mk_report(self.j_dict)
        if report:
            # there's value in report

            # attach article id
            report['article_id'] = self.id

            # push request
            self.my_lock.acquire()
            mk_request('reports', report)
            self.my_lock.release()


if __name__ == "__main__":
    # import argparse
    workers = []
    # start the timer to refresh the token
    refresh_token()

    time.sleep(2)

    # import disease
    it = iter(fileinput.input(files='output.jl'))
    for i in range(8):
        workers.append(Worker(it))

    # print(mk_report(loads(next(it))))

    # start up the sender
    for w in workers:
        w.start()
        time.sleep(0.5)
