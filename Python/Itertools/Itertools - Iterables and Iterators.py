N = int(raw_input())
letters = raw_input().split()
K = int(raw_input())

total = 0
count = 0

for letter in combinations(letters, K):
    total += 1
    count += 'a' in letter
    ans = float(count)/total
print ans