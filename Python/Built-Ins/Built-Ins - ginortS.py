def check(S):
    if S.islower():
        return ord(S) - 123
    if S.isupper():
        return ord(S) - 65
    if S.isdigit():
        if (int(S) % 2) == 0:
            return ord(S) + 10
        else:
            return ord(S)
S = raw_input().strip()
print (reduce(lambda x,y: x+y, sorted(S, key=lambda x: check(x))))