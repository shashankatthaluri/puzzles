import math
a = 1 
b = 100 # total number of doors 
def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1) 
print("total number of doors open is:", int(CountSquares(a, b)))
