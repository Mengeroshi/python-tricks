from string import Template

name = 'Bob'

t = Template('Hey, $name!')

print(t.substitute(name=name))
