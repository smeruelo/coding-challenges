#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
from email.utils import parseaddr, formataddr

def valid(address):
    regex = re.compile(r'[a-zA-Z][\w\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', re.IGNORECASE)
    return bool(regex.match(address))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        name, mail = parseaddr(raw_input())
        if valid(mail):
            print formataddr((name, mail))
