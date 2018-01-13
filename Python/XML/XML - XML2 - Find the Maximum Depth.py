import xml.etree.ElementTree as etree

#===============================#
    # Code in stub above #
#===============================#

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if len(elem) != 0:
        for i in elem:
            maxdepth = max(depth(i, level + 1), maxdepth)
        return maxdepth
    else:
        return level
xml = str()

N = raw_input()
for i in xrange(int(N)):
    xml += raw_input().strip()

tree = etree.ElementTree(etree.fromstring(xml))

print depth(tree.getroot(), maxdepth)

#===============================#
    # Code in stub below #
#===============================#
if __name__ == '__main__':
    n = int(raw_input())
    xml = ""
    for i in range(n):
        xml =  xml + raw_input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth