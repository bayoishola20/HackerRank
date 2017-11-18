import re
N = raw_input()

for i in xrange(int(N)):
    hex_code = re.findall(r"(?<= |:)((?:#)(?:[0-9A-Fa-f]{1,2}){3,4})", raw_input())
    if hex_code:
        for hex_ in hex_code:
            print hex_