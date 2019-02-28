# prompts:

# python3 testing.py
# import nltk
# nltk.download(all) 

from nltk.tokenize import * #sent_tokenize, word_tokenize
from nltk.corpus import *
from nltk.stem import *
import pickle


from json import loads
import fileinput

import nltk
# from nltk.corpus import state_union
# from nltk.tokenize import PunktSentenceTokenizer



# sample text
# sample = gutenberg.raw("/Users/iriszhang/Desktop/ProjectNeon-w1-nltk/scraper/outbreak.jl")

# tok = sent_tokenize(sample)

# for x in range(5):
#     print(tok[x])
#     print( '\n')



if __name__ == "__main__":
	import argparse

	# get input of command line arguement
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'file',
		help="File of json line input.",
		type=str,
		default="outbreak.jl"
		)
	args = parser.parse_args()

	# change it to an iterator to enable setting up multi-thread
	# without dealing with lock
	print(args.file)

	it = iter(fileinput.input(files=args.file))
	ps = PorterStemmer()

	while True:
		j_dict = loads(next(it))
		# print(j_dict['main_text'])
		
		sample = j_dict['main_text']

		stop_words = set(stopwords.words('english'))
		print(stop_words)

		tok = sent_tokenize(sample)
		punk = PunktSentenceTokenizer(sample)
		tokenize = punk.tokenize(sample)
		print(tokenize)
		print('\n\n')

		try:
			for i in tokenize:
				words = nltk.word_tokenize(i)
				tagged = nltk.pos_tag(words)

				for t in tagged:
					if t not in stop_words:
						print(t)
						# print(ps.stem(t[0]))
				
				print("\n")

		except Exception as e:
			print("Exception!!")
			print(str(e))

		# for x in range(4):
		# 	print(tok[x])
		# 	print('\n')

		exit(0)



# save_classifier = open("naivebayes.pickle","wb")
# pickle.dump()


###################### Tutorial example below #######################

# sentence = "Hello, this is a test for nltk testing"
# s1 = "This is a sample sentence, showing off the stop words filtration."
# stop_words = set(stopwords.words('english'))


# filtered_sentence = []

# for w in word_tokenize(s1):
#     if w not in stop_words:
#         filtered_sentence.append(w)

# print(filtered_sentence)



# filtered_sentence = []

# new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
# ps = PorterStemmer()

# for w in word_tokenize(new_text):
#     filtered_sentence.append(ps.stem(w))

# print(filtered_sentence)


# print(sent_tokenize(sentence))
# print(word_tokenize(sentence))


