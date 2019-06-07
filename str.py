"""learning str in python"""

# len(str) gives the length of string passed as an argument.
len("hello") # 5

# concatenate
"hello " + "my name is" + " Jay" # "hello my name is Jay"

# string augmentation
s = "Hello "
s += "my name is "
s += "Jay"

s == "Hello my name is Jay" # True

# join / split
colors = ";".join(['a', 'b', 'c'])
colors == "a;b;c" # True
colors.split(";") == ['a', 'b', 'c'] # True

# partition; it returns tuple
"unforgetable".partition("forget") == ("un", "forget", "able") # True
departure, separator, arrival = "London:Edinburgh".partition(":") # departure == "London", arrival == "Edinburgh"

# Underscore as a dummy name for the separator. This convention is understood by many tools.
origin, _, destination = "Seattle-Boston".partition('-') # origin == "Seattle", destination == "Boston"

# format; to insert values into strings
# replacement fields delimited by { and }
# integer field names matched with positional arguments
# field names can be omitted if used in sequence
# named fields are matched with keyword arguments
# access values through keys or indexes with square brackets in the replacement field
# access attributes using dot in the replacement field
# the replacement field mini-language provides many value and alignment formatting options

"The age of {0} is {1}".format("Jim", 32) # "The age of Jim is 32"
"Reticulating spline {} of {}".format(4, 23) # "Reticulating spline 4 of 23"
"Current position {latitude} {longitude}".format(latitude="60N", longitude="5E") # "Current position 60N 5E"

pos = (65.2, 23.1, 82.2)
"Galactic position x={pos[0]} y={pos[1]} z={pos[2]}" # "Galactic position x=65.2 y=23.1 z=82.2"

import math
'Math constants: pi={m.pi}, e={m.e}'.format(m = math) # 'Math constants: pi=3.141592653589793, e=2.718281828459045'
'Math constants: pi={m.pi:.3f}, e={m.e:.3f}'.format(m = math) # 'Math constants: pi=3.142, e=2.718'