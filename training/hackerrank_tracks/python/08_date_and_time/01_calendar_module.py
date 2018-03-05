#!/usr/bin/python2
# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

if __name__ == '__main__':
    month, day, year = map(int, raw_input().split())
    print calendar.day_name[calendar.weekday(year, month, day)].upper()
