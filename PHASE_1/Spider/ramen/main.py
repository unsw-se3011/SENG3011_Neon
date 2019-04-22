#!/usr/bin/python3

import requests
from json import dumps
import re
import datetime


# https://sneg-ramen.herokuapp.com/api/articles?skip=0&limit=50&start_date=2000-01-01T00%3A00%3A00&end_date=2020-03-31T01%3A56%3A55

# "2019-07-01Txx:xx:xx"
 
 
# a mapping from fuzz level to the fuzz string 
FUZZ_MAP =  {
    6:"Y",
    5:"M",
    4:"D",
    3:"H",
    2:"I",
    1:"S",
    0:"A"
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


class FuzzDate(object):
    def __init__(self, date_str):
        self.date_str = date_str
        res = re.search(r'([0-9]{4})-([0-9x]{1,2})-([0-9x]{1,2})T([0-9x]{1,2}):([0-9x]{1,2}):([0-9x]{1,2})', self.date_str)
        self.date_group = [t for t in res.groups()] 
        
        # count how much field is fuzzy and replace it 
        self.fuzz_count =0
        new_date_group = []
        index =0
        for t in self.date_group:
            if t[0] == 'x':
                self.fuzz_count +=1
                # replace the t = 01
                if index <3:
                    t = "01"
                else:
                    t = "00"
            new_date_group.append(t)

            index +=1
        # replace the new date group 
        self.date_group = [int(t) for t in new_date_group]

    def get_datetime(self):
        # easy python list to function input
        return datetime.datetime(*self.date_group).isoformat()

    def get_fuzz_level(self):
        return FUZZ_MAP[self.fuzz_count]

class ReportParser(object):
    def __init__(self, report:dict):
        self.report = report
        self.report['report_events'] = \
            [self.parseReportEvent(t) for t in self.report['reported_events']]
        print(self.dumps())

    def parseReportEvent(self, re ):
        fd = FuzzDate(re['date'])
        re['start_date'] = fd.get_datetime()
        re['start_date_fuzz'] = fd.get_fuzz_level()
        re['end_date'] = fd.get_datetime()
        re['end_date_fuzz'] = fd.get_fuzz_level()

        re['type'] = EVENT_TYPE_MAP[re['type']]
        return re 

    def dumps (self):
        return dumps(self.report)

def mk_request(page =0 ):
    res = requests.get(
        'https://sneg-ramen.herokuapp.com/api/articles', params={
            'start_date': '1980-01-01T00:00:00',
            'end_date':'2020-01-01T00:00:00',
            'skip': page * 50,
            'limit': (page + 1)* 50
        }
    )
    for article in res.json():
        # replace the \n to ' '
        article['main_text'] = article['main_text'].replace('\n',' ')
        for report in article['reports']:
            ReportParser(report)
                
                
        # print(dumps(report))
        break

if __name__ == "__main__":
    mk_request()