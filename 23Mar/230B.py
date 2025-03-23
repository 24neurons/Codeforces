n = int(input())
from math import sqrt

limit = 10**6

isPrime = [1 for i in range(limit + 1)] 
for i in range(2, int(limit**0.5 + 1)):
    if isPrime[i]:
        for j in range(i * i , limit + 1, i):
            isPrime[j] = False


List = list(map(int, input().split()))
for k in List:
    if k == 1:
        print("NO")
    elif sqrt(k) == int(sqrt(k)):
        if isPrime[int(sqrt(k))]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")