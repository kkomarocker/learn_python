"""learning dict"""

# Delimited by { and }.
# Key-value pairs comma separated.
# Corresponding keys and values joined by colon.
# Keys must be unique
# Keys are immutable, while values are mutable.

# dict() constructor
# Iterable series of key-value 2 tuples
names_and_ages = [ ('Alice', 32), ('Bob', 48) ]
d = dict(names_and_ages)
print(d) # { 'Alice': 32, 'Bob': 48 }

phonetic = dict(a = 'alpha', b = 'bravo', c = 'charlie')
print(phonetic) # { 'a': 'alpha', 'c': 'charlie', 'b': 'bravo' }

# Copying
# Use either copy() method or dict() constructor with original dict collection as an argument.

d = dict(goldenrod = 0xDAA520, indigo = 0x4B0082, seashell = 0xFFF5EE)
print(d) # { 'indigo': 4915330, 'seashell': 16774638, 'goldenrod': 14329120 }

e = d.copy()
print(e) # { 'indigo': 4915330, 'seashell': 16774638, 'goldenrod': 14329120 }

f = dict(e)
print(f) # { 'indigo': 4915330, 'seashell': 16774638, 'goldenrod': 14329120 }

# Extend a dictionary by using update() method.
g = dict(wheat = 0xF5DEB3, khaki = 0xF0E68C, crimson = 0xDC143C)
f.update(g)
print(f) # { 'indigo': 4915330, 'wheat': 16113331, 'crimson': 14423100, 'khaki': 15787660, seashell': 16774638, 'goldenrod': 14329120 }

# update() method replaces values corresponding to duplicate keys.
stocks = { 'GOOG': 891, 'AAPL': 416, 'IBM': 194 }
stocks.update({ 'GOOG': 894, 'YHOO': 25 })
print(stocks) # { 'GOOG': 894, 'AAPL': 416, 'YHOO': 25, IBM': 194 }

# Iteration.
# iterates over keys.
# get corresponding value with d[key] lookup
# returns order in arbitrary.

numbers = { 'a': 1, 'b': 2, 'c': 3 }
for key in numbers:
    print("{key} => {value}".format(key = key, value = numbers[key]))

# Use values() method for an iterable view onto the series of values in dictionary.
# No efficient way to get the key corresponding to a value.
# keys() method gives iterable view onto keys - not often needed.
for value in numbers.values():
    print(value) # 1 2 3

for key in numbers.keys():
    print(key) # 'a' 'b' 'c'

# Use items() method for an iterable view onto the series of key-value tuples.
# Use with tuple unpacking.
for key, value in numbers.items():
    print("{key} => {value}".format(key = key, value = value))

# Membership
# check membership using in and not in operator on the keys. (not values!)
symbols = dict(usd = '\u0024', gbp = '\u00a3', nzd = '\u0024')
print('nzd' in symbols) # True
print('mkd' in symbols) # False

# Delete element using del() method by key.
# del d[key]
z = { 'H': 1, 'Tc': 43, 'Xe': 54, 'Un': 137 }
del z['Un']
print(z) # { 'H': 1, 'Tc': 43, 'Xe': 54 }

# Mutability
# keys must be immutable while values may be mutable.
m = { 
        'H': [1, 2, 3],
        'He': [3, 4],
        'Li': [6, 7],
        'Be': [7, 9, 10]
    }

m['H'] += [4, 5, 6, 7]

print(m) 
# { 
#     'H': [1, 2, 3, 4, 5, 6, 7],
#     'He': [3, 4],
#     'Li': [6, 7],
#     'Be': [7, 9, 10]
# }

m['N'] = [13, 14, 15]
print(m)
# { 
#     'H': [1, 2, 3, 4, 5, 6, 7],
#     'He': [3, 4],
#     'Li': [6, 7],
#     'Be': [7, 9, 10],
#     'N': [13, 14, 15]  
# }

# Use pprint module by importing standard library named pprint.

from pprint import pprint as ppr
ppr(m)
# { 
#     'H': [1, 2, 3, 4, 5, 6, 7],
#     'He': [3, 4],
#     'Li': [6, 7],
#     'Be': [7, 9, 10],
#     'N': [13, 14, 15]  
# }