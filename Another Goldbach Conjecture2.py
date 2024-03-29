import time
import math
start = time.time()
primelist= []
goldbach_found =[]

def primefinder(number):
    prime = [True] * (number+1)
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            primelist.append(y)
            for x in range(y*y, number + 1,y*y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if prime[x] == True:
            primelist.append(x)

number= 20000
primefinder(number)

def goldbach_checker(number):
    z = 6
    while z < number:
        for x in primelist:
            if x >= z:
                break
            for y in primelist:
                if x+y > z:
                    break
                if x+y == z:
                    print(str(x) + "+" + str(y) + "=" + str(x+y))
                    z += 2
                    if z == number:
                        return None
                    goldbach_found.append(x+y)
                else:
                    continue

goldbach_checker(number)

if len(goldbach_found) != (number/2)-4:
    print("Goldbach Conjecture disproved")

end = time.time()
print(end - start)
