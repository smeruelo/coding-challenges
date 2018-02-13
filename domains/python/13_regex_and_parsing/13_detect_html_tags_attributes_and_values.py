#!/usr/bin/python2
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for attr, value in attrs:
            print '-> {} > {}'.format(attr, value)
    def handle_startendtag(self, tag, attrs):
        print tag
        for attr, value in attrs:
            print '-> {} > {}'.format(attr, value)


if __name__ == '__main__':
    html = '\n'.join([raw_input() for _ in range(int(raw_input()))])
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
