import re
S = raw_input()
pattern = re.search(r'([0-9a-zA-Z])\1', S)
if pattern:
    print pattern.group(1)
else:
    print -1