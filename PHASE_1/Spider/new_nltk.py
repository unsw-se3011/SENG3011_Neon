#! /usr/bin/python3
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet,stopwords

from nltk.tokenize import word_tokenize
from nltk import SnowballStemmer
from nltk.collocations import *
from nltk import pos_tag
import nltk
from nltk.stem import WordNetLemmatizer
import json

def get_wordnet_pos(tag):
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

# convert all texts to lowercase, delete stop words 
def initial_text(TEXTS):
    sr = stopwords.words('english')
    #get all lower case clean_tokens
    clean_tokens = list()

    # transfer all cases to lower cases
    text1 = str.lower(TEXTS)
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
def country_text(TEXTS):
    country_tokens = list()
    sr = stopwords.words('english')
    #get all lower case clean_tokens

    #divide text to word with tokenize for lower cases
    mytext = word_tokenize(TEXTS)
    # remove all useless word in all lower cases
    for token in mytext:
        if token not in sr:
            country_tokens.append(token)

    #store the initial text
    country_tags = nltk.pos_tag(country_tokens)
    #print(country_tags)
    return country_tags

# change all form of words to nouns 
def noun_text(TEXTS):
    stem_tokens = list()
    lemmas_sent = []
    sr = stopwords.words('english')
    # transfer all cases to lower cases
    text1 = str.lower(TEXTS)
    #divide text to word with tokenize for lower cases
    mytext = word_tokenize(text1)
    tagged_sent = pos_tag(mytext)
    wnl = WordNetLemmatizer()

    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos='n'))
    # remove all useless word in all lower cases
    for token in lemmas_sent:
        if token not in sr:
            stem_tokens.append(token)

    #store the initial text
    pos_tags = nltk.pos_tag(lemmas_sent)
    #print(pos_tags)
    return pos_tags


# pos_tags = initial_text(TEXTS)
# event_tags = noun_text(TEXTS)
# country_tags = country_text(TEXTS)
# people_tags = noun_text(TEXTS)
# date_tags = noun_text(TEXTS)

def match_syndrome(pos_tags):
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


def match_disease(pos_tags):
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

def match_event(pos_tags):
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

# this function can ONLY match the country name but not including city, state etc.
def match_country(pos_tags):
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

# this function is wrong, this function only works for one (the first) article 
def match_people(pos_tags):
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
def match_date(pos_tags):
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

# syndrome = match_syndrome(pos_tags)
# disease = match_disease(pos_tags)
# event_type = match_event(event_tags)
# country = match_country(country_tags)
# people = match_people(people_tags)
# date = match_date(date_tags)

# report = list()
# report.append(people)
# report.append(date)
# report.append(syndrome)
# report.append(disease)
# report.append(country)
# report.append(event_type)
# print(json.dumps(report, sort_keys=True,
#            indent=4, separators=(',', ': ')))

# tokenized_sentences = [nltk.word_tokenize(text) for text in TEXTS]
# # tag sentences and use nltk's Named Entity Chunker
# tagged_sentences = [nltk.pos_tag(text) for text in tokenized_sentences]
# ne_chunked_sents = [nltk.ne_chunk(tagged) for tagged in tagged_sentences]
# # extract all named entities
# named_entities = []
# for ne_tagged_sentence in ne_chunked_sents:
#    for tagged_tree in ne_tagged_sentence:
#        # extract only chunks having NE labels
#        if hasattr(tagged_tree, 'label'):
#            entity_name = ' '.join(c[0]
#                                   for c in tagged_tree.leaves())  # get NE name
#            entity_type = tagged_tree.label()  # get NE category
#            named_entities.append((entity_name, entity_type))
#            # get unique named entities
#            named_entities = list(set(named_entities))

# # store named entities in a data frame
# entity_frame = pd.DataFrame(named_entities, columns=[
#                             'Entity Name', 'Entity Type'])
# # display results
# print(entity_frame)
