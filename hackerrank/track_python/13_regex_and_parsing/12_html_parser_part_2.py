#!/usr/bin/python2
# https://www.hackerrank.com/challenges/html-parser-part-2/problem

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            print '>>> Data\n{}'.format(data)

    def handle_comment(self, data):
        comment = data.split('\n')
        print '>>> Multi-line Comment' if len(comment) > 1 else '>>> Single-line Comment'
        print data


if __name__ == '__main__':
    html = '\n'.join([raw_input() for _ in range(int(raw_input()))])
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
