"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):

    #convert all items to strings
    itemsAsStrings = []
    for x in items:
         itemsAsStrings.append (str(x))

    #count occurances of each string
    from collections import Counter
    frequencies = Counter (itemsAsStrings)
    return frequencies
