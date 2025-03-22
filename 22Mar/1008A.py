k = int(input())

def char2int(c):
    if ord('a') <= ord(c) and ord(c) <= ord('z'):
        return ord(c) - ord('a') + 1
    else: 
        return ord(c) - ord('A') + 27

def int2char(c):
    if 1 <= c and c <= 26:
        return chr(ord('a') + c - 1)
    else:
        return chr(ord('A') + c - 27)
    
def countString(S, start, end):
    cnt = [0 for i in range(26 * 2 + 1)]
    for i in range(start, end):
        cnt[char2int(S[i])] +=1
    
    return cnt

ans = 0
    
for i in range(k):
    S = input()
    n = len(S)
    cnt1 = countString(S, 0, n // 2)
    cnt2 = countString(S, n // 2, n)
    for i in range(53):
        if cnt1[i] and cnt2[i]:
            print(int2char(i))
            ans = ans + i

print(ans)