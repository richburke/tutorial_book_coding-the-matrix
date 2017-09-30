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
