#!/usr/bin/python3
"""
Fetch the disease and sydrome
"""
import fileinput
from json import loads

# import disease
it = iter(fileinput.input(files='ramen.jl'))
# it = iter(fileinput.input(files='output.jl'))

disease_set = set()
syndrome_set = set()

try:
    while True:
        article = loads(next(it))
        # print(article)
        for re in article['report']:
            [disease_set.add(disease) for disease in re['disease']]
            [syndrome_set.add(syndrome) for syndrome in re['syndrome']]

except StopIteration as e:
    pass

print("diseases")
print(disease_set)
print("Syndromes")
print(syndrome_set)
