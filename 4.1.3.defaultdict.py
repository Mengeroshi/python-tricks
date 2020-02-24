""" default dict is dict subclass that returns a callable if the key cannot be found """

from  collections import defaultdict

dd = defaultdict(list)

dd['dogs'].append('Rufus') # <---accessing to missimg key creates it and initializes it using default factory
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

print(dd['dogs'])
print(dd)