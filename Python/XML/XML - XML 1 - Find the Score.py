import sys
import xml.etree.ElementTree as etree

#===============================#
    # Code in stub above #
#===============================#

def get_attr_number(node):
    # your code goes here
    if len(node) != 0:
        total = len(node.attrib)
        for i in node:
            total += get_attr_number(i)
        return total
    else:
        return len(node.attrib)
    
xml = str()

N = raw_input()
for i in xrange(int(N)):
    xml += raw_input().strip()

tree = etree.ElementTree(etree.fromstring(xml))

print get_attr_number(tree.getroot())

#===============================#
    # Code in stub below #
#===============================#
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print get_attr_number(root)