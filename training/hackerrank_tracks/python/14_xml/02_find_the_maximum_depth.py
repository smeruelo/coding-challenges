#!/usr/bin/python2
# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem

# Awful solution, but it's what they ask for
# Much better one in https://docs.python.org/2/library/xml.etree.elementtree.html#xmlparser-objects

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    xml = '\n'.join([raw_input() for i in range(int(raw_input()))])
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth
