""" Duck typing and Asking Forgiveness, Not Permission (EAFP) """

class duck:

	def quack(self):
		print('Quack, Qauck')

	def fly(self):
		print('Flap, Flap')

class perosn:

	def quack(self):
		print('I\'m quacking like a Duck')

	def fly(self):
		print('I\'m flaping like a Duck')

def quack_and_fly(thing):
		
	#If it quacks like a duck then it's a duck-(Pythonic)-
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

d = duck()
p = perosn()
quack_and_fly(d)
print()
quack_and_fly(p)			


# #Not a duck-typed-(Non-Pythonic)-
# 	if isinstance(thing, duck):
# 		thing.quack()
# 		thing.fly()
# 	else:
# 		print('This has to be a duck')


#Look Before You Leap Method
#LBYL-(Non-Pythonic)-
# if hasattr(thing, 'quack'):
# 	if callable(thing.quack):
#     	thing.quack()

# if hasattr(thing, 'fly'):
# 	if callable(thing.fly):
# 		thing.fly()

#If it quacks like a duck then it's a duck-(Pythonic)-
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)