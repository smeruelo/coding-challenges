#!/usr/bin/python2
# https://www.hackerrank.com/challenges/find-angle/problem

#    A
#    |\
#    | \
#    |  \
#    |   \M
#    |   /\
#    |  /| \
#    | / |  \
#    |/  |   \
#    B   X    C
#
#    XC = BX = BC / 2
#    MX = sin(theta)

from math import sqrt, asin, pi

if __name__ == '__main__':
    ab = float(raw_input())
    bc = float(raw_input())
    mc = sqrt(ab ** 2 + bc ** 2) / 2
    xc = bc / 2
    mx = sqrt(mc ** 2 - xc ** 2)
    # Divide MX / MC so we have a valid value among [-1, 1]
    theta_rad = asin(mx / mc)
    theta_deg = (theta_rad * 180) / pi
    print str(int(round(theta_deg))) + u'\u00B0'
