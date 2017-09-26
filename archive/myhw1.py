
def myFilter(L, num):
	return [x for x in L if x%num != 0]

#print( myFilter([2, 3, 4, 6, 7, 11], 3) )

def myLists(L):
	return [list(range(1, x+1)) for x in L]

#print( myLists([2, 3, 4, 6, 7, 11]) )

def myFunctionComposition(f, g):
	return {k:g[v] for k, v in f.items()}

'''
F = {0:'a', 1:'b'}
G = {'a':'apple', 'b':'banana'}

print( myFunctionComposition(F, G) )
'''

def mySum(L):
	current = 0
	for x in L:
		current = current + x
	return current

def myProduct(L):
	current = 1
	for x in L:
		current = current * x
	return current

def myMin(L):
	for (i, x) in enumerate(L):
		if i == 0:
			current = x
		if x < current:
			current = x
	return current

def myConcat(L):
	current = ''
	for x in L:
		current = current + x
	return current

def myUnion(L):
	current = set()
	for x in L:
		current = current | x
	return current

'''
myL = [2, 7, 3, 1, 9, 2, -4, -3]
print( mySum(myL) )
print( myProduct(myL) )
print( myMin(myL) )
print( myConcat(['freedom', 'is', 'priority', 'number', 'one']) )
print( myUnion([{'a', 'c', 'n'}, {'housewives', 'truck drivers', 'salesmen'}, {'liberals', 'conservatives'}, {'What the heck?', 'Never, ever.'}, {'PR', 'PA'}]) )
'''

def list2vec(L):
	return Vec(set(range(len(L))), {k:x for k, x in enumerate(L)})

def addVectors(v1, v2):
	assert len(v1) == len(v2)
	return [v1[i] + v2[i] for i, elem in enumerate(v1)]


#print( addVectors([1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0]) )
#L = []

def politics1():
	KEY_INDEX = 0
	RECORD_START_INDEX = 3
	lines = [ln.split() for ln in list(open('voting_record_dump109.txt'))]
	return {ln[KEY_INDEX]:list(map(int, ln[RECORD_START_INDEX::])) for ln in lines}

#print(politics1()['Clinton'])

def politics2(sen_a, sen_b, voting_dict):
	return sum([a*b for a, b in zip(voting_dict[sen_a], voting_dict[sen_b])])

#print(politics2('Clinton', 'Grassley', politics1()))

def politics3(sen, voting_dict):
	d = {comp:politics2(sen, comp, voting_dict) for comp in voting_dict.keys() if comp != sen}
	return max(d, key=d.get)

def politics4(sen, voting_dict):
	d = {comp:politics2(sen, comp, voting_dict) for comp in voting_dict.keys() if comp != sen}
	return min(d, key=d.get)
	

print(politics3('Chafee', politics1()))
print(politics4('Santorum', politics1()))

