""" Random Module """
import random

# #to get a random number between 0-1 -- Not important
# print(random.random())

# #to get a floating point number between two specified numbers -- random.uniform(1,10)
# print(random.uniform(5,20))

# #to get an integar number
# print(random.randint(1,6))



# numbers_list = [1,2,3,"hola",'y', 26, "tuna"]

# #to get a random element from a list 
# print(random.choice(numbers_list))

# #to grap a number of random elements form a list
# print(random.choices(numbers_list, k=3))

# deck = [1,5,7,8,9,6,2]
# #to grap a number of unique random elements form a list 
# random.shuffle(deck) # to shuffle up a list
# print(random.sample(deck, k=4))


i = 4
d = 4.0
s = 'HackerRank ' 

int_input = 12
double_input = 4.0
con_input = 'is the best place to learn and practice coding!'

print('{}\n{:01}\n{}'.format(int_input+i, double_input+d, s+con_input))