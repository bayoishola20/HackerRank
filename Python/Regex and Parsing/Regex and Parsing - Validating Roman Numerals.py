import re
N = raw_input()
pattern = re.match(r"^M{,3}(CM|CD|D?C{,3})(XC|XL|L?X{,3})(IX|IV|V?I{,3})$", N)
if pattern:
    print "True"
else:
    print "False"