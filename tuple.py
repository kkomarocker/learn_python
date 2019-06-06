"""This is script for tuple.
This file does nothing but showing how tuple is constructed.
"""

a = (1, 2, 3)
b = ("a", "b", 4)

# simple iteration
for num in a:
    print(num)

for val in b:
    print(val)

# elements can be accessed by using [index]
# a[1] = 2
# b[2] = 4

# length of tuple
print(len(a))
print(len(b))

# nested tuples
c = ((220, 1092), ("a", 1982), (9102, "d"))

# can't use one object in parentheses as a single element tuple
# for a single element tuple, include a trailing comma
c = (391,) # type will print as 'class <tuple>'
e = () # this will also print as 'class <tuple>!'

# destructuring / tuple unpacking

def minmax(items):
    return min(items), max(items)

minmax([33, 21, 11, 34, 82, 99, 13]) # this will give you (11, 82)

lower, upper = minmax([33, 21, 11, 34, 82, 99, 13]) # this will give you 11 for lower, 82 for upper

(a, (b, (c, (d)))) = (4, (3, (2, (1)))) # a = 4, b = 3, c = 2, d = 1...

# creating tuple using tuple constructor
tuple([1, 2, 3, 4]) # (1, 2, 3, 4)
tuple('Python!') # ("P", "y", "t", "h", "o", "n", "!")

# check whether value is valid in tuple using 'in' operator

5 in (3, 5, 6, 1, 20) # True
5 not in (3, 5, 6, 1, 20) # False
