#!/usr/bin/python3

import requests
import json
from json import dumps
import re
import datetime
from locationSet import LocationSet
from math import ceil

# http://api.pandetrack.online/listall/reports

# "2019-07-01Txx:xx:xx"
FUZZ_MAP = {
    6: "Y",
    5: "M",
    4: "D",
    3: "H",
    2: "I",
    1: "S",
    0: "A"
}


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


def dd(str):
    print(str)
    exit(0)


class FuzzDate(object):
    def __init__(self, date_str):
        self.date_str = date_str
        res = re.search(
            r'([0-9]{4})-([0-9x]{1,2})-([0-9x]{1,2})T([0-9x]{1,2}):([0-9x]{1,2}):([0-9x]{1,2})', self.date_str)
        if res is not None:
            self.date_group = [t for t in res.groups()]
        else:
            res = re.search(
                r'([0-9]{4})-([0-9x]{1,2})-([0-9x]{1,2}) ([0-9x]{1,2}):([0-9x]{1,2}):([0-9x]{1,2})', self.date_str)
            self.date_group = [t for t in res.groups()]

        # count how much field is fuzzy and replace it
        self.fuzz_count = 0
        new_date_group = []
        index = 0
        for t in self.date_group:
            if t[0] == 'x':
                self.fuzz_count += 1
                # replace the t = 01
                if index < 3:
                    t = "01"
                else:
                    t = "00"
            new_date_group.append(t)

            index += 1
        # replace the new date group
        self.date_group = [int(t) for t in new_date_group]

    def get_datetime(self):
        # easy python list to function input
        return datetime.datetime(*self.date_group).isoformat()

    def get_fuzz_level(self):
        return FUZZ_MAP[self.fuzz_count]


class ReportParser(object):
    def __init__(self, report: dict):
        self.report = report

        temp_list = []
        for t in self.report['reported_events']:
            temp_list += self.parseReportEvent(t)
        self.report['report_events'] = temp_list

        del self.report['reported_events']
        # print(dumps(self.dumps()))

    def parseReportEvent(self, re):
        fd = FuzzDate(re['date'])

        # dd(fd.get_fuzz_level())
        re['start_date'] = fd.get_datetime()
        re['start_date_fuzz'] = fd.get_fuzz_level()
        re['end_date'] = fd.get_datetime()
        re['end_date_fuzz'] = fd.get_fuzz_level()
        # we don't need the old date anymore
        del re['date']

        re['type'] = EVENT_TYPE_MAP[re['type']]

        ls = LocationSet()

        # ramen have two level location, both name location
        [ls.add(l['location']) for l in re['location']]

        if len(ls.location_list) > 1:
            #  we need to handle this type of location list
            # split the number affect betweeen locations

            tmp_list = []
            for l in ls.location_list:
                # do some calculation
                re_copy = {**re}
                re_copy['location'] = l
                re_copy['number_affected'] = \
                    ceil(re['number-affected'] / len(ls.location_list))
                tmp_list.append(re_copy)

            return tmp_list

        elif ls.location_list:

            # use the first location in the list
            # we expect only one location
            re['location'] = ls.location_list[0]
        else:
            re['location'] = None
       # dd("last call " + re)
        return [re]

    def dumps(self):
        return self.report


def mk_request():
    res = requests.get(
        'http://api.pandetrack.online/listall/reports',
    )

    res.raise_for_status()
    data = res.json()
    # dd(res.json())
    # exit(0)
   # print(data["articles"])
    for o in data["articles"]:
        # standerdise the publicationdate
        fd = FuzzDate(o['date_of_publication'])
        o['date_of_publication'] = fd.get_datetime()
        o['p_fuzz'] = fd.get_fuzz_level()

        # parse the report
        o['main_text'] = o['main_text'].replace('\n', '')
        o['report'] = [ReportParser(report).dumps() for report in o['reports']]
        del o['reports']

        print(dumps(o))


if __name__ == "__main__":
    mk_request()
