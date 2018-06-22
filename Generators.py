""" Example On Generators """
#Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
#Note: Please note that in real life, integers do not take up that much space, unless they are really, really, really, big integers.
#For instance you can represent a 309 digit number with 128 bytes (add some overhead, it will still be less than 150 bytes).



###########################################

##Build and return a list##
# def firstn(n):
# 	num, nums = 0, []
# 	while num < n:
# 		nums.append(num)
# 		num += 1
# 	return nums
  
# sum_of_first_n = sum(firstn(1000000))
# print(sum_of_first_n)

#This is clearly not acceptable in our case, because we cannot afford to keep all n "10 megabyte" integers in memory.

#Using the generator pattern (an iterable)
# class firstn(object):
#     def __init__(self, n):
#         self.n = n
#         self.num, self.nums = 0, []

#     def __iter__(self):
#         return self

#     # Python 3 compatibility
#     def __next__(self):
#         return self.next()

#     def next(self):
#         if self.num < self.n:
#             cur, self.num = self.num, self.num+1
#             return cur
#         else:
#             raise StopIteration()

# sum_of_first_n = sum(firstn(1000))
# print(sum_of_first_n)

# This will perform as we expect, but we have the following issues:
##### there is a lot of boilerplate
##### the logic has to be expressed in a somewhat convoluted way
##### Furthermore, this is a pattern that we will use over and over for many similar constructs. Imagine writing all that just to get an iterator.

##############################################

#Python provides generator functions as a convenient shortcut to building iterators. 
#Lets us rewrite the above iterator as a generator function:

# a generator that yields items instead of returning a list
# def firstn(n):
# 	num = 0
# 	while num < n:
# 		yield num
# 		num += 1

# sum_of_first_n = sum(firstn(1000000))

#list comprehension as generator
# my_nums = (i*i for i in range(1000)) #Note: parentheses() not brackets []
# print(*my_nums, sep = ", ")