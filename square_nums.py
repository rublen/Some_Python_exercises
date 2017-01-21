'''
How many square numbers are between a (included) anb b (not included)?
'''

import math

def how_many_sqr(a, b):
    n = 0
    a = int(math.ceil(math.sqrt(a)))
    b = int(math.ceil(math.sqrt(b+1)))
    for c in range(a, b): 
        n += 1
    return n
    
print(how_many_sqr(1,10)) # 3
print(how_many_sqr(3,100)) # 9
print(how_many_sqr(1,10000)) # 100
print(how_many_sqr(999999917, 999999985)) # 0
