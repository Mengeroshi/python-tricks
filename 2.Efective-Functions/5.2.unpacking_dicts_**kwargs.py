def print_vector(x, y, z):
    print('<%s, %s, %s>' %(x, y, z))

dict_vec ={
    'y': 0,
    'z': 1,
    'x': 1,
}

print_vector(*dict_vec)#ramdom order
print_vector(**dict_vec)

