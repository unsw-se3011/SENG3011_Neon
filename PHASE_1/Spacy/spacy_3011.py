from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
LABEL1 = "Syndrome"
LABEL2 = "Disease"
TEXTS = [
    "The Pat Walker Health Center at the University of Arkansas issued a campus health advisory after the Arkansas Department of Health (ADH) identified three confirmed cases and one suspected case of mumps on the University of Arkansas (UA) at Fayetteville campus in the last few weeks.",
    "Infographic aimed at college students depicting symptoms of mumps and steps they can take to protect themselves.",
    "Those who may have been exposed have receive additional communication and information from Pat Walker Health Center.",
    "ADH is working closely with the UA Fayetteville campus to alert students and staff who may have been in close contact with the confirmed cases.",
    "These close contacts, as well as anyone with an MMR vaccine exemption on campus, are encouraged to seek vaccination.",
    "MMR vaccines are available at the Washington County Local Health Unit, and are also available at many doctors\u2019 offices or local pharmacies.",
    "Vaccines are also available to the UA Fayetteville community at the Pat Walker Health Center on campus From August 2016 to August 2017, Arkansas experienced the second-largest mumps outbreak in the United States in the last 30 years.",
    "Nearly 3,000 mumps cases related to the outbreak during that period were identified.",
    "Texas measles case count at eight as of mid-February According to the Centers for Disease Control and Prevention (CDC), mumps is a viral illness that is transmitted by direct contact with respiratory droplets or saliva from an infected person.",
    "It is best known for painful, swollen salivary glands that show up as puffy cheeks and swollen jaw. Boys may also have painful, swollen testicles.",
    "In some of these cases, fertility can be affected. Other symptoms include fever, headache, muscles aches, tiredness, and loss of appetite.",
    "There is no treatment, and symptoms usually resolve themselves within a few weeks.",
    "Mumps is usually a mild disease in children, but adults may have more serious disease with complications.",
    "Complications can include deafness and encephalitis.",
    "Encephalitis is inflammation of the brain.",
    "The MMR vaccine is safe and effective.",
    "Two doses of MMR vaccine are 88 percent effective in preventing mumps.",
    "It is a live virus vaccine and is not recommended for pregnant women or patients with a weakened immune system.",
    "Adults born before 1957 are generally considered to be immune to mumps and do not need to receive the MMR vaccine."
]
TRAIN_DATA = [
    ("Encephalitis is inflammation of the brain.",
     {"entities": [(0, 12, LABEL1)]}),
    ("Haemorrhagic Fever", {"entities": [(0, 18, LABEL1)]}),
    ("Acute Flacid Paralysis", {"entities": [(0, 22, LABEL1)]}),
    ("Acute gastroenteritis", {"entities": [(0, 21, LABEL1)]}),
    ("Acute respiratory syndrome", {"entities": [(0, 26, LABEL1)]}),
    ("Influenza-like illness", {"entities": [(0, 22, LABEL1)]}),
    ("Acute fever and rash", {"entities": [(0, 20, LABEL1)]}),
    ("Fever of unknown Origin", {"entities": [(0, 23, LABEL1)]}),
    ("Meningitis", {"entities": [(0, 10, LABEL1)]}),
    ("Encephalitis", {"entities": [(0, 12, LABEL1)]}),
    ("Two doses of MMR vaccine are 88 percent effective in preventing mumps.",
     {"entities": []}),
    ("Complications can include deafness and encephalitis.",
     {"entities": [(39, 51, LABEL1)]},),
]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model, n_iter=30):

    # load existing spaCy model
    if model is not None:
        nlp = spacy.load(model)
        print("Loaded model '%s'" % model)
    else:

        # create blank Language class
        nlp = spacy.blank("en")
        print("Created blank 'en' model")

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)

    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    # add new entity label to entity recognizer
    ner.add_label(LABEL1)
    ner.add_label(LABEL2)
    # Adding extraneous labels shouldn't mess anything up
    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()
    move_names = list(ner.move_names)

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

    # only train NER
    with nlp.disable_pipes(*other_pipes):
        sizes = compounding(1.0, 4.0, 1.001)

        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = minibatch(TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer,
                           drop=0.35, losses=losses)

    print("Loaded model '%s'" % model)
    print("Processing %d texts" % len(TEXTS))

    # test the above texts
    for text in TEXTS:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == "Syndrome":
                print(ent.label_, ent.text)
            if ent.label_ == "Disease":
                print(ent.label_, ent.text)


'''
#try to extract information from above 
def extract_currency_relations(doc):
    # merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    for syndrome in filter(lambda w: w.ent_type_ == "Syndrome", doc):
        if syndrome.dep_ in ("attr", "dobj"):
            subject = [w for w in syndrome.head.lefts if w.dep_ == "nsubj"]
            if subject:
                subject = subject[0]
                relations.append((subject, syndrome))
        elif syndrome.dep_ == "pobj" and syndrome.head.dep_ == "prep":
            relations.append((syndrome.head.head, syndrome))
    return relations'''

if __name__ == "__main__":
    plac.call(main)


'''
#simple code for check pos, ent and tag
import spacy
from collections import Counter
syndrome_pos_tags = ["NOUN"]
nlp = spacy.load('en')

myfile = open('outbreak_brief.jl').read()
doc = nlp(myfile)
nouns = [ token.text for token in doc if token.is_stop != True and token.is_punct !=True and token.pos_ == 'NOUN']
word_freq = Counter(nouns)

common_nouns = word_freq.most_common(10)

print(common_nouns)

verbs = [ token.text for token in doc if token.is_punct !=True and token.pos_ == 'VERB']
print(Counter(verbs).most_common(10))

verbs_with_stopword = [ token.text for token in doc if token.is_stop != True and token.is_punct !=True and token.pos_ == 'VERB']
print(Counter(verbs_with_stopword).most_common(10))

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

#try to use pos match disease or syndrome
def isSyndrome(token):
    is_Syndrome = False
    if token.pos_ in  syndrome_pos_tags:
        is_Syndrome = True
    elif token.dep_ == conj:
        is_Syndrome = True
    elif token.is_alpha = True:
        is_Syndrome = True
    elif token.is_stop = False:
        isSyndrome = True'''
