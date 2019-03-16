import spacy
nlp= spacy.load('en')

'''myfile = open("outbreak_brief.jl").read()
test_doc = nlp(myfile)'''

doc = nlp('Spacy is an amazing tool')
for token in doc :
    print(token.text)
#word Shape
for word in doc:
    print(word.text,word.shape_)
ex_doc = nlp("Hello hello HELLO hello")
for word in ex_doc:
    print("Token =>", word.text, "Shape",word.shape_)

ex1 = nlp("he drinks a drink")
for word in ex1 :
    print(word.text,word.pos_)
'''output
        He PRON
        drinks VRB
        a DET
        drink NOUN'''

ex2 = nlp("I fish a fish")
    for word in ex2:
        print(word.text, word_pos,word.tag_)
'''output
        I RPON PRP
        fish VERB VBP
        a DET DT
        fish NOUN NN'''

ex3 = nip(u"All the faith he had had had no effecton the outcome in his life")
     for word in ex3:
         print((word.text,word.tag_,word.pos_))
'''output
        ('All', 'PDT','ADJ')
        '
        '
        '
        ('had','VBD','VERB')
        ('had','VBN','VERB')
        ('had','VBN','VERB')'''
docx3 = nlp('Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo')
for word in docx3:
    print((word.text,word.tag_,word.pos_,word.dep_))
'''output
        ('Buffalo', 'NNP', 'PROPN', 'compound')
('buffalo', 'NN', 'NOUN', 'compound')
('Buffalo', 'NNP', 'PROPN', 'compound')
('buffalo', 'NN', 'NOUN6', 'compound')
('buffalo', 'NN', 'NOUN', 'compound')
('buffalo', 'NN', 'NOUN', 'compound')
('Buffalo', 'NNP', 'PROPN', 'compound')
('buffalo', 'NN', 'NOUN', 'ROOT')
'''

Using displaCy in Jupyter notebooks
displacy.render(jupyter=True)

displacy.render(docx3,style='dep',jupyter=True)
SVG Image
options = {'compact': True, 'bg': 'cornflowerblue',
           'color': '#fff', 'font': 'Sans Serif'}

displacy.render(docx3,style='dep',options=options,jupyter=True)
SVG Image

# Adding Title
docx3.user_data['title']= 'Buffalo Complex Sentence'

displacy.render(docx3,style='dep',options=options,jupyter=True)

html = displacy.render(docx3,style='dep',page=True)
Exporting The Rendered Graphic

svg = displacy.render(doc, style='dep')
output = 'buffalosentence.svg'
with open(output,'w', encoding='utf-8') as f:
    f.write(svg)

# Alternative Method
# svg = displacy.render(doc, style='dep')
# output_path = Path('/images/sentence.svg')
# output_path.open('w', encoding='utf-8').write(svg)
Named Entity Recognition or Detection
Classifying a text into predefined categories or real world object entities.
takes a string of text (sentence or paragraph) as input and identifies relevant nouns (people, places, and organizations) that are mentioned in that string.
Uses
Classifying or Categorizing contents by getting the relevant tags
Improve search algorithms
For content recommendations
For info extraction

wikitext = nlp(u"By 2020 the telecom company Orange, will relocate from Turkey to Orange County in the U.S. close to Apple.It will cost them 2 billion dollars.")

for entity in wikitext.ents:
    print(entity.text,entity.label_)
'''out
2020 DATE
Turkey GPE
Orange County GPE
U.S. GPE
Apple ORG
2 billion dollars MONEY'''


# What does GPE means
spacy.explain('GPE')
'Countries, cities, states'

# Visualize With DiSplaCy
displacy.render(wikitext,style='ent',jupyter=True)
By the telecom company Orange, will relocate from to in the close to .It will cost them .

wikitext2 = nlp(u"Linus Benedict Torvalds is a Finnish-American software engineer who is the creator, and for a long time, principal developer of the Linux kernel, which became the kernel for operating systems such as the Linux operating systems, Android, and Chrome OS.")
# Visualize With DiSplaCy
displacy.render(wikitext2,style='ent',jupyter=True)
is a -American software engineer who is the creator, and for a long time, principal developer of the kernel, which became the kernel for operating systems such as the operating systems, , and Chrome OS.

spacy.explain('NORP')
'Nationalities or religious or political groups'

doc1 = nlp("Facebook, Explosion.ai, JCharisTech are all internet companies")
# Visualize With DiSplaCy
displacy.render(doc1,style='ent',jupyter=True)


## Lemmatization  
docx_lemma = nlp("studying student study studies studio studious")

for word in docx_lemma:
    print("Token=>",word.text,"Lemma=>",word.lemma_,word.pos_)

'''Token=> studying Lemma=> study VERB
Token=> student Lemma=> student NOUN
Token=> study Lemma=> study NOUN
Token=> studies Lemma=> study NOUN
Token=> studio Lemma=> studio NOUN
Token=> studious Lemma=> studious ADJ'''


docx_lemma1 = nlp("good goods run running runner was be were")

for word in docx_lemma1:
    print("Token=>",word.text,"Lemma=>",word.lemma_,word.pos_)
'''Token=> good Lemma=> good ADJ
Token=> goods Lemma=> good NOUN
Token=> run Lemma=> run VERB
Token=> running Lemma=> run VERB
Token=> runner Lemma=> runner NOUN
Token=> was Lemma=> be VERB
Token=> be Lemma=> be VERB
Token=> were Lemma=> be VERB'''

docx_lemma2 = nlp("walking walks walk walker")

for word in docx_lemma2:
    print("Token=>",word.text,"Lemma=>",word.lemma_,word.pos_)
'''Token=> walking Lemma=> walk VERB
Token=> walks Lemma=> walk NOUN
Token=> walk Lemma=> walk VERB
Token=> walker Lemma=> walker ADV
Semantic Similarity
object1.similarity(object2)'''
Uses:
Recommendation systems
Data Preprocessing eg removing duplicates
python -m spacy download en_core_web_lg


# Loading Packages
import spacy
nlp = spacy.load('en')

# Similarity of object
doc1 = nlp("wolf")
doc2 = nlp("dog")

doc1.similarity(doc2)
0.6759108958707175

doc3  = nlp("cat")
doc3.similarity(doc2)
0.7344887997583573

# Synonmys
doc4 = nlp("smart")
doc5 = nlp("clever")
# Similarity of words
doc4.similarity(doc5)
0.8051825859624082

similarword = nlp("wolf dog cat bird fish")

for token in similarword:
    print(token.text)
'''
wolf
dog
cat
bird
fish'''


# Similarity Between Tokens
for token1 in similarword:
    for token2 in similarword:
        print((token1.text,token2.text),"similarity=>",token1.similarity(token2))
'''('wolf', 'wolf') similarity=> 1.0
('wolf', 'dog') similarity=> 0.5234999
('wolf', 'cat') similarity=> 0.30953428
('wolf', 'bird') similarity=> 0.52796596
('wolf', 'fish') similarity=> 0.051317338
('dog', 'wolf') similarity=> 0.5234999
('dog', 'dog') similarity=> 1.0
('dog', 'cat') similarity=> 0.62507194
('dog', 'bird') similarity=> 0.4794655
('dog', 'fish') similarity=> 0.32915178
('cat', 'wolf') similarity=> 0.30953428
('cat', 'dog') similarity=> 0.62507194
('cat', 'cat') similarity=> 1.0
('cat', 'bird') similarity=> 0.4474155
('cat', 'fish') similarity=> 0.447517
('bird', 'wolf') similarity=> 0.52796596
('bird', 'dog') similarity=> 0.4794655
('bird', 'cat') similarity=> 0.4474155
('bird', 'bird') similarity=> 1.0
('bird', 'fish') similarity=> 0.35412988
('fish', 'wolf') similarity=> 0.051317338
('fish', 'dog') similarity=> 0.32915178
('fish', 'cat') similarity=> 0.447517
('fish', 'bird') similarity=> 0.35412988
('fish', 'fish') similarity=> 1.0'''

#[x for b in a for x in b] 
mylist = [(token1.text,token2.text,token1.similarity(token2)) for token2 in similarword for token1 in similarword]
mylist
'''[('wolf', 'wolf', 1.0),
 ('dog', 'wolf', 0.5234999),
 ('cat', 'wolf', 0.30953428),
 ('bird', 'wolf', 0.52796596),
 ('fish', 'wolf', 0.051317338),
 ('wolf', 'dog', 0.5234999),
 ('dog', 'dog', 1.0),
 ('cat', 'dog', 0.62507194),
 ('bird', 'dog', 0.4794655),
 ('fish', 'dog', 0.32915178),
 ('wolf', 'cat', 0.30953428),
 ('dog', 'cat', 0.62507194),
 ('cat', 'cat', 1.0),
 ('bird', 'cat', 0.4474155),
 ('fish', 'cat', 0.447517),
 ('wolf', 'bird', 0.52796596),
 ('dog', 'bird', 0.4794655),
 ('cat', 'bird', 0.4474155),
 ('bird', 'bird', 1.0),
 ('fish', 'bird', 0.35412988),
 ('wolf', 'fish', 0.051317338),
 ('dog', 'fish', 0.32915178),
 ('cat', 'fish', 0.447517),
 ('bird', 'fish', 0.35412988),
 ('fish', 'fish', 1.0)]'''
Using DataFrames
import pandas as pd
df = pd.DataFrame(mylist)
df.head()
'''0	1	2
0	wolf	wolf	1.000000
1	dog	wolf	0.523500
2	cat	wolf	0.309534
3	bird	wolf	0.527966
4	fish	wolf	0.051317'''


# Correlation
df.corr()
2
2	1.0

df.columns = ["Token1","Token2","Similarity"]
df.head()
'''Token1	Token2	Similarity
0	wolf	wolf	1.000000
1	dog	wolf	0.523500
2	cat	wolf	0.309534
3	bird	wolf	0.527966
4	fish	wolf	0.051317'''


# Types
df.dtypes
Token1         object
Token2         object
Similarity    float64
dtype: object
# Visualization Package with Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Encoding it
df_viz = df.replace({'wolf':0,'dog':1,'cat':2,'fish':3,'bird':4})
df_viz.head()
'''
Token1	Token2	Similarity
0	0	0	1.000000
1	1	0	0.523500
2	2	0	0.309534
3	4	0	0.527966
4	3	0	0.051317'''


# Plotting with Correlation
plt.figure(figsize=(20,10))
sns.heatmap(df_viz.corr(),annot=True)
plt.show()


# Plotting without correlation
plt.figure(figsize=(20,10))
sns.heatmap(df_viz,annot=True)
plt.show()
'''
Word Analysis
shape of word
is_alpha
is_stop
Noun Chunks
noun + word describing the noun
noun phrases
adnominal
root.text'''


import spacy
nlp = spacy.load('en')

# Noun Phrase or Chunks
doc_phrase1 = nlp("The man reading the news is very tall.")

for word in doc_phrase1.noun_chunks:
    print(word.text)
'''The man
the news'''


# Root Text
# the Main Noun 
for word in doc_phrase1.noun_chunks:
    print(word.root.text)
'''man
news'''


# Text of the root token head
for token in doc_phrase1.noun_chunks:
    print(token.root.text,"connector_text to root head :",token.root.head.text)
'''man connector_text to root head : is
news connector_text to root head : reading'''



doc_phrase2 = nlp("For us the news is a concern.")
for word in doc_phrase2.noun_chunks:
    print(word.text,"Connector:",word.root.text,"Text of Root Tokens Head: ",word.root.head.text)

'''us Connector: us Text of Root Tokens Head:  For
the news Connector: news Text of Root Tokens Head:  is
a concern Connector: concern Text of Root Tokens Head:  is
Sentence Segmentation or Boundary Detection
Deciding where sentences begin and end'''

===================================================
a) If it's a period, it ends a sentence.
(b) If the preceding token is in the hand-compiled list of abbreviations, then it doesn't end a sentence.
(c) If the next token is capitalized, then it ends a sentence.
===================================================


Default = Uses the Dependency parser
Custom Rule Based or Manual
You set boundaries before parsing the doc

# Manual or Custom Based
def mycustom_boundary(docx):
    for token in docx[:-1]:
        if token.text == '...':
            docx[token.i+1].is_sent_start = True
    return docx

import spacy 
nlp = spacy.load('en')

# Adding the rule before parsing
nlp.add_pipe(mycustom_boundary,before='parser')

mydoc = nlp(u"This is my first sentence...the last comment was so cuul... what if...? this is the last sentence")

for sentence in mydoc.sents:
    print(sentence.text)
'''This is my first sentence...
the last comment was so cuul...
what if...
?
this is the last sentence'''


# Manual or Custom Based
def mycustom_boundary2(docx):
    for token in docx[:-1]:
        if token.text == '---':
            docx[token.i+1].is_sent_start = True
    return docx

nlp2 = spacy.load('en')

# Adding the rule before parsing
nlp2.add_pipe(mycustom_boundary2,before='parser')

mydoc2 = nlp2(u"Last year was great---this year 2018-05-22 will be so cuul. when was your birthday? ---this is the last sentence")

for sentence in mydoc2.sents:
    print(sentence.text)

'''Last year was great---
this year 2018-05-22 will be so cuul.
when was your birthday?
---this is the last sentence'''


# Removing the parsing
nlp.remove_pipe('parser')

nlp = spacy.load('en')

mydoc3 = nlp(u"This is my first sentence...the last comment was so cuul... what if...? this is the last sentence")

# Normal Sentence Segmenter
for sentence in mydoc3.sents:
    print(sentence.text)
'''This is my first sentence...the last comment was so cuul...
what if...?
this is the last sentence'''

Custome Rule Based

from spacy.lang.en import English
from spacy.pipeline import SentenceSegmenter

def split_on_newlines(doc):
    start = 0
    seen_newline = False
    for word in doc:
        if seen_newline and not word.is_space:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text == '\n':
            seen_newline = True
    if start < len(doc):
        yield doc[start:len(doc)]

def split_on_tab(doc):
    start = 0
    seen_newline = False
    for word in doc:
        if seen_newline and not word.is_space:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text == '\t':
            seen_newline = True
    if start < len(doc):
        yield doc[start:len(doc)]

nlp = English()  # just the language with no model
sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)
nlp.add_pipe(sbd)

doc = nlp(u"This is a great sentence\n\nThis is another comment\nAnd more")
for sent in doc.sents:
    print(sent.text)

'''This is a great sentence

This is another comment

And more'''


doc = nlp(u"This is a great sentence\n\nThis is another comment\nAnd more")
for sent in doc.sents:
    print([token.text for token in sent])

'''['This', 'is', 'a', 'great', 'sentence', '\n\n', 'This', 'is', 'another', 'comment', '\n']
['And', 'more']'''


nlp_tab = English()  # just the language with no model
sbd_tab = SentenceSegmenter(nlp.vocab, strategy=split_on_tab)
nlp_tab.add_pipe(sbd_tab)

## Spliting on Tabs
doc_tab = nlp_tab(u"This is a great sentence\t This is another\t comment\t And more")

for sent in doc_tab.sents:
    print(sent.text)

'''This is a great sentence	 This is another	 comment	 And more'''

Stops Words In Spacy
A Stop word/Stop list
Words filtered out before preprocessing
Most Common words*
Uses
Improve performance in search engines
eg how to perform sentiment analysis
Eliminating noise and distraction in sentiment classification
Make ML learning faster due to less features
Make Prediction more accurate due to noise reduction

import spacy 
nlp = spacy.load('en')

from spacy.lang.en.stop_words import STOP_WORDS

# Print List of Stop words
print(STOP_WORDS)
'''{'although', 'ours', 'since', 'she', 'last', 'anyone', 'together', 'herself', 'besides', 'was', 'else', 'one', 'toward', 'often', 'unless', 'indeed', 'something', 'itself', 'becomes', 'several', 'front', 'meanwhile', 'whereafter', 'will', 'whereby', 'two', 'before', 'each', 'empty', 'do', 'fifteen', 'otherwise', 'own', 'has', 'anywhere', 'really', 'i', 'an', 'have', 'hundred', 'nine', 'the', 'all', 'others', 'beyond', 'hereby', 'yet', 'bottom', 'perhaps', 'into', 'anyway', 'when', 'both', 'sixty', 'onto', 'whereupon', 'once', 'six', 'where', 'would', 'about', 'by', 'because', 'no', 'except', 'ten', 'yourselves', 'above', 'cannot', 'thereby', 'forty', 'on', 'hers', 'myself', 'name', 'side', 'latter', 'from', 'nowhere', 'then', 'throughout', 'for', 'himself', 'same', 'their', 'again', 'there', 'full', 'done', 'under', 'it', 'thus', 'might', 'already', 'whether', 'call', 'now', 'via', 'could', 'make', 'elsewhere', 'always', 'many', 'seems', 'they', 'third', 'seemed', 'did', 'get', 'his', 'well', 'does', 'may', 'few', 'whence', 'please', 'say', 'such', 'while', 'whom', 'hereupon', 'beside', 'who', 'anyhow', 'however', 'amongst', 'your', 'move', 'be', 'along', 'ca', 'back', 'none', 'therein', 'within', 'how', 'nothing', 'among', 'than', 'across', 'but', 'neither', 'whither', 'here', 'if', 'nor', 'being', 'below', 'is', 'afterwards', 'seem', 'through', 'whole', 'take', 'nobody', 'sometimes', 'with', 'became', 'he', 'see', 'less', 'over', 'am', 'either', 'various', 'most', 'five', 'somehow', 'twelve', 'becoming', 'whenever', 'beforehand', 'anything', 'become', 'sometime', 'very', 'are', 'just', 'mine', 'its', 'noone', 'ever', 'must', 'part', 'against', 'thereupon', 'though', 'hence', 'another', 'any', 'behind', 'everyone', 'until', 'mostly', 'can', 'namely', 'only', 'or', 'enough', 'someone', 'a', 'us', 'without', 'of', 'whoever', 'seeming', 'more', 'these', 'themselves', 'also', 'due', 'formerly', 'them', 'eleven', 'give', 'keep', 'using', 'off', 'former', 'therefore', 'up', 'first', 'whereas', 'after', 'as', 'every', 'made', 'towards', 'fifty', 'what', 'yourself', 're', 'my', 'our', 'which', 'quite', 'wherever', 'three', 'used', 'had', 'regarding', 'been', 'between', 'everywhere', 'somewhere', 'this', 'too', 'still', 'we', 'whose', 'even', 'hereafter', 'thru', 'almost', 'ourselves', 'and', 'doing', 'four', 'never', 'next', 'during', 'eight', 'whatever', 'rather', 'further', 'much', 'out', 'him', 'least', 'those', 'not', 'some', 'should', 'moreover', 'amount', 'to', 'you', 'twenty', 'down', 'why', 'thence', 'were', 'serious', 'everything', 'wherein', 'around', 'in', 'other', 'thereafter', 'upon', 'nevertheless', 'per', 'alone', 'go', 'show', 'top', 'her', 'herein', 'at', 'that', 'so', 'me', 'latterly', 'put', 'yours'}
'''

len(STOP_WORDS)
'''
305'''


# Checking If A Word is a Stopword
nlp.vocab["the"].is_stop
True


nlp.vocab["theme"].is_stop
Out[120]:
False


mysentence = nlp(u"This is a group of word to check for stop words")
# Filtering Non Stop Words
for word in mysentence:
    if word.is_stop == True:
        print(word)
'''is
a
of
to
for'''


# Filtering Stop Words
filterdwords = []
for word in mysentence:
    if word.is_stop == False:
        print(word)
'''This
group
word
check
stop
words'''


# Filtering Stop Words
filteredwords = []
for word in mysentence:
    if word.is_stop == False:
        filteredwords.append(word)
print(filteredwords)

'''[This, group, word, check, stop, words]'''


[ word for word in mysentence if word.is_stop == False]
[This, group, word, check, stop, words]

# Filtering Stop Words
filtered = []
for word in mysentence:
    if word not in STOP_WORDS:
        filtered.append(word)
print(filtered)

'''[This, is, a, group, of, word, to, check, for, stop, words]'''
In [ ]:
# Filtering Stop Words

# for word in STOP_WORDS:
#     if nlp.vocab[word].is_stop == True:
#         print(word)

# for mysentence in STOP_WORDS:
#     lexeme = nlp.vocab[mysentence]
#     lexeme.is_stop = True
#     print(lexeme)

Adding Your Own Stop Words
stoplist = STOP_WORDS.add("lol")
example2 = nlp(u"There are a lot of lol in this sentence but what does it mean.")
for word in example2:
    if word.is_stop == True:
        print(word)

'''are
a
of
lol
in
this
but
what
does
it'''


# Lol Has been Added as A Stop Word
nlp.vocab["lol"].is_stop
Out[130]:
True


In [ ]:
#Removing Stop Words
STOP_WORDS.remove("lol")
# Remove the Last word added
STOP_WORDS.pop("lol")
In [ ]:

Text Similarity With ML

# Using ML
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

documents = ['wolf','dog','cat','bird','fish']

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(documents).todense()

print(vectorizer.vocabulary_)
{'dog': 2, 'fish': 3, 'wolf': 4, 'cat': 1, 'bird': 0}

for word in features:
    print(euclidean_distances(features[0]),word)
'''[[0.]] [[0 0 0 0 1]]
[[0.]] [[0 0 1 0 0]]
[[0.]] [[0 1 0 0 0]]
[[0.]] [[1 0 0 0 0]]
[[0.]] [[0 0 0 1 0]]'''
Sentence Similarity
To do

# Using Three Sentences
corpus1 = ["I like that bachelor","I like that unmarried man","I don't like the married man"]
corpus2 = ["Jane is very nice.", "Is Jane very nice?"]
corpus3 = ["He is a bachelor","He is an unmarried man"]
corpus4 = ["She is a wife","She is a wife"]
corpus5 = ["He is a king","He is a doctor"]
Rule-based Matching
Tokenize
Pattern matching

from spacy.matcher import Matcher
import spacy
nlp = spacy.load('en')
patterns = {'HelloWorld': [{'LOWER': 'hello'}, {'LOWER': 'world'}]}
matcher = Matcher(nlp.vocab)

matcher = Matcher(nlp.vocab)

pattern = [{'LOWER': "hello"}, {'LOWER': "world"}]
# matcher.add("HelloWorld", None, pattern)

matcher.add("HelloWorld", None, pattern)

doc = nlp(u'hello world this is not it!')
matches = matcher(doc)

print(matches)
'''[(15578876784678163569, 0, 2)]'''
