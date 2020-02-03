""" 
    Function that can accept other functions as arguments are:
                HIGH ORDER FUNCTIONS
"""
def yell(text):
    return text.upper()+'!'

bark = yell


def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

greet(bark)

def whisper(text):
    return text.lower() + '...'

greet(whisper)
""" MAP """
obo = list(map(bark, ['hello', 'hey', 'hi']))

print(obo)