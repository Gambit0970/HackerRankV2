from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
        
N = int(input())
htmlText = ''.join([input() for _ in range(N)])
parser = MyHTMLParser()
parser.feed(htmlText)
