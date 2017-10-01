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
