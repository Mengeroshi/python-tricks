""" 
Groups multiple dictionaries into single mapping.
insertions, updates and deletions only affect to the first added
"""

from collections import ChainMap

dict1 =  {'one': 1, 'two':2 }
dict2 = {'three': 3, 'four': 4}

chain = ChainMap(dict1, dict2)

print(chain)

print(chain['three'])

print(chain['one'])

print(chain['missing'])