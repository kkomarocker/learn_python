"""learning range"""

# Stop value is one-past-the-end
range(5) # range(0, 5)

for i in range(5):
    print(i) # 0 1 2 3 4

# ranges are "half-open"; start is included but stop is not
# stop value of a range used as start value of consecutive range
# optional third step value -> range(start, stop, step)

list(range(5, 10)) # [5, 6, 7, 8, 9] (10 is not included in the list)
list(range(10, 15)) # [10, 11, 12, 13, 14] (10 is included this time..)
list(range(0, 10, 2)) # [0, 2, 4, 6, 8] (increments by 2 since 2 is given as a step value in range)

# Avoid range() for iterating over lists at all cost.
# Python is not C.
# Prefer direct iteration over iterable objects, such as lists

# BAD
s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(s[i])

# GOOD
for v in s:
    print(v) # 0 1 4 6 13

# Not using range - enumerate
# Prefer enumerate() for counters
# enumerate() yields (index, value) tuples

t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print(p) # (0, 6), (1, 372), (2, 8862), (3, 148800), (4, 2093886)

# Or, combine with tuple unpacking..
for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v)) # (i = 0, v = 6), (i = 1, v = 372), (i = 2, v = 8862), (i = 3, v = 148800), (i = 4, v = 2093886)
