#!/usr/bin/python3

import requests
from json import dumps
import re
import datetime
# from locationSet import LocationSet
from math import ceil

# http://api.pandetrack.online/listall/reports

# "2019-07-01Txx:xx:xx"

class ReportParser(object):
    def __init__(self, report: dict):
        self.report = report

        temp_list = []
        for t in self.report['reported_events']:
            temp_list += self.parseReportEvent(t)
        self.report['report_events'] = temp_list
        del self.report['reported_events']
        # print(self.dumps())

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
                    ceil(re['number_affected'] / len(ls.location_list))
                tmp_list.append(re_copy)
            return tmp_list

            # print("Dump the error")
            # print(re['location'])
            # print(re['number_affected'])
            # dd(ls.location_list)
        elif ls.location_list:

            # use the first location in the list
            # we expect only one location
            re['location'] = ls.location_list[0]
        else:
            re['location'] = None
        # dd(re)
        return [re]

    def dumps(self):
        print(self.report)
        return self.report




def mk_request(page=0):
    res = requests.get(
        'http://api.pandetrack.online/listall/reports', params={
            'start_date': '1900-01-01T00:00:00',
            'end_date': '2020-01-01T00:00:00',
            'skip': page * 50,
            'limit':  50
        }
    )

    res.raise_for_status()

    # dd(res.json())
    # exit(0)


    for article in res.json():
        # replace the \n to ' '
        # 抓不出来？
        dd(article['articles'])
        exit(0)

        article['main_text'] = article['main_text'].replace('\n', ' ')
        article['report'] =\
            [ReportParser(report).dumps() for report in article['reports']]

        del article['reports']

        print(dumps(article))

    if len(res.json()) != 50:
        exit()


if __name__ == "__main__":
    mk_request(1)
    # i = 0
    # while True:
    #     mk_request(i)
    #     i += 1
