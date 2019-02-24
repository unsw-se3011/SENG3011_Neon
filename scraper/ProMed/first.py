#!python3
from json import loads, dumps
import requests 
import re

def get_request(end_day, feed_id):
    # ?edate=2019-01-24&return_map=0&feed_id=15&seltype=latest
    return  requests.get('http://www.promedmail.org/ajax/getPosts.php', params = {
        "edate":end_day,
        "feed_id": feed_id,
        "return_map":0,
        "seltype":"latest"
    })

class YearMonth(object):
    def __init__(self, year=2019, month=2, day=24):
        self.year = year
        self.month = month
        self.day = day
    def decrease(self):
        self.month -= 1 
        if self.month ==0:
            self.month = 12
            self.year -= 1 
    def __str__(self):
        return "%s-%s-%s" % (self.year,self.month,self.day)

# regular expression to find all the ids 
# id is each post 
pattern = re.compile(r"\"id(\d+)\"")

def parse(text):
    return pattern.findall(text)

# initial a self construct object 
ym = YearMonth()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('max_id',
        help="The maximun id last time left over.",
        type=int,
        default = 0
    )
    parser.add_argument('feed',
        help="The feed id we need to scrap.",
        type=int
    )
    # dictionary of commandline you input
    args = parser.parse_args()
    

    # could be larger than this 
    pre_min = 16061615
    while True:
        r = get_request(ym,args.feed)
        # remove the uneccessary \ from json encoding
        list = loads(r.text)
        # we don't need next and previos from return 
        # and after parse, the result will be a string of ids array
        result = parse(list['listview'])
        
        for i in result:
            # an o(n) solution, instad of sorting it 
            if int(i) < pre_min:
                print(int(i))
            if int(i) < args.max_id:
                exit

        # update the pre min
        pre_min = int(result[-1])
        # decrement the month year combo 
        ym.decrease()