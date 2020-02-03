def speak(text):
    def whisper(t):#whisper don't exist outside
        return t.lower() + '...'
    return whisper(text)

def get_speak_func(volume):
    def whisper(t):#whisper don't exist outside
        return t.lower() + '...'
    def yell(text):
        return text.upper()+'!'
    if volume > 0.5:
        return yell
    else:
        return whisper

print(get_speak_func(0.3))
print(get_speak_func(0.7))

speaking = get_speak_func(0.7)
print(speaking('hello'))