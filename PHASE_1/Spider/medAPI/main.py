#!/usr/bin/python3

import requests
import json
from json import dumps
import re
import datetime
from locationSet import LocationSet
from math import ceil

# https://med-api-seng3011-csb.herokuapp.com/#/Articles%20on%20known%20outbreaks/CurrentOutbreakData

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


# Two not support disease
DISEASE_MAP = {
    'rubella': 'rubella',
    'measles': 'measles',
    'lassa fever': 'lassa fever',
    'rabies': 'rabies',
    'ebola': 'ebola haemorrhagic fever',
    'h7n9': 'influenza a/h7n9',
    'typhoid fever': 'thypoid fever',
    'unknown': 'unknown',
    'rift valley fever': 'rift valley fever',
    'polio': 'poliomyelitis',
    'brucellosis': 'brucellosis',
    'cholera': 'cholera',
    'monkeypox': 'monkeypox',
    'hepatitis a': 'hepatitis a',
    'hantavirus': 'hantavirus',
    'salmonella': 'salmonellosis',
    'psittacosis': None,
    'yellow fever': 'yellow fever',
    'leptospirosis': None
}


def dd(str):
    print(str)
    exit(0)

CLEANRX = re.compile('<.*?>')
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANRX, '', raw_html)
  return cleantext



class FuzzDate(object):
    def __init__(self, date_str):
        self.date_str = date_str + "Txx:xx:xx"
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

        for t in temp_list:
            if not t['location']:
                del t['location']

        self.report['report_events'] = temp_list

        # remap the disease and deprecate it's syndrome
        self.report['syndrome'] = []
        # map and remove empty
        self.report['disease'] = \
            [DISEASE_MAP[d] for d in self.report['disease']]
        self.report['disease'] = \
            [t for t in self.report['disease'] if t]

        del self.report['reported_events']
        # print(dumps(temp_list))

    def parseReportEvent(self, re):
        fd = FuzzDate(re['date'])

        # dd(fd.get_fuzz_level())
        re['start_date'] = fd.get_datetime()
        re['sd_fuzz'] = fd.get_fuzz_level()
        re['end_date'] = fd.get_datetime()
        re['ed_fuzz'] = fd.get_fuzz_level()
        # we don't need the old date anymore
        del re['date']

        re['e_type'] = EVENT_TYPE_MAP[re['type']]

        ls = LocationSet()
        # ramen have two level location, both name location
        [ls.add(l['location']) for l in re['location']]
        # print("Length of location   " + str(len(ls.location_list)))

        # print location list
        # print([l['location'] for l in re['location']])
        # print(ls.location_list)
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

            print("Dump the error")
            print(re['location'])
            print(re['number_affected'])
            dd(ls.location_list)
        elif ls.location_list:

            # use the first location in the list
            # we expect only one location
            re['location'] = ls.location_list[0]
        else:
            re['location'] = None
        #    dd("last call " + re)

        return [re]

    def dumps(self):
        return self.report


def mk_request(page):
    res = requests.get(
        'https://med-api-seng3011-csb.herokuapp.com/articles', params={
            'startDate': '1980-01-01T00:00:00',
            'endDate': '2020-04-23T00:00:00',
            'limit':  1000
        }
    )

    res.raise_for_status()
    for article in res.json():
        # replace the \n to ' '
        # print("NEXT ONE  ---------------")

        if(article['main_text']) is None:
            continue

        del article['ArticleID']
        article['date_of_publication'] += "T00:00:00"
        article['main_text'] = article['main_text'].replace('\n', ' ')
        # clean the html tags 
        article['main_text'] = cleanhtml(article['main_text'])
        article['headline'] = cleanhtml(article['headline'])
        

        del article['reports'][0]['ReportID']
        del article['reports'][0]['comment']
        del article['reports'][0]['ArticleID']
        article['report'] =\
            [ReportParser(report).dumps() for report in article['reports']]
        del article['reports']

        print(dumps(article))
    if len(res.json()) != 50:
        exit()


if __name__ == "__main__":
    mk_request(0)
