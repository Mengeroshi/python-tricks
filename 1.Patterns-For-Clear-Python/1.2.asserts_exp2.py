def do_x(x):
    print(x)

def do_y(y):
    print(y)



def check(cond):
    if cond == 'x':
        do_x(cond)
    elif cond == 'y':
        do_y(cond)
    else:
        assert False, ('Damn! it's imposible to this to happend')
x = 'x'
y = 'y'
z = 'z'

check(x)
check(y)
check(z)