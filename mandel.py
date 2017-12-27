#This determines pi by reitterating z^2 + c, with c as a constant E away from 0.25 and z starts at 0. 
#Pi comes from the number of times this itteration is run before the value of z^2 + c >= 2 multiplied by the square
#root of E. Enjoy.

import math

def mandel(E):
    z = 0
    c = 0.25 + E
    counter = 1

    while True:
        if (z**2 + c) <= 2:
            counter += 1
            z = (z**2 + c)
        else:
            break
    print(counter * math.sqrt(E))

mandel(10**-14)
