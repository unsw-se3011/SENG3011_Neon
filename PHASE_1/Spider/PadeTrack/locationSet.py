#!/usr/bin/python3

# import city to memory

import csv
from json import dumps
CITIES = []
with open('world-cities.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row = list(row.items())
        CITIES.append({
            'city': row[0][1], 'country': row[1][1], 'state': row[2][1]
        })


class LocationSet(object):
    def __init__(self):
        # atomic location set
        self.location_set = set()
        # list of location object
        self.location_list = []

    def add_place_obj(self, place_obj: dict):
        self.location_list.append(place_obj)
        self.location_set.add(place_obj.get('country'))
        self.location_set.add(place_obj.get('state'))
        self.location_set.add(place_obj.get('city'))

    def find_collapse(self, level, value):
        # find at that level, which is collapse
        for t in self.location_list:
            if t.get(level) == value:
                return t

        # doesn't find the object
        return None

    def add(self, place: str):
        place = place.strip()
        if not place:
            return False

        place_obj = {}
        for city_dict in CITIES:
            low_city = city_dict['city']
            low_country = city_dict['country']
            low_state = city_dict['state']
            place = place.lower()
            low_city = low_city.lower()
            low_country = low_country.lower()
            low_state = low_state.lower()
            # print(low_city)
            # print(place + "!=" + low_city)
            # print(place + "!=" + low_country)
            # print(place + "!=" + low_state)

            # map the place string to place object
            if place in low_city:
                place_obj = {
                    'country': city_dict['country'],
                    'state': city_dict['state'],
                    'city': city_dict['city'],
                    'name': city_dict['city'],
                }
                break
            elif place in low_state:
                place_obj = {
                    'country': city_dict['country'],
                    'state': city_dict['state'],
                    'name': city_dict['state'],
                }
                break
            elif place in low_country:
                place_obj = {
                    'country': city_dict['country'],
                    'name': city_dict['country'],
                }
                break

        # print('imhere with' + place)
        # print(place_obj)
        if 'name' not in place_obj:
            # cloudn't find the place in database
            return False

        if 'city' in place_obj and \
                self.find_collapse('city', place_obj['city']):

            # this object is recorded
            return False
        if 'state' in place_obj and\
                self.find_collapse('state', place_obj['state']):
                # get the collapse object
            col = self.find_collapse('state', place_obj['state'])
            if 'city' not in col:
                # this place is more advanced
                self.location_list = \
                    [t for t in self.location_list if t != col]
        elif self.find_collapse('country', place_obj['country']):
            col = self.find_collapse('country', place_obj['country'])
            if 'city' not in col and 'state' not in col:
                # new place is more advanced
                self.location_list = \
                    [t for t in self.location_list if t != col]

        self.add_place_obj(place_obj)
        return True


if __name__ == "__main__":
    ls = LocationSet()
    ls.add("Brazil")
    ls.add("Brazilia")
    print(ls.location_list)
    ls.add("China")
    ls.add("Shanghai")
    print(ls.location_list)

    ls = LocationSet()
    ls.add("Shanghai")
    ls.add("Zhejiang")
    print(ls.location_list)

    ls = LocationSet()
    ls.add('california')
    ls.add('minnesota')
    ls.add('wisconsin')
    print(ls.location_list)
