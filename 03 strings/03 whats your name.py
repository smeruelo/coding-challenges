#!/usr/bin/python2
# https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(name, lastname):
    print "Hello {} {}! You just delved into python.".format(name, lastname)

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
