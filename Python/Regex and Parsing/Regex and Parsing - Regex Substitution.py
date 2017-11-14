import re
N = int(raw_input())
for i in range(N):
    print (re.sub(r"(?<= )\|\|(?= )", "or", re.sub(r"(?<= )&&(?= )", "and", raw_input())))