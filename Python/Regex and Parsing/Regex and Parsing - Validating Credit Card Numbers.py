import re
T = int(raw_input())
for i in xrange(T):
    N = raw_input()
    validCard = (re.findall(r'^([456]\d{15})$',N) or re.findall(r'^([456]\d{3})-(\d{4})-(\d{4})-(\d{4})$',N))
    if  validCard and not re.search(r'(\d)\1\1\1',('').join(validCard[0])):
        print 'Valid'
    else:
        print 'Invalid'