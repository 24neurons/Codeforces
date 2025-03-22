n = int(input())
for i in range(1, n + 1, 1):
    S = input()
    if len(S) > 10:
        print(S[0], len(S) - 2, S[-1], sep = "")
    else:
        print(S)