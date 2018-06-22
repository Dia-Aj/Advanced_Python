"""
Python special methods help to emulate a built-in behavior
in python and implement operator over loading

__init__ : Similar to constractors in C++.
__repr__ : the “official” representation as a string.
__str__ : the “informal” value as a string.
__add__: to overload add operator
__len__: to overload len operator
__doc__: returns the documentation of the class and also could be used with functions

"""
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): #The 'offical' representation to the object (used between developers)
    	return('Employee({}, {}, {})'.format(self.first, self.last, self.pay))
    	#it won't run as long as __str__ is in the code

    def __str__(self): #The 'informal' representation to the object (used with users)  
    	return('{} - {}'.format(self.fullname(), self.email))

    def __add__(self, other): #Over loads the + for this class
   		return(self.pay + other.pay)

   	def __len__(self):
   		return(len(self.fullname()))#full name could be replaced with what ever you want 	

dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

print(dev_1) 
"""
NOTE: when we have both '__repr__' and '__str__' the str method would take
the priorty to be executed and the repr will be as a fallback.	
"""
print(dev_1 + dev_2) #Return the summation of both developers
#print(len(dev_1))


