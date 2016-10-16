import random
import pickle

def markov_next(currword, probDict):
	if currword not in probDict.keys():
		return random.choice(probDict.keys())
	else:
		wordprobs = probDict[currword]
		randProb = random.uniform(0.0, 1.0)
		currProb = 0.0
		for key in wordprobs:
			currProb += wordprobs[key]
			if randProb <= currProb:
				return key
		return random.choice(probDict.keys())

def makeRap(startword, probDict, no_words):
	rap, curr, wc = '', startword, 0
	while wc < no_words:
		rap += curr + ' '
		curr = markov_next(curr, probDict)
		wc += 1
	return rap
	
def main():
	f = open('GeneratorPickle.pickle','r')
	probDict = pickle.load(f)
	f.close()
	word = raw_input("Enter the starting word for generating rap!?")
	no_words = raw_input("Enter number of words for the rap!?")
	print makeRap(word, probDict, int(no_words))
	
if __name__=="__main__":
	main()

	
