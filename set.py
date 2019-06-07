"""learning set"""

# Literals
# Delimited by { and }
# Single comma separated items
# Empty {} makes a dict collection. For empty set, use the set() constructor

p = { 6, 28, 496, 8128, 33550336 }
print(type(p)) # <class 'set'>

d = {}
print(type(d)) # <class 'dict'>

# Set constructor accepts:
# Iterable series of values
# Duplicates are discarded
# Often used specifically to remove duplicates - not order preserving

s = set([2, 4, 16, 64, 4096, 65536, 262144])
print(s) # { 2, 4, 16, 64, 4096, 65536, 262144 }

t = set([1, 4, 2, 1, 7, 9, 9])
print(t) # { 1, 2, 4, 9, 7 } // removes duplicates!

for val in t:
    print(val) # 1 2 4 7 9 // order is arbitrary.

# Check membership by using in and not in operators.
print(1 in t) # True
print(4 not in t) # False

# Adding elements
# Use add() method by passing a value as an argument.
# Duplicates are silently ignored.

k = { 81, 108 }
k.add(10)
print(k) # {81, 10, 108}

# For multiple elements, use update() method by passing any iterable series.
k.update([1, 2, 3])
print(k) # { 1, 2, 3, 10, 108, 81 }

# Removing elements
# use remove() method by passing value that is present in the set, otherwise it will raise KeyError.
# discard() method is similar to remove() method, except it won't raise any error whether the passed value is presented in the set or not.

k.remove(3)
print(k) # { 1, 2, 10, 108, 81 }

k.discard(200) # won't effect anything in the set.

# Copy set by using copy() method or set() constructor.
j = k.copy()
print(j) # { 1, 2, 10, 108, 81 }

d = set(k)
print(d) # { 1, 2, 10, 108, 81 }

# Union
# joins two sets
# Commutative

blue_eyes = { 'Olivia', 'Harry', 'Lily', 'Jack' }
blond_hair = { 'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua' }
smell_hcn = { 'Harry', 'Amelia' }
taste_ptc = { 'Harry', 'Lily', 'Amelia', 'Lola' }
o_blood = { 'Mia', 'Joshua', 'Lily', 'Olivia' }
b_blood = { 'Amelia', 'Jack' }
a_blood = { 'Harry' }
ab_blood = { 'Joshua', 'Lola' }

print(blue_eyes.union(blond_hair)) # { 'Jack', 'Harry', 'Lily', 'Olivia', 'Joshua', 'Mia', 'Amelia' }
print(blond_hair.union(blue_eyes)) # same result as blue_eyes.union(blond_hair) // { 'Jack', 'Harry', 'Lily', 'Olivia', 'Joshua', 'Mia', 'Amelia' }

# Intersection
# returns set of values where values are equally presented in two different sets
# Commutative
print(blond_hair.intersection(blue_eyes)) # {'Jack', 'Harry'}
print(blond_hair.intersection(blue_eyes) == blue_eyes.intersection(blond_hair)) # True

# Difference
# returns set values where values in the first set does not present in the second set passed as an argument of difference() method.
# Non-Commutative
print(blond_hair.difference(blue_eyes)) # { 'Mia', 'Amelia', 'Joshua' }
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair)) # False

# Symmetric_difference
# returns set of values where value presents only in the one set but not both.
# Commutative
print(blond_hair.symmetric_difference(blue_eyes)) # { 'Mia', 'Lily', 'Amelia', 'Olivia', 'Joshua' }
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair)) # True

# Issubset
# returns bool if the one set is subset of the other set that is passed as an argument in issubset() method.
print(smell_hcn.issubset(blond_hair)) # True

# Issuperset
# returns bool if the one set contains all of values in the other set passed as an argument in issuperset() method.
print(taste_ptc.issuperset(smell_hcn)) # True

# Isdisjoint
# returns bool if two different set has no intersecting values.
print(a_blood.isdisjoint(o_blood)) # True