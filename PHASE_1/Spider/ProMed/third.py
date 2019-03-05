#!python3

import fileinput
import requests 
from cssselect import GenericTranslator, SelectorError
from lxml.etree import fromstring
from json import loads, dumps
import threading
import time
import sys

def get_request(id):
    return requests.get(
        "http://www.promedmail.org/ajax/getPost.php", 
        params = {"alert_id":id, "path_to_main":"../" },
        headers = {
            "Referer": "http://www.promedmail.org/%s" % id
        }
    )


def parse(req):
    el = loads(req.text)
    return el['post']


class Worker(threading.Thread):
    def __init__(self,iteratable, directory):
        threading.Thread.__init__(self)
        self.it = iteratable
        self.dir = directory

    def write_to_file(self, text ):
        file = open(self.dir +self.id, "w+")
        file.write(text)
        file.close()
    
    def run(self):
        while True:
            # rstrip is chmop in perl 
            self.id = next(self.it).rstrip()
            print("reach id %s" % self.id )
            req = get_request(self.id)
            self.write_to_file(parse(req))




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('dir',
        help="Directory to store the posts.",
        type=str,
        default = "posts/"
    )
    parser.add_argument('list',
        help="list of post id",
        type=str,
        default = "all.data"
    )
    args = parser.parse_args()

    # change the input list as an iterator,
    # so I don't need to set up a lock 
    it = iter(fileinput.input(files=args.list))

    workers = []
    #  have a worker thread 
    for i in range(8):
        workers.append ( Worker(it,args.dir))
    for w in workers:
        w.start()
        time.sleep(1)
        
    print("Main thread is exit")