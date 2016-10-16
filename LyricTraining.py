import random
import re
import pickle

def addToLib(fileName):
	f = open(fileName, 'r')
	words = re.sub("\n", " \n ", f.read()).split(' ')
	f.close()
	print "Words Read and Split"
	curr = 0
	currLib = {}
	while curr < len(words) - 1:
		currWord = words[curr].lower()
		nextWord = words[curr + 1].lower()
		if currWord in currLib.keys():
			if nextWord in currLib[currWord].keys():
				currLib[currWord][nextWord] += 1
			else:
				currLib[currWord][nextWord] = 1
		else:
			currLib[currWord] = {nextWord: 1}
		curr += 1
	print "Chain Built"
	for key in currLib.keys():
		#for each word
		keyTotal = 0
		for probKey in currLib[key].keys():
			keyTotal += currLib[key][probKey]
		for probKey in currLib[key].keys():
			currLib[key][probKey] = currLib[key][probKey]/keyTotal
	print "Probabilites calculated for transition matrix"
	return currLib
	
def main():
	libChain = addToLib('Lyrics.txt')
	f = open('GeneratorPickle.pickle','w')
	pickle.dump(libChain,f)
	f.close()
	print "Stored in Pickle"
	
if __name__ == "__main__":
	main()
