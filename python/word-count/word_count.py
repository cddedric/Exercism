from collections import Counter
def word_count(inputString):
	inputString = inputString.lower()
	secondString = ''
	for i in range(len(inputString)):
		if inputString[i].isalpha() or inputString[i].isdecimal():
			secondString += inputString[i]
		else:
			secondString += ' '
			i = i+1
	dictionary = secondString.split()
	wordDictionary = Counter(dictionary)
	return wordDictionary