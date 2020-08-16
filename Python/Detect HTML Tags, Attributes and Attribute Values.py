from html.parser import HTMLParser
class myParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for x in attrs:
            print('-> {} > {}'.format(x[0],x[1]))
mp=myParser()
for _ in range(int(input())):
    mp.feed(input())
