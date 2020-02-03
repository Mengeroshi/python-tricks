""" Clousures - remember the value of its lexical scope """
def get_speak_func(text,volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '...'
    if volume > 0.5:
        return yell#if I put parenthesis here I don't need use in print
    else:
        return whisper

print(get_speak_func('hello, world', 0.7)())


def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))