"""
str is an inmutable array
"""

arr = 'abcd'

print(arr[1])

print(arr)

#arr[1] = 'e' #<--- inmutable list

#del arr[1] #<--- inmutable list

#unpacked into a list

print(list(arr))

print(''.join(list('abcd')))