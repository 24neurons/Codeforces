S = input()
first_letter = S[0]
later = S[1:]
def capitalize(S):
    print(S[0].upper() , end = '')
    print(S[1:].lower())
if ord('a') <= ord(first_letter) and ord(first_letter) <= ord('z'):
    if later == later.upper():
        capitalize(S)
    else:
        print(S)
else:
    if S == S.upper():
        print(S.lower())
    else:
        print(S)