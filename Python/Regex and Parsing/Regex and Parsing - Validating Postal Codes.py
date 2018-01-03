import re
P = raw_input()
print bool(re.search(r'^[1-9][0-9]{5}$', P) and len(re.findall(r'(.)(?=.\1)',P))<2)