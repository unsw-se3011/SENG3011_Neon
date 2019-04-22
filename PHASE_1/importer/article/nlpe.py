#! /usr/bin/python3
from geotext import GeoText
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet, stopwords

from nltk.tokenize import word_tokenize
from nltk import SnowballStemmer
from nltk.collocations import *
from nltk import pos_tag
import nltk
import json
import geograpy
from word2number import w2n
from const import *
import numpy as np


def get_similarity(syndrome_set, atom_syn_arr):
    count = 0
    i = 0
    j = 0
    length = 0
    for j in atom_syn_arr:
        length = length+1
    for i in syndrome_set:
        if i in atom_syn_arr:
            count = count+1
    similarity = round(count/length, 2)
    return similarity


class Nlpe(object):
    def __init__(self, text):
        self.text = text
        self.pos_tags = self.parse_pos_tags()
        self.event_tags = self.noun_text()
        self.country_tags = self.country_text()
        self.people_tags = self.noun_text()
        self.date_tags = self.noun_text()
        self.disease_tags = self.noun_text()

    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        else:
            return None
    # convert all self.text to lowercase, delete stop words

    def parse_pos_tags(self):
        sr = stopwords.words('english')
        # get all lower case clean_tokens
        clean_tokens = list()

        # transfer all cases to lower cases
        text1 = str.lower(self.text)
        # divide text to word with tokenize for lower cases
        mytext = word_tokenize(text1)
        # remove all useless word in all lower cases
        for token in mytext:
            if token not in sr:
                clean_tokens.append(token)

        # store the initial text
        pos_tags = nltk.pos_tag(clean_tokens)
        # print(pos_tags)
        return pos_tags

    # make sure the initial Alphabet of teh country is a Capital letter
    def country_text(self):
        country_tokens = list()
        sr = stopwords.words('english')
        # get all lower case clean_tokens

        # divide text to word with tokenize for lower cases
        mytext = word_tokenize(self.text)
        # remove all useless word in all lower cases
        for token in mytext:
            if token not in sr:
                country_tokens.append(token)

        # store the initial text
        country_tags = nltk.pos_tag(country_tokens)
        # print(country_tags)
        return country_tags

    # change all form of words to nouns
    def noun_text(self):
        stem_tokens = list()
        lemmas_sent = []
        sr = stopwords.words('english')
        # transfer all cases to lower cases
        text1 = str.lower(self.text)
        # divide text to word with tokenize for lower cases
        mytext = word_tokenize(text1)
        tagged_sent = pos_tag(mytext)
        wnl = WordNetLemmatizer()

        for tag in tagged_sent:
            wordnet_pos = self.get_wordnet_pos(tag[1]) or wordnet.NOUN
            lemmas_sent.append(wnl.lemmatize(tag[0], pos='n'))
        # remove all useless word in all lower cases
        for token in lemmas_sent:
            if token not in sr:
                stem_tokens.append(token)

        # store the initial text
        pos_tags = nltk.pos_tag(lemmas_sent)
        # print(pos_tags)
        return pos_tags

    def get_syndrome(self):
        # syndrome
        # syndrome match
        syndrome_set = set()
        DONE_SYNDROME = set()
        #syndrome2 = list()
        for word, pos in self.pos_tags:
            #print(word, pos)
            if word in MATCH_SYNDROME:
                syndrome_set.add(word)
        for keys in SYNDROME:
            # improve the get_similarity function later
            similarity = get_similarity(syndrome_set, SYNDROME[keys])
            print(similarity)
        # get syndrome the similarity more then 0.75
            if similarity > 0.1:
                DONE_SYNDROME.add(keys)
        return [t for t in DONE_SYNDROME]

    def get_disease(self):
        # disease match
        disease1 = set()
        for word, pos in self.disease_tags:
            if word in DISEASE:
                disease1.add(word)
            if word in MATCH_DISEASE:
                disease1.add(MATCH_DISEASE[word])
        return [t for t in disease1]

    def get_event(self):
        # event_type match
        event_type_set = set()
        for word, pos in self.event_tags:
            if word in EVENT_TYPE:
                event_type_set.add(word)
        # from set to array
        return [t for t in event_type_set]

    def get_country(self):
        # this function can ONLY match the country name but not including city, state etc.
        # Country
        country = set()
        for word, pos in self.country_tags:
            if word in COUNTRY_LIST:
                country.add(word)
        return [t for t in country]
    # try to match the places under the country

    def get_places(self):
        """"
        Why i need to open the dataset every time i parse this  
        """
        text_input = self.text
        location_dict = {}
        places = geograpy.get_place_context(text=text_input)

        for city_dict in CITIES:
            if city_dict['city'] in places.countries:
                location_dict[city_dict['city']] = {
                    'country': city_dict['country'],
                    'state': city_dict['state'],
                    'city': city_dict['city'],
                    'name': city_dict['city'],
                }
            if city_dict['state'] in places.countries:
                location_dict[city_dict['state']] = {
                    'state': city_dict['state'],
                    'country': city_dict['country'],
                    'name': city_dict['state'],
                }
            if city_dict['country'] in places.countries:
                location_dict[city_dict['country']] = {
                    'country': city_dict['country'],
                    'name': city_dict['country'],
                }
        return list(location_dict.values())

    # this function is wrong, this function only works for one (the first) article
    def get_people(self):
        # effect_number (need improve after)
        # this grammar is used to match people
        grammar = "NP: {<CD><NNS>}"
        cp = nltk.RegexpParser(grammar)
        tree1 = cp.parse(self.people_tags)
        people = list()
        for subtree1 in tree1.subtrees():
            if subtree1.label() == 'NP':
                for word, pos in subtree1.leaves():
                    if (pos == 'CD'):
                        people.append(word)
        people = [t.replace(',', '') for t in people]
        try:
            people = [w2n.word_to_num(t) for t in people]
        except ValueError as e:
            return []
        return people

    # this function is wrong, this function only works for one (the first) article
    def get_date(self):
        # date
        # one of type to match the date need improve after
        # this grammar is used to match date
        grammar = "NP: {<JJ><CD>(<TO><VB><CD>)?}"
        cp = nltk.RegexpParser(grammar)
        tree = cp.parse(self.date_tags)
        date = list()
        date1 = list()
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                for word, pos in subtree.leaves():
                    date.append(word)
        date = ' '.join(date)
        date1.append(date)
        return date1
