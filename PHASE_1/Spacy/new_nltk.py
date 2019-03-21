#! /usr/bin/python3
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import SnowballStemmer
from nltk.collocations import *
import nltk
import re
TEXTS = [
    "The Pat Walker Health Center at the University of Arkansas issued a campus health advisory after the Arkansas Department of Health (ADH) identified three confirmed cases and one suspected case of mumps on the University of Arkansas (UA) at Fayetteville campus in the last few weeks.",
    "Infographic aimed at college students depicting symptoms of mumps and steps they can take to protect themselves.",
    "Those who may have been exposed have receive additional communication and information from Pat Walker Health Center.",
    "2019 ADH is working closely with the UA Fayetteville campus to alert students and staff who may have been in close contact with the confirmed cases.",
    "These close contacts, as well as anyone with an MMR vaccine exemption on campus, are encouraged to seek vaccination.",
    "MMR vaccines are available at the Washington County Local Health Unit, and are also available at many doctors\u2019 offices or local pharmacies.",
    "Vaccines are also available to the UA Fayetteville community at the Pat Walker Health Center on campus From August 2016 to August 2017, Arkansas experienced the second-largest mumps outbreak in the United States in the last 30 years.",
    "Nearly 3,000 mumps cases related to the outbreak during that period were identified.",
    "Texas measles case count at eight as of mid-February According to the Centers for Disease Control and Prevention (CDC), mumps is a viral illness that is transmitted by direct contact with respiratory droplets or saliva from an infected person.",
    "It is best known for painful, swollen salivary glands that show up as puffy cheeks and swollen jaw. Boys may also have painful, swollen testicles.",
    "In some of death these cases, fertility can be affected. Other symptoms include fever, headache, muscles aches, tiredness, and loss of appetite.",
    "There is no treatment, and symptoms usually resolve themselves within a few weeks.",
    "Mumps is usually a mild disease in children, unknown but adults may have more serious disease with complications.",
    "Complications can include deafness and encephalitis.",
    "Encephalitis is inflammation of the brain meningitis acute gastroenteritis.",

]

# syndrome
syndrome = ['encephalitis', 'haemorrhagic fever',
            'acute flacid paralysis', 'acute gastroenteritis', 'acute respiratory syndrome', 'influenza-like illness', 'acute fever and rash', 'fever of unknown origin', 'meningitis']

# disease
disease = ['unknown','other','anthrax cutaneous','anthrax gastrointestinous','anthrax inhalation','botulism','brucellosis','chikungunya','cholera','cryptococcosis','cryptosporidiosis','crimean-congo haemorrhagic fever','dengue','diphteria','ebola haemorrhagic fever','ehec (e.coli)','enterovirus 71 infection','influenza a/h5n1','influenza a/h7n9','influenza a/h9n2','influenza a/h1n1','influenza a/h1n2','influenza a/h3n5','influenza a/h3n2','influenza a/h2n2','hand, foot and mouth disease','hantavirus','hepatitis a','hepatitis b','hepatitis c','hepatitis d','hepatitis e','histoplasmosis','hiv/aids','lassa fever','malaria','marburg virus disease','measles','mers-cov','mumps','nipah virus','norovirus infection','pertussis','plague','pneumococcus pneumonia','poliomyelitis','q fever','rabies','rift valley fever','rotavirus infection','rubella','salmonellosis','sars','shigellosis','smallpox','staphylococcal enterotoxin b','thypoid fever','tuberculosis','tularemia','vaccinia and cowpox','varicella','west nile virus','yellow fever','yersiniosis','zika','legionares','listeriosis','monkeypox']

# event_type
event_type = ['presence','death','infected','hospitalised','recovered']
clean_tokens = list()

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# remove all useless word
sr = stopwords.words('english')
for text in TEXTS:

    # transfer all cases to lower cases
    text1 = str.lower(text)

    #divide text to word with tokenize
    mytext = word_tokenize(text1)

   # finder = BigramCollocationFinder.from_words(mytext)
   # scored = finder.scor e_ngrams(bigramgram_measures.raw_freq)
   # sorted(bigram for bigram,score in scored)
   # print(scored)
    # remove all useless word
    for token in mytext:
        if token not in sr:
            clean_tokens.append(token)

#store the initial text
pos_tags = nltk.pos_tag(clean_tokens)

# syndrome match
for word, pos in pos_tags:                  
    for i in syndrome:
        # print(i)
        if (word == i):
            print(word, pos)

# disease match
for word, pos in pos_tags:  
    for i in disease:
        # print(i)
        if (word == i):
            print(word, pos)

# event_type match
for word, pos in pos_tags:  
    for i in event_type:
        # print(i)
        if (word == i):
            print(word, pos)

for word, pos in pos_tags:
    if(pos == 'CD'):
        print(word)
        
