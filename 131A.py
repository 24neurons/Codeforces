n = int(input())
C = []
for i in range(n):
    S = input()
    if C.__contains__(S):
        print(S, C.count(S))
    else:
        C.append(S)
        print(S)
    