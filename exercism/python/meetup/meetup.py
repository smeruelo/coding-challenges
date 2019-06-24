# https://exercism.io/my/solutions/b41b63c3c8d4426193afca8bbb5ec369

import calendar


def meetup(year, month, week, day_of_week):
    TEENS = range(13, 20)
    WEEKDAYS = dict(zip(list(calendar.day_name), range(7)))

    wd = WEEKDAYS[day_of_week]
    cal = calendar.Calendar().itermonthdates(year, month)
    days = [day for day in cal if day.weekday() == wd and day.month == month]

    if week == 'teenth':
        return [day for day in days if day.day in TEENS][0]
    if week == 'last':
        return days[-1]
    try:
        return days[int(week[0])-1]
    except Exception:
        raise MeetupDayException('Impossible date')


class MeetupDayException(Exception):
    pass
