import time
import math
start = time.time()
primelist= [2]
goldbach_set = []

def primefinder(number):
    prime = [True for x in range(number + 1)]
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            primelist.append(y)
            for x in range(y+y, number + 1,y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if prime[x] == True:
            primelist.append(x)


def goldbach_conjecture():
    for x in primelist:
        for y in primelist:
            if x >= y:
                if (x + y) % 2 == 0:
                    print(str(x) + "+" + str(y) + "=" + str(x + y))
                    goldbach_set.append(x+y)
            else:
                break

def goldbach_conjecture_checker():
    for x in range(0,len(goldbach_set)):
        if goldbach_set[x] != 2*x+4:
            if goldbach_set[x] <= primelist[-1]:
                print(2*x)
                print("Goldbach Conejcture disproved")
            else:
                end = time.time()
                print(end - start)
                print(goldbach_set)
                exit()

number = 10000
primefinder(number)
goldbach_conjecture()
goldbach_set = set(goldbach_set)
goldbach_set = list(goldbach_set)
goldbach_conjecture_checker()
end = time.time()
print(end - start)
