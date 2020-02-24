"""
Creates proxy dictionaries (inmutable, only view dicts)
"""

from types import MappingProxyType

writable = {'one': 1, 'two': 2}

read_only =MappingProxyType(writable)

print(read_only['one'])

#read_only['one'] = 25 <--- READ ONLY

writable['one'] = 25

print(read_only)


