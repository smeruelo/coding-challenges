# https://exercism.io/my/solutions/b41b63c3c8d4426193afca8bbb5ec369

import calendar
import datetime


def weekday(name):
    INDEX = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    return INDEX[name]


def meetup(year, month, week, day_of_week):
    TEENS = range(13, 20)
    wd = weekday(day_of_week)

    if week == 'teenth':
        for d in TEENS:
            date = datetime.date(year, month, d)
            if date.weekday() == wd:
                return date
    else:
        cal = calendar.Calendar().monthdatescalendar(year, month)
        if week == 'last':
            w = len(cal)-1
            if cal[w][wd].month == month:
                return cal[w][wd]
            else:
                return cal[w-1][wd]
        else:
            w = int(week[0]) - 1
            try:
                if cal[0][wd].month != month:
                    w += 1
                if cal[w][wd].month != month:
                    w -= 1
                return cal[w][wd]
            except Exception:
                raise MeetupDayException('Impossible date')


class MeetupDayException(Exception):
    pass
