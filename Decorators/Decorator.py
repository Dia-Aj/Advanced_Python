"""
Decorator is a function that takes another as an argument add some kind
of functionality and returns another function without attering the source 
code of the original function you passed in.
""" 

#Closures and first class functions quick recap
def decorator_function(msg):
	def wrapper_function():
		print(msg)
	return wrapper_function

say_hi = decorator_function('hi')
say_hi()

#Decoratoes	

def decorator_function(original_function):
	""" Decorator Function """
	def wrapper_function(*args, **kwargs): #We userd args and kwargs here to make the arguments flexible 
		print('wrapper executed this first {}'.format(original_function.__name__))
		return(original_function(*args, **kwargs)) 
	return wrapper_function

#Decorator function rewritten as class
class decorator_class():
	""" Decotrator Class """
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('call method executed this first {}'.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs) 
		
""" @decorator_function == (display = decorator_function(display))
We don't need to write "display = decorator_function(display)",  instead
we just replace it with @decorator_function """
@decorator_function
def display():
	print("display function ran")

#We type @decorator_function with any function we want it to work as a decorator
"""
make sure to place the right number of arguments, the best pratice of this is to
put (*arg and **kwargs) in the wrapper function inside the decorator function
""" 

#@decorator_function
@decorator_class
def display_info(name, age):
	print(f'display_info function ran with arguments ({name}, {age})')

# display = decorator_function(display) #We no longer need this one
display()
display_info('Victoria', 18)

print('*'*20)
#Real examples on decorator 
from functools import wraps

#loggers are used to track changes
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    @wraps(orig_func) #We use it when we run 2 decorators together so it keeps working properly 
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

"""
if we used more than 1 decorator and didn't use @warps(funcName), 
the output will be written in a different file called wrapper.info. 
We must include that wrapper in order to avoid that bug. 
"""

def my_timer(orig_func):
    import time
    @wraps(orig_func) #We use it when we run 2 decorators together so it keeps working properly 
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


import time

@my_logger
@my_timer
def display_info(name, age, **kwargs):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Victoria', 14, country = 'Scotland')

"""
When we run my_logger with my_timer together we get into trouble that the output will be written in another file called wrapper.txt
to avoid this we import wraps from functools and place it above each wrapper we have. 
"""


