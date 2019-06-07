"""Comprehension"""

words = "this is something cool".split() # ['this', 'is', 'something', 'cool']
[len(word) for word in words] # [4, 2, 9, 4]

from math import factorial

# List Comprehension
[len(str(factorial(x))) for x in range(20)] # [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]

# Set Comprehension
{ len(str(factorial(x))) for x in range(20) } # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}

# Dictionary Comprehension
from pprint import pprint as pp

country_to_capital = { 
    "UK": "London",
    "USA": "DC",
    "Korea": "Seoul"
}

capital_to_country = { capital: country for country, capital in country_to_capital.items() }
pp(capital_to_country) 
# { 
#   'DC': 'USA', 
#   'London': 'UK', 
#   'Seoul': 'Korea'
# }

# Filtering predicates
# Works with list, set, and dictionary comprehensions
# To perform filtering, simply pass optional third argument inside comprehension.
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print([x for x in range(101) if is_prime(x)]) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Iteration Protocols
iterable = ["Spring", "Summer", "Autumn", "Winter"]
iterator = iter(iterable)
next(iterator) # "Spring"
next(iterator) # "Summer"
next(iterator) # "Autumn"
next(iterator) # "Winter"

# Generator
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123() # g now became generator object.
next(g) # 1
next(g) # 2
next(g) # 3
next(g) # throws an exception; StopIteration.

# every generator object are different; can be used differently.