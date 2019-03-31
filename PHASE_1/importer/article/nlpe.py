#! /usr/bin/python3
from geotext import GeoText
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet,stopwords

from nltk.tokenize import word_tokenize
from nltk import SnowballStemmer
from nltk.collocations import *
from nltk import pos_tag
import nltk
from nltk.stem import WordNetLemmatizer
import json
import geograpy
import csv
# text = ["The Pat Walker Health Center at the University of Arkansas issued a campus health advisory after the Arkansas Department of Health (ADH) identified three confirmed cases and one suspected case of mumps on the University of Arkansas (UA) at Fayetteville campus in the last few weeks. Infographic aimed at college students depicting symptoms of mumps and steps they can take to protect themselves. Those who may have been exposed have receive additional communication and information from Pat Walker Health Center. ADH is working closely with the UA Fayetteville campus to alert students and staff who may have been in close contact with the confirmed cases. These close contacts, as well as anyone with an MMR vaccine exemption on campus, are encouraged to seek vaccination. MMR vaccines are available at the Washington County Local Health Unit, and are also available at many doctors\u2019 offices or local pharmacies. Vaccines are also available to the UA Fayetteville community at the Pat Walker Health Center on campus From August 2016 to August 2017, Arkansas experienced the second-largest mumps outbreak in the United States in the last 30 years. Nearly 3,000 mumps cases related to the outbreak during that period were identified. Texas measles case count at eight as of mid-February According to the Centers for Disease Control and Prevention (CDC), mumps is a viral illness that is transmitted by direct contact with respiratory droplets or saliva from an infected person. It is best known for painful, swollen salivary glands that show up as puffy cheeks and swollen jaw. Boys may also have painful, swollen testicles. In some of these cases, fertility can be affected. Other symptoms include fever, headache, muscles aches, tiredness, and loss of appetite. There is no treatment, and symptoms usually resolve themselves within a few weeks. Mumps is usually a mild disease in children, but adults may have more serious disease with complications. Complications can include deafness and encephalitis. Encephalitis is inflammation of the brain. The MMR vaccine is safe and effective. Two doses of MMR vaccine are 88 percent effective in preventing mumps. It is a live virus vaccine and is not recommended for pregnant women or patients with a weakened immune system. Sydney Adults born before 1957 are generally considered to be immune to mumps and do not need to receive the MMR vaccine."]

class Nlpe(object):
    def __init__(self, text):
        self.text = text

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
    def initial_text(self):
        sr = stopwords.words('english')
        #get all lower case clean_tokens
        clean_tokens = list()

        # transfer all cases to lower cases
        text1 = str.lower(self.text)
        #divide text to word with tokenize for lower cases
        mytext = word_tokenize(text1)
        # remove all useless word in all lower cases
        for token in mytext:
            if token not in sr:
                clean_tokens.append(token)

        #store the initial text
        pos_tags = nltk.pos_tag(clean_tokens)
        #print(pos_tags)
        return pos_tags

    # make sure the initial Alphabet of teh country is a Capital letter 
    def country_text(self):
        country_tokens = list()
        sr = stopwords.words('english')
        #get all lower case clean_tokens

        #divide text to word with tokenize for lower cases
        mytext = word_tokenize(self.text)
        # remove all useless word in all lower cases
        for token in mytext:
            if token not in sr:
                country_tokens.append(token)

        #store the initial text
        country_tags = nltk.pos_tag(country_tokens)
        #print(country_tags)
        return country_tags

    # change all form of words to nouns 
    def noun_text(self):
        stem_tokens = list()
        lemmas_sent = []
        sr = stopwords.words('english')
        # transfer all cases to lower cases
        text1 = str.lower(self.text)
        #divide text to word with tokenize for lower cases
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

        #store the initial text
        pos_tags = nltk.pos_tag(lemmas_sent)
        #print(pos_tags)
        return pos_tags



    def get_syndrome(self, pos_tags):
        # syndrome
        syndrome = ['encephalitis', 'haemorrhagic fever',
                    'acute flacid paralysis', 'acute gastroenteritis', 'acute respiratory syndrome', 'influenza-like illness', 'acute fever and rash', 'fever of unknown origin', 'meningitis']
        # syndrome match
        syndrome1 = list()
        #syndrome2 = list()
        for word, pos in pos_tags:
            #print(word, pos)
            for i in syndrome:
                # print(i)
                if (word == i):
                    if word not in syndrome1:
                        syndrome1.append(word)
        return syndrome1


    def get_disease(self, pos_tags):
        # disease
        disease = ['unknown','other','anthrax cutaneous','anthrax gastrointestinous','anthrax inhalation','botulism','brucellosis','chikungunya','cholera','cryptococcosis','cryptosporidiosis','crimean-congo haemorrhagic fever','dengue','diphteria','ebola haemorrhagic fever','ehec (e.coli)','enterovirus 71 infection','influenza a/h5n1','influenza a/h7n9','influenza a/h9n2','influenza a/h1n1','influenza a/h1n2','influenza a/h3n5','influenza a/h3n2','influenza a/h2n2','hand, foot and mouth disease','hantavirus','hepatitis a','hepatitis b','hepatitis c','hepatitis d','hepatitis e','histoplasmosis','hiv/aids','lassa fever','malaria','marburg virus disease','measles','mers-cov','mumps','nipah virus','norovirus infection','pertussis','plague','pneumococcus pneumonia','poliomyelitis','q fever','rabies','rift valley fever','rotavirus infection','rubella','salmonellosis','sars','shigellosis','smallpox','staphylococcal enterotoxin b','thypoid fever','tuberculosis','tularemia','vaccinia and cowpox','varicella','west nile virus','yellow fever','yersiniosis','zika','legionares','listeriosis','monkeypox']
        # disease match
        disease1 = list()
        for word, pos in pos_tags:
            for i in disease:
                # print(i)
                if (word == i):
                    if word not in disease1:
                        disease1.append(word)
        return disease1

    def get_event(self, pos_tags):
        # event_type
        event_type = ['presence', 'death', 'infected', 'hospitalised', 'recovered']

        # event_type match
        event_type1 = list()
        for word, pos in pos_tags:
            for i in event_type:
                # print(i)
                if (word == i):
                    if word not in event_type1:
                        event_type1.append(word)
        return event_type1

    def get_country(self, pos_tags):
        # this function can ONLY match the country name but not including city, state etc.
        # countries
        country_list = ['Afghanistan','Albania','Algeria','Andorra','Angola','Anguilla','Antigua &amp; Barbuda','Argentina','Armenia','Aruba','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia &amp; Herzegovina','Botswana','Brazil','British Virgin Islands','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Cape Verde','Cayman Islands','Chad','Chile','China','Colombia','Congo','Cook Islands','Costa Rica','Cote D Ivoire','Croatia','Cruise Ship','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Estonia','Ethiopia','Falkland Islands','Faroe Islands','Fiji','Finland','France','French Polynesia','French West Indies','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guam','Guatemala','Guernsey','Guinea','Guinea Bissau','Guyana','Haiti','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Jersey','Jordan','Kazakhstan','Kenya','Kuwait','Kyrgyz Republic','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Mauritania','Mauritius','Mexico','Moldova','Monaco','Mongolia','Montenegro','Montserrat','Morocco','Mozambique','Namibia','Nepal','Netherlands','Netherlands Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palestine','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania','Russia','Rwanda','Saint Pierre &amp; Miquelon','Samoa','San Marino','Satellite','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','South Africa','South Korea','Spain','Sri Lanka','St Kitts &amp; Nevis','St Lucia','St Vincent','St. Lucia','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Timor LEste','Togo','Tonga','Trinidad &amp; Tobago','Tunisia','Turkey','Turkmenistan','Turks &amp; Caicos','Uganda','Ukraine','United Arab Emirates','United Kingdom','Uruguay','Uzbekistan','Venezuela','Vietnam','Virgin Islands (US)','Yemen','Zambia','Zimbabwe']
        # Country
        country = list()
        for word, pos in pos_tags:
            for i in country_list:
                if(word == i):
                    if word not in country:
                        country.append(word)
        return country
    #try to match the places under the country
    def get_places(self):
        text_input = self.text
        places1=list()
        places = geograpy.get_place_context(text=text_input)
        with open('world-cities.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for i in places.countries:
                    if row['name'] == i:
                        if i not in places1:
                            places1.append(i)
                    if row['country'] == i:
                        if i not in places1:
                            places1.append(i)
        return places1

    # this function is wrong, this function only works for one (the first) article 
    def get_people(self, pos_tags):
        #effect_number (need improve after)
        grammar = "NP: {<CD><NNS>}"               # this grammar is used to match people 
        cp = nltk.RegexpParser(grammar)
        tree1 = cp.parse(pos_tags)
        people = list()
        for subtree1 in tree1.subtrees():
            if subtree1.label() == 'NP':
                for word, pos in subtree1.leaves():
                    if (pos == 'CD'):
                        people.append(word)
        return people

    # this function is wrong, this function only works for one (the first) article
    def get_date(self, pos_tags):
        #date
        #one of type to match the date need improve after
        # this grammar is used to match date
        grammar = "NP: {<JJ><CD><TO><VB><CD>}"
        cp = nltk.RegexpParser(grammar)
        tree = cp.parse(pos_tags)
        date = list()
        date1 = list()
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                for word, pos in subtree.leaves():
                    date.append(word)
        date = ' '.join(date)
        date1.append(date)
        return date1
