with open('hello.txt', 'w') as f:
    f.write("hello, world!")

#another way to write same code of with

f = open('hello.txt', 'w')
try:
    f.write('hello world')
finally:
    f.close()