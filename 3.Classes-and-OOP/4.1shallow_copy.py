"""Shallow copy """
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

original_dict = {
    "x": 1,
    "y": 2,
    "z": 3,
}

original_set = (1,2,3)

new_list = list(original_list)

new_dict = dict(original_dict)

new_set = set(original_set)

xs = [[1,2,3], [4,5,6], [7,8,9]]
ys = list(xs)

print(ys)

xs.append(['new sublist'])

print(xs)
print(ys)
"""This happend because it's only a shallow copy """
xs[1][0] = 'x'
print(xs)#something change here
print(ys)#something change here too