import math
import random

while True:
    x=[]
    y=[]
    z=[]

    numInt=int(input("How many pairs of integers?"))
    maxVal=int(input("What is the max value?"))
    for i in range(numInt):
        x.append(random.randint(1, maxVal))
        #creates a list of random variables of length numInt
        
    for i in range(numInt):
        y.append(random.randint(1, maxVal))
        #creates another list of the same length
        
    for i in range(len(x)-1):
        if math.gcd(x[i], y[i])==1:
            z.append(1)
            #creates a list of '1's for every pair of coprimes in x and y
            
    probCp=len(z)/len(x)
    result=math.sqrt(6/probCp)
    #calculates an experimental value for pi
    
    print('the value for pi is: ' + str(result))
    percentError=(abs(math.pi-result))/math.pi
    print('the percent error is: ' + str(percentError*100))
    #prints a value for the experimental value of pi and the percent error
    
    print('would you like to run program again?')
    prompt=input('type y/n: ')
    if prompt=='y':
        print(' ')
        continue
    else:
        break
    #prompt to run the program again, otherwise it breaks

