Person = {'name':'Jenn', 'age':23}
sentence1 = 'My name is {0} and I\'m {1} years old'.format(Person['name'], Person['age'])
sentence2 = 'My name is {0[name]} and I\'m {0[age]} years old'.format(Person)
sentence3 = 'My name is {name} and I\'m {age} years old'.format(**Person)
print(f'{sentence1}\n{sentence2}\n{sentence3}')

class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

P1 = Person("Jenn", 23)
sentence = 'My name is {0.name} and I\'m {0.age} years old.'.format(P1)
print(sentence)

sentence = 'My name is {name} and I\'m {age} years old.'.format(name = "Jenn", age = 23)
print(sentence)


""" Working With Numbers """

pi = 3.14159265
sentence1 = 'Pi is equal to {:.2f}'.format(pi)
sentence2 = 'Pi is equal to {:.5f}'.format(pi)
print(f'{sentence1}\n{sentence2}')

sentence = '1MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

a = [1, "k", 5, 4, "hello"]
print(*a, sep=",")





