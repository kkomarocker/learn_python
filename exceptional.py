"""A module for demonstrating exceptions"""
import sys
from math import log

def convert(s):
    """Convert to an integer"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), 
            file = sys.stderr)
        raise