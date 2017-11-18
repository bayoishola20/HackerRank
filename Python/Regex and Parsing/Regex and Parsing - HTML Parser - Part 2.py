from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != "\n":
            print ">>> Data", "\n", data
    def handle_comment(self, data):
        if len(data.split("\n")) == 1:
            print ">>> Single-line Comment", "\n", data
        else:
            print ">>> Multi-line Comment", "\n", data

#===============================#
    # Code in stub #
#===============================#
html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()