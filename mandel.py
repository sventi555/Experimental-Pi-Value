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
