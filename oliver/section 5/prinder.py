import math
test = 0
prime = int(input("Find primes up to: "))
for i in range(1,prime):
    for k in range(1,i):
        test = i % k
        if test == 1:
            print(i)
