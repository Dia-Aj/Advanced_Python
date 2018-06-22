#name tuples are used to clarify the content of a tuple and giving each one a name
from collections import namedtuple

color = (55, 155, 255) #-> unreadable
#in that case it's not recommended to use a dictionary because it would be little harder and inappropriate if we had more values
#we instead use named tuples

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)

print(color.red) 

#######################################################

Stocks = namedtuple('Stocks', ['Oil', 'Gold', 'Bitcoin', 'Hippty'])
stocks = Stocks(+22.2, -11.5, +0.85, -2.5)
print(stocks.Gold)

#######################################################

Prices = namedtuple('myPrices', ['vr', 'laptop', 'headphones'])
prices = Prices(50.20, 500.60, 20)
print(Prices)
print(Prices.__dict__)