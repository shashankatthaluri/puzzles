import math
n = 10 # total number of people in a circle
K = 3 # Position who initiates the game. K must be less than n. 
def highestPowerof2(n):
    p = int(math.log(n, 2));
    return int(pow(2, p));
l = highestPowerof2(n) #nearest power of 2 to the total and l <= n.
r = 2*(n-l) + K
if r > n:
    rr = r - n
    print (rr)
else:
    print(r)
