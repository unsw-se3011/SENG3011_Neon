from nltk import pos_tag
from nltk.corpus import wordnet, stopwords
from nltk.stem import WordNetLemmatizer
import csv

# constants
SYNDROME = [
    'encephalitis', 'haemorrhagic fever', 'acute flacid paralysis', 'acute gastroenteritis', 'acute respiratory syndrome', 'influenza-like illness', 'acute fever and rash', 'fever of unknown origin', 'meningitis'
]

DISEASE = [
    'unknown', 'other', 'anthrax cutaneous', 'anthrax gastrointestinous', 'anthrax inhalation', 'botulism', 'brucellosis', 'chikungunya', 'cholera', 'cryptococcosis', 'cryptosporidiosis', 'crimean-congo haemorrhagic fever', 'dengue', 'diphteria', 'ebola haemorrhagic fever', 'ehec (e.coli)', 'enterovirus 71 infection', 'influenza a/h5n1', 'influenza a/h7n9', 'influenza a/h9n2', 'influenza a/h1n1', 'influenza a/h1n2', 'influenza a/h3n5', 'influenza a/h3n2', 'influenza a/h2n2', 'hand, foot and mouth disease', 'hantavirus', 'hepatitis a', 'hepatitis b', 'hepatitis c', 'hepatitis d', 'hepatitis e', 'histoplasmosis', 'hiv/aids', 'lassa fever', 'malaria', 'marburg virus disease', 'measles', 'mers-cov', 'mumps', 'nipah virus', 'norovirus infection', 'pertussis', 'plague', 'pneumococcus pneumonia', 'poliomyelitis', 'q fever', 'rabies', 'rift valley fever', 'rotavirus infection', 'rubella', 'salmonellosis', 'sars', 'shigellosis', 'smallpox', 'staphylococcal enterotoxin b', 'thypoid fever', 'tuberculosis', 'tularemia', 'vaccinia and cowpox', 'varicella', 'west nile virus', 'yellow fever', 'yersiniosis', 'zika', 'legionares', 'listeriosis', 'monkeypox'
]

EVENT_TYPE = ['presence', 'death', 'infected', 'hospitalised', 'recovered']

COUNTRY_LIST = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua &amp; Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia &amp; Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote D Ivoire', 'Croatia', 'Cruise Ship', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'French West Indies', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Pierre &amp; Miquelon', 'Samoa', 'San Marino', 'Satellite', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'St Kitts &amp; Nevis', 'St Lucia', 'St Vincent', 'St. Lucia', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor LEste', 'Togo', 'Tonga', 'Trinidad &amp; Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks &amp; Caicos', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Virgin Islands (US)', 'Yemen', 'Zambia', 'Zimbabwe'
]

DISEASE_NOUN = {
    "unknown": "unknown",
    "other": "other",
    "cutaneous": "anthrax cutaneous",
    "gastrointestinous": "anthrax gastrointestinous",
    "inhalation": "anthrax inhalation",
    "botulism": "botulism",
    "Food-borne": "botulism",
    "Intestinal": "botulism",
    "brucellosis": "brucellosis",
    "Brucella": "brucellosis",
    "chikungunya": "chikungunya",
    "cholera": "cholera",
    "cryptococcosis": "cryptococcosis",
    "cryptosporidiosis": "cryptosporidiosis",
    "crimean-congo": "crimean-congo haemorrhagic fever",
    "dengue": "dengue",
    "diphtheria": "diphteria",
    "EVD": "ebola haemorrhagic fever",
    "ebola": "ebola haemorrhagic fever",
    "EHEC": "ehec (e.coli)",
    "Escherichia": "ehec (e.coli)",
    "e.coli": "ehec (e.coli)",
    "EV71": "enterovirus 71 infection",
    "enterovirus": "enterovirus 71 infection",
    "a/h5n1": "influenza a/h5n1",
    "a/h7n9": "influenza a/h7n9",
    "a/h9n2": "influenza a/h9n2",
    "a/h1n1": "influenza a/h1n1",
    "a/h1n2": "influenza a/h1n2",
    "a/h3n5": "influenza a/h3n5",
    "a/h3n2": "influenza a/h3n2",
    "a/h2n2": "influenza a/h2n2",
    "HFMD": "hand, foot and mouth disease",
    "HPS": "hantavirus",
    "hantavirus": "hantavirus",
    # "hepatitis a":"hepatitis",
    # "hepatitis b":"hepatitis",
    # "hepatitis c":"hepatitis",
    # "hepatitis d":"hepatitis",
    # "hepatitis e":"hepatitis",
    "Histoplasma": "histoplasmosis",
    "reticuloendotheliosis": "histoplasmosis",
    "histoplasmosis": "histoplasmosis",
    "HIV": "hiv/aids",
    "AIDS": "hiv/aids",
    "lassa": "lassa fever",
    "Malaria": "malaria",
    "MVD": "marburg virus disease",
    "MARV": "marburg virus disease",
    "RAVV": "marburg virus disease",
    "measles": "measles",
    "MERS": "mers-cov",
    "MERS-coronavirus": "mers-cov",
    "mumps": "mumps",
    "RNA": "nipah virus",
    "Henipavirus": "nipah virus",
    "Noroviruses": "norovirus infection",
    "Norwalk-like": "norovirus infection",
    "Pertussis": "pertussis",
    "whoop": "pertussis",
    "plague": "plague",
    "Yersinia": "plague",
    "Streptococcus": "pneumococcus pneumonia",
    "Pneumococcal": "pneumococcus pneumonia",
    "polio": "poliomyelitis",
    "poliomyelitis": "poliomyelitis",
    # "Coxiella": "q fever",
    "rabies": "rabies",
    "RVF": "rift valley fever",
    "Rotavirus": "rotavirus infection",
    "rubella": "rubella",
    "salmonellosis": "salmonellosis",
    "Salmonella": "salmonellosis",
    "SARS": "sars",
    "Shigella": "shigellosis",
    "Variola": "smallpox",
    "smallpox": "smallpox",
    "SEB": "staphylococcal enterotoxin b",
    "enteric": "thypoid fever",
    "Salmonella typhi": "thypoid fever",
    "TB": "tuberculosis",
    "MTB": "tuberculosis",
    "Tularemia": "tularemia",
    "tularensis": "tularemia",
    "cowpox": "vaccinia and cowpox",
    "vaccinia": "vaccinia and cowpox",
    "varicella": "varicella",
    "Chickenpox": "varicella",
    "VZV": "varicella",
    "WNV": "west nile virus",
    "EYE": "yellow fever",
    # "Yersinia": "yersiniosis",
    "yersiniosis": "yersiniosis",
    "zika": "zika",
    "Legionella": "legionares",
    "legionares": "legionares",
    "Listeria": "listeriosis",
    "monkeypox": "monkeypox"
}


# Not sure how  to use this fun in class, re-define
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


#import disease
KEY_DISEASE = []
VALUE_DISEASE = []
for keys in DISEASE_NOUN:
    KEY_DISEASE.append(keys)
    VALUE_DISEASE.append(DISEASE_NOUN[keys])
tagged_sent = pos_tag(KEY_DISEASE)
WNL = WordNetLemmatizer()
LEMMAS_DISEASE = []
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
    LEMMAS_DISEASE.append(WNL.lemmatize(tag[0], pos=wordnet_pos))
# get all noun_keys into new map with value
MATCH_DISEASE = dict(zip(LEMMAS_DISEASE, VALUE_DISEASE))

# import city to memory
CITIES = []
with open('world-cities.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row = list(row.items())
        CITIES.append({
            'city': row[0][1], 'country': row[1][1], 'state': row[2][1]
        })

"""
Syndrome parser support 
"""
ATOMIC_SYNDROME = {
    'Encephalitis': 'encephalitis',
    'haemorrhagic': 'haemorrhagic fever',
    'AFP': 'acute flacid paralysis',
    'gastroenteritis': 'acute gastroenteritis',
    'SARS': 'acute respiratory syndrome',
    'ILI': 'influenza-like illness',
    'AFR': 'acute fever and rash',
    'FUO': 'fever of unknown origin',
    'meningitis': 'meningitis',
    'Headache': 'Headache',
    'Fever': 'Fever',
    'muscles': 'Aches in muscles',
    'weakness': 'weakness',
    'Chills': 'Chills',
    'sore': 'sore throat',
    'appetite': 'loss of appetite',
    'rash': 'rash',
    'diarrhoea': 'diarrhoea',
    'paralysis': 'paralysis',
    'Nausea': 'Nausea',
    # 'vomiting': 'Nausea, vomiting or both',
    'Confusion': 'Confusion',
    'Malaise': 'Malaise',
    'nausea': 'nausea',
    'breathlessness': 'breathlessness',
    'fretfulness': 'fretfulness',
    'flu-like': 'flu-like syndrome',
    'vomiting': 'vomiting',
    'photophobia': 'photophobia'
}

KEY_SYNDROME = []
VALUE_SYNDROME = []
for keys in ATOMIC_SYNDROME:
    KEY_SYNDROME.append(keys)
    VALUE_SYNDROME.append(ATOMIC_SYNDROME[keys])
tagged_sent = pos_tag(KEY_SYNDROME)
WNL = WordNetLemmatizer()
LEMMAS_SYNDROME = []
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
    LEMMAS_SYNDROME.append(WNL.lemmatize(tag[0], pos=wordnet_pos))
# get all noun_keys into new map with value
MATCH_SYNDROME = dict(zip(LEMMAS_SYNDROME, VALUE_SYNDROME))
#

SYNDROME = {
    'encephalitis': [
        'encephalitis',
        'Headache',
        'Fever'
        'Aches in muscles',
        'weakness'
    ],
    'haemorrhagic fever': [
        'haemorrhagic fever',
        'Fever',
        'Chills',
        'sore throat',
        'loss of appetite'
        'rash',
        'muscle pains',
        'diarrhoea'
    ],
    'acute flacid paralysis': [
        'acute flacid paralysis',
        'weakness',
        'paralysis'
    ],
    'acute gastroenteritis': [
        'acute gastroenteritis',
        'Abdominal cramps and pain',
        'Nausea',
        'vomiting',
        'Low-grade fever'
    ],
    'acute respiratory syndrome': [
        'acute respiratory syndrome',
        'Chills',
        'Stiff muscles',
        'Body aches and pains',
        'Skin rash',
        'Confusion',
        'Malaise',
        'breathlessness'
    ],
    'influenza-like illness': [
        'influenza-like illness',
        'ARI',
        'flu-like syndrome',
        'dry cough',
        'nausea'
    ],
    'acute fever and rash': [
        'acute fever and rash',
        'Fever',
        'rash'
    ],
    'fever of unknown origin': [
        'fever of unknown origin',
    ],
    'meningitis': [
        'meningitis',
        'refusing feeds',
        'fretfulness',
        'high moaning cry',
        'vomiting',
        'purple–red skin rash',
        'photophobia'
    ]
}

if __name__ == "__main__":
    print(MATCH_SYNDROME)
