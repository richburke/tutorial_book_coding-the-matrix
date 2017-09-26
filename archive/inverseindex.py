'''
def makeInverseIndex(strlist):
	S = {}
	for line in enumerate(strlist):
		for word in line[1].split():
			if word not in S:
				S[word] = []
			S[word].append(line[0])
	print(S)
'''

def makeInverseIndex(strlist):
	S = {}
	for (num, line) in enumerate(strlist):
		for word in line.split():
			if word not in S:
				S[word] = set()
			S[word].add(num)
	return S

def orSearch(inverseIndex, query):
	return {docs for w in query for docs in inverseIndex[w]}

def andSearch(inverseIndex, query):
	S = set()
	for (i, w) in enumerate(query):
		if i == 0:
			S = S | inverseIndex[w]
		else:
			S = S & inverseIndex[w]
	return S

strs = list(open('stories_big.txt'))
searchTerms = ['determined', 'desperately', 'egomaniacs']

print( orSearch(makeInverseIndex(strs), searchTerms) )

searchTerms = ['writer', 'reveals']
print( andSearch(makeInverseIndex(strs), searchTerms) )
