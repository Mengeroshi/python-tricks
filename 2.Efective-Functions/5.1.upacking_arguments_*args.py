"""
Unpacking data structures without for
"""
def print_vector(x, y, z):
    print('<%s, %s, %s>' %(x, y, z))

print_vector(0, 1, 0)

tuple_vec = (1, 0, 1)

list_vec = [1, 0, 1]
"""
print_vector(tuple_vec[0], tuple_vec[1],tuple_vec[2])
"""
#unpacking
print_vector(*tuple_vec)
print_vector(*list_vec)

#generator expressions
genexpr = (x * x for x in range(3))

print_vector(*genexpr)