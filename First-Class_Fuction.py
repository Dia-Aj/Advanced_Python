#In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizen

"""
In programming language design, a first-class citizen (also type, object, entity, or value) in a given programming language is
an entity which supports all the operations generally available to other entities. 
These operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable.
"""

""" First-Class citizen """
# def square(x):
# 	return (x*x)

# def cube(x):
# 	return (x*x*x)	

# a = square #without parenthese
# print(a(5))

# def my_map(func, arg_list):
# 	result = []
# 	for i in arg_list:
# 		result.append(func(i))
# 	return result	

# print(my_map(cube, [1,2,3,4,5]))

""" First-Class Function """

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')