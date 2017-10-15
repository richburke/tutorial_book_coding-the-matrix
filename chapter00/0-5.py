# Exercises from section 0.5

# Secondary exercise(s):
# * set up workspace [done]
# * set up git [done]

# 0.5.1
print('0.5.1: Number of seconds in a week')
seconds_in_week = 7 * 24 * 60 * 60
print(seconds_in_week)
print()

# 0.5.2
n1 = 2304811
divisor = 47
print('0.5.2: Remainder of {} / {}'.format(n1, divisor))
remainder = (n1 / divisor) - (n1 // divisor)
print(remainder)
print()

# 0.5.3
n1 = 673
n2 = 909
divisor = 3
print('0.5.3: Test whether {} + {} is divisible by {}'.format(n1, n2, divisor))
print((673 + 909) % 3 == 0)
print()

# 0.5.4
x = -9
y = 1 / 2
print('0.5.4: If x is {} and y is {}, predict the value of 2**(y+1/2) if x+10<0 else 2**(y-1/2)'.format(x, y))
print(2**(y + 1 / 2) if x + 10 < 0 else 2**(y - 1 / 2))
print()

# 0.5.5
x = -9
y = 1 / 2
n = 2
print('0.5.5: Comprehension over {1,2,3,4,5}, squaring each element of the set')
S = {1, 2, 3, 4, 5}
print({x**n for x in S})
print()

# 0.5.6
x = -9
y = 1 / 2
n = 2
print('0.5.6: Comprehension over {{0,1,2,3,4}}, where each element is a power of {}'.format(n))
S = {0, 1, 2, 3, 4}
print({n**x for x in S})
print()

# 0.5.7
S = {1, 4, 5}
T = {2, 3, 7}
print('0.5.7: Comprehension involving multiplication over 2 three element sets that results in a 9 element set')
print({x * y for x in S for y in T})
print()

# 0.5.8
S = {0, 3, 6}
T = {1, 2, 4}
print('0.5.8: Comprehension with 2 disjoint (non-overlapping) sets that results in a set of 5 elements')
print({x * y for x in S for y in T})
print()

# 0.5.9
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
print('0.5.9: Comprehension that is intersection of 2 sets, without using intersection operator')
print({x for x in S for y in T if x == y})
print()

# 0.5.10
L = [20, 10, 15, 75]
print('0.5.10: The average of the elements in L ({})'.format(L))
print(sum(L) / len(L))
print()

# 0.5.11
L = ['A', 'B', 'C']
M = [1, 2, 3]
print('0.5.11: A list comprehension that is the Cartesion product of L ({}) and M ({})'.format(L, M))
print([[x, y] for x in L for y in M])
print()

# 0.5.12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
print('0.5.12: The sum of a list of lists ({})'.format(LofL))
print(sum([sum(x) for x in LofL]))
print()

# 0.5.13
#[a, b] = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
print('0.5.13: Find out what happens if the sides of an unpacking operation don\'t match')
print('An unpack error is thrown')
print()

# 0.5.14
S = {-4, -2, 1, 2, 5, 0}
print('0.5.14: Three element tuples over S ({}) such that the elements sum to 0'.format(S))
print([(x, y, z) for x in S for y in S for z in S if sum([x, y, z]) == 0])
print()

# 0.5.15
S = {-4, -2, 1, 2, 5, 0}
print('0.5.15: As above, but don\'t include (0, 0, 0)')
print([(x, y, z) for x in S for y in S for z in S if sum([x, y, z]) == 0 and (x, y, z) != (0, 0, 0)])
print()

# 0.5.16
S = {-4, -2, 1, 2, 5, 0}
print('0.5.16: As above, but only get the first tuple')
print([(x, y, z) for x in S for y in S for z in S if sum([x, y, z]) == 0 and (x, y, z) != (0, 0, 0)][0])
print()

# 0.5.17
L = [0, 0, 1, 2]
print('0.5.17: Provide an example wherein len(L) is different from len(list(set(L)))')
print('len(L) {}'.format(len(L)))
print('len(list(set(L))) {}'.format(len(list(set(L)))))
print()

# 0.5.18
print('0.5.18: Using range(), provide the set of odd integers from 1 to 99')
print({n for n in list(range(100))[1::2]})
print()

# 0.5.19
L = ['A', 'B', 'C', 'D', 'E']
print('0.5.19: List of tuples of L ({}) and each letter\'s index, without using a comprehension'.format(L))
print(list(zip(L, range(len(L)))))
print()

# 0.5.20
L = [10, 25, 40]
M = [1, 15, 20]
print('0.5.20: List comprehension over L ({}) and M ({}), summing ith element of each'.format(L, M))
print([sum([x, y]) for x, y in zip(L, M)])
print()

# 0.5.21
dlist = [{'James': 'Sean', 'director': 'Terence'}, {'James': 'Roger', 'director': 'Lewis'}, {'James': 'Pierce', 'director': 'Roger'}]
k = 'James'
print('0.5.21: List comprehension over dlist ({}), pulling k ({}) from each'.format(dlist, k))
print([d[k] for d in dlist])
print()

# 0.5.22
print('0.5.22: As above, but handle cases with dictionaries that don\'t contain the supplied key')
dlist = [{'Bilbo': 'Ian', 'Frodo': 'Elijah'}, {'Bilbo': 'Martin', 'Thorin': 'Richard'}]
k = 'Bilbo'
print([d[k] if k in d else 'NOT PRESENT' for d in dlist])
k = 'Frodo'
print([d[k] if k in d else 'NOT PRESENT' for d in dlist])
print()

# 0.5.23
print('0.5.23: Dictionary comprehension with keys 0-99 and the values being the squares of the key')
print({k:(k**2) for k in list(range(100))})
print()

# 0.5.24
S = ('red', 'white', 'blue')
print('0.5.24: Dictionary comprehension that is the identity function for S ({})'.format(S))
print({k:k for k in S})
print()

# 0.5.25
print('0.5.25: Dictionary comprehension with keys 0-999 with each value being a list of the digits in the key')
base = 10
digits = set(range(10))
print({k * base**2 + j * base + i:[k, j, i] for k in digits for j in digits for i in digits})
#print({k:[k // base**2, (k % base**2 - k % base) // base, k % base] for k in digits})
print()

# 0.5.25.a
print('0.5.25.a: Dictionary comprehension with keys 0-1 with each value being a list of the digits in the key')
base = 2
digits = {0, 1}
print({k * base**2 + j * base + i:[k, j, i] for k in digits for j in digits for i in digits})
print()

# 0.5.26
id2salary = {0: 1000.0, 3:990, 1:1200.50}
names = ['Frodo', 'Bilbo', 'Golem']
print('0.5.26: Dictionary comprehension mapping employee names ({}) to salaries'.format(names))
print({names[id]: salary for (id, salary) in id2salary.items() if id < len(names) - 1})
print()

# 0.5.27
print('0.5.27: Define a procedure called twice()')
def twice(zTwice): return zTwice * 2;
print(twice(4))
print(twice([2, 4, 5]))
print(twice('chars or cars'))
#print(zTwice)  # Throws "NameError: name 'zTwice' is not defined" error
print()

# 0.5.28
print('0.5.28: Define a procedure that returns a list each of whose elements are one more than those passed')
def nextInts(L): return [x + 1 for x in L];
L = [1, 5, 7]
print(nextInts(L))
print()

# 0.5.29
print('0.5.29: Define a procedure that returns a list each of whose elements are the cubes of those passed')
def cubes(L): return [x ** 3 for x in L];
L = [1, 2, 3]
print(cubes(L))
print()

# 0.5.30
dct = {'a': 'A', 'b': 'B', 'c':'C'}
keylist = ['a', 'b', 'c', 'd']
print('0.5.30: Define a procedure that returns the dictionary value ({}) associated with the ith element in a list ({})'. format(dct, keylist))
def dict2list(dct, keylist): return [dct[k] for k in keylist if k in dct];
print(dict2list(dct, keylist))
print()

# 0.5.31
keylist = ['a', 'b', 'c']
L = ['A', 'B', 'C']
print('0.5.31: Define a procedure that returns a dictionary generated from the supplied keys ({}) and values ({})'. format(keylist, L))
def lists2dict(keylist, L): return {k: v for k, v in zip(keylist, L)};
print(lists2dict(keylist, L))
print()

# 0.5.32
print('0.5.31: Define a procedure that returns the base 10 representation of 3 digit values for the supplied base')
def all_3_digit_numbers(base, digits): return {k * base**2 + j * base + i for k in digits for j in digits for i in digits}
# 0.5.32.a
base = 2
print('For base {}'.format(base))
print(all_3_digit_numbers(base, set(range(base))))
# 0.5.32.b
base = 3
print('For base {}'.format(base))
print(all_3_digit_numbers(base, set(range(base))))
# 0.5.32.c
base = 10
print('For base {}'.format(base))
print(all_3_digit_numbers(base, set(range(base))))
print()
