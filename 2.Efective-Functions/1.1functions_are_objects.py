def yell(text):
    return text.upper()+'!'

print(yell('hello'))

bark = yell
print(bark('wooof'))

del yell

#print(yell('hello'))

print(bark.__name__)