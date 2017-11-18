from HTMLParser import HTMLParser

N = int(raw_input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
    def handle_endtag(self, tag):
        pass
    
    def handle_startendtag(self, tag, attrs):
        print tag
        for attr in attrs:
            print "->", attr[0], ">", attr[1]
        
parser = MyHTMLParser()


for i in xrange(N):
    parser.feed(raw_input())