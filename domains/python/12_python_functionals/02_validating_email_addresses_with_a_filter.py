#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

from string import letters, digits

def valid_email(s):
    """Returns True if s is a valid email, else return False"""

    if s.count('@') == 1 and s.count('.') == 1 and s.find('@') < s.find('.'):
        user = s[:s.find('@')]
        website = s[s.find('@')+1:s.find('.')]
        extension = s[s.find('.')+1:]
        return len(user) > 0 and len(website) > 0 and len(extension) > 0 and \
            all(map(lambda c: c in letters + digits + '-_', user)) and \
            all(map(lambda c: c in letters + digits, website)) and \
            len(extension) <= 3
    else:
        return False

if __name__ == '__main__':
    emails = [raw_input() for _ in range(int(raw_input()))]
    print sorted(filter(valid_email, emails))
