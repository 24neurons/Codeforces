for i in range(5):
    G = list(map(int, input().split()))
    for j in range(5):
        if G[j] == 1:
            ans = abs(3 - (i + 1)) + abs(3 - (j + 1))

print(ans)