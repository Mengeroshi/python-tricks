import copy
""" deep copies"""

xs = [[1,2,3], [4,5,6], [7,8,9]]
zs = copy.deepcopy(xs)

print(xs)
print(zs)

xs[1][0] = 'x'
print(xs)#something change here
print(zs)#Nothing change here cause is deep copy


""" shallow copies """
original = [[1,2,"obo"], [4,5,6], [7,8,"obo"]]
shallow = copy.copy(original)

print(original)
print(shallow)

original[0][2] = 3
print(original)
print(shallow)
