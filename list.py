""" learning list """

# Access element by using bracket.
# Zero and positive integers for indexing from the front.
# Negative integers index from the end.
# The last element is at index -1.
# Avoid seq[len(seq) - 1].

s = "show how to index into sequences".split() # ['show', 'how', 'to', 'index', 'into', 'sequences']
print(s[4]) # 'into'
print(s[-5]) # 'how'

# Slicing extracts part of a list.
# Syntax -> seq[start:stop]
# Slice range is half-open; stop not included.
# Slicing works with negative indexes.
# Omitting the stop index slices to the end.
# Omitting the start index slices from the beginning.

print(s[1:4]) # ['how', 'to', 'index']
print(s[1:-1]) # ['how', 'to', 'index', 'into']
print(s[3:]) # ['index', 'into', 'sequences']
print(s[:3]) # ['show', 'how', 'to']

# Omitting both start and stop index slices from the beginning to the end - full slice. (important idiom for copying lists)
# Alternatives; use copy() method on given list or list() constructor which accepts given list as an argument.

full_slice = s[:]

print(s[:]) # ['show', 'how', 'to', 'index', 'into', 'sequences']

full_slice is s # False
full_slice == s # True

u = s.copy() # copies s
v = list(s) # created another list object for s

# Repeat lists using the * operator
# Most often used for initializing a list of know size with a constant; s = [constant] * size
# Multiple references to one instance of the constant in the produced list

c = [21, 37]
d = c * 4
print(d) # [21, 37, 21, 37, 21, 37, 21, 37]
print([0] * 9) # [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Find element.
# Use index() to obtain index of given argument.
w = "the quick brown fox jumps over the lazy dog".split() # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
i = w.index('fox')
print(i) # 3
print(w[i]) # 'fox'
print(w.index('unicorn')) # this will throw a ValueError
print(w.count('the')) # returns the counts of matching element. In this case 2 since there is 2 'the' in the list.

# in and not in operator to test the membership
print(37 in [1, 78, 9, 37, 32, 53]) # True
print(78 not in [1, 78, 9, 37, 32, 53]) # False

# Delete element using del method.
# Alternatively, use remove() with designated value to be removed from the list.
del w[3]
print(w) # ['the', 'quick', 'brown', 'jumps', 'over', 'the', 'lazy', 'dog']
w.remove('dog')
print(w) # ['the', 'quick', 'brown', 'jumps', 'over', 'the', 'lazy']

# Insert items with insert() method.
# Insert method accepts two arguments; insert(index, item)
w.insert(2, "one") # ['the', 'quick', 'one', 'brown', 'jumps', 'over', 'the', 'lazy']

# Concatenate lists with + operator
# Alternatively, use += to extend list in-place or use extend() method which accepts one arguments; extend(seq)
m = [2, 1, 3]
n = [4, 7, 11]
k = m + n 
print(k) # [2, 1, 3, 4, 7, 11]

k += [18, 29, 47]
print(k) # [2, 1, 3, 4, 7, 11, 18, 29, 47]

k.extend([76, 129, 199])
print(k) # [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 129, 199]

# Reverse and Sort
# reverse() method reverses the list in-place
# sort() method sorts the list in-place

g = [1, 2, 3, 4, 5]
print(g.reverse()) # [5, 4, 3, 2, 1]

d = [5, 17, 2, 6, 3]
print(d.sort()) # [2, 3, 5, 6, 17]

# Passing reverse=True will sort in descending order.
e = [3, 2, 10, 8, 1]
print(e.sort(reverse=True)) # [10, 8, 3, 2, 1]

# Key argument to sort() method accepts a function for producing a sort key from an item.
z = "not perflexing do handwriting family where I illegibly know doctors".split()
print(z) # ['not', 'perflexing', 'do', 'handwriting', 'family', 'where', 'I', 'illegibly', 'know', 'doctors']

print(z.sort(key=len)) # ['I', 'do', 'not', 'know', 'where', 'family', 'doctors', 'illegibly', 'perflexing', 'handwriting']

print(' '.join(z)) # 'I do not know where family doctors illegibly perflexing handwriting'

# Built-in sorted() and reversed() function.
# sorted() sorts any iterable series and returns a list.

r = [4, 9, 2, 1]
q = sorted(r)
print(q) # [1, 2, 4, 9]
print(r) # [4, 9, 2, 1]

# reversed() built-in function reverses any iterable series.
p = [9, 3, 1, 0]
w = reversed(p)
print(w) # returns a reverse iterator
print(list(w)) # [0, 1, 3, 9]