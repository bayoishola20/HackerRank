from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
        
parser = MyHTMLParser()

N = int(raw_input())

for i in xrange(N):
    parser.feed(raw_input())