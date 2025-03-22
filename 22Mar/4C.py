n = int(input())
C = {}
#  hash function 


for i in range(n):
    S = input()
    if C.keys().__contains__(S):
        cnt = C[S]
        print(S, cnt, sep = '')
        C[S] += 1
    else:
        C[S] = 1
        print("OK")
    