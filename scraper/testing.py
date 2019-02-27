# prompts:

# python3 testing.py
# import nltk
# nltk.download(all) 

from nltk.tokenize import * #sent_tokenize, word_tokenize
from nltk.corpus import *
from nltk.stem import *



sentence = "Hello, this is a test for nltk testing"
s1 = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))


filtered_sentence = []

for w in word_tokenize(s1):
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)



filtered_sentence = []

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
ps = PorterStemmer()

for w in word_tokenize(new_text):
    filtered_sentence.append(ps.stem(w))

print(filtered_sentence)


# print(sent_tokenize(sentence))
# print(word_tokenize(sentence))


