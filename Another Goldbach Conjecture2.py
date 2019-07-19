import time
import math
start = time.time()
primelist= [2]
goldbach_found =[]

def primefinder(number):
    import time
import math
start = time.time()
primelist= [2]
largest_sum = []

def primefinder(number):
    prime = [True] * (number+1)
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            primelist.append(y)
            for x in range(y+y, number + 1,y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if prime[x] == True:
            primelist.append(x)

primefinder(1000000)

def prime_summation(y):
    for x in primelist:
       if y + x < 1000000:
           y += x
       else:
           largest_sum.append(y)
           break

prime_summation(0)

def Consecutive_prime_sum(number):
    for x in range(-1,-534634,-1):
        if primelist[x]-number < 0:
            print(primelist[x])
            break

Consecutive_prime_sum(largest_sum[0])

end = time.time()
print(end - start)
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            primelist.append(y)
            for x in range(y+y, number + 1,y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if prime[x] == True:
            primelist.append(x)

number= 20000
primefinder(number)

def goldbach_checker(number):
    z = 4
    while z < number-2:
        for x in primelist:
            if x >= z:
                break
            for y in primelist:
                if y >= z:
                    break
                if x+y >= number or x+y > z:
                    break
                if x >= y:
                    if x+y == z:
                        print(str(x) + "+" + str(y) + "=" + str(x+y))
                        z += 2
                        goldbach_found.append(x+y)
                        break
                else:
                    break

goldbach_checker(number)

if len(goldbach_found) != (number/2)-2:
    print("Goldbach Conjecture disproved")


end = time.time()
print(end - start)
