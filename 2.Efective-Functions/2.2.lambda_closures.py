def make_adder(n):
    return lambda x: x + n

plus_10 = make_adder(10)

plus_5 = make_adder(5)

print(plus_10(20))
print(plus_5(3))