"""
Constrain your list to a single type
"""

import array

arr = array.array('f',(1.0, 1.5, 2.0, 2.5))

print(arr)

arr[1] = 23.0
print(arr)

del arr[1]
print(arr)

arr.append(42.0)
print(arr)


arr[1] = 'hello' # <----- arrays typed


