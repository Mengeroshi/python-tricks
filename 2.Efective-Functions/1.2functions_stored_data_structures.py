def yell(text):
    return text.upper()+'!'

bark = yell

funcs = [bark, str.lower, str.capitalize]

print(funcs)