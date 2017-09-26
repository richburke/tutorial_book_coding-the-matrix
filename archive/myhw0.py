
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

myL = [2, 7, 3, 1, 9, 2, -4, -3]
print( mySum(myL) )
print( myProduct(myL) )
print( myMin(myL) )
print( myConcat(['freedom', 'is', 'priority', 'number', 'one']) )
print( myUnion([{'a', 'c', 'n'}, {'housewives', 'truck drivers', 'salesmen'}, {'liberals', 'conservatives'}, {'What the heck?', 'Never, ever.'}, {'PR', 'PA'}]) )