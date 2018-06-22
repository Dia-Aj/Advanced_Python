class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email1 = '{}.{}@gmail.com'.format(first, last) #we delete this in real projects as we 
        #created another email method but im keeping it for the sake of clarifying 

    @property
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    @fullname.setter
    def fullname(self, name):
    	first, last = name.split(' ')
    	self.first = first
    	self.last = last   

    @fullname.deleter
    def fullname(self):
    	print('Deleted Name!')
    	self.first = None
    	self.last = None	 

    @property
    def email(self):
    	return('{}.{}@gmail.com'.format(self.first, self.last))


emp_1 = Employee('John', 'Smith')
#here if we changed the first name it won't be change in the email

emp_1.first = 'Jim'
print(emp_1.fullname) #we treat it as an attribute
print(emp_1.email1)

#We use create a new method with property decorator to treat like attribute
#Now it works
print(emp_1.email)

#What if I want to change the full name like this:
#emp_1.fullname = "Taylor Swift"
#we declare a "@fullname.setter"

#Now it works
emp_1.fullname = "Taylor Swift"
print(emp_1.fullname)
print(emp_1.email)

#Now lets test the deleter
del emp_1.fullname