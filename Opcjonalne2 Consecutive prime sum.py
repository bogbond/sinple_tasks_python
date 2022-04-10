import math
from functools import reduce

def prime(n):
    return  sorted(list(reduce(lambda r, x: r - set(range(int(math.pow(x, 2)), n, x)) if x in r else r, range(2, int(math.sqrt(n)) + 1), set(range(2,n)))))

def primeMax(n):
    primes = prime(n)
    end = len(primes)
    terms = 0
    maxPrime = 0
    
    for i in range(len(primes)):
        for j in range(i+terms, end):
            summa = sum(primes[i:j])
            if summa < n:
                if summa in primes:
                    terms = j-i
                    maxPrime = summa
            else:
                end = j+1
                break
    
    return "The prime " + str(maxPrime) +" can be written as the sum of " + str(terms)+ " consecutive primes"
    


n = 1000000
print(primeMax(n))