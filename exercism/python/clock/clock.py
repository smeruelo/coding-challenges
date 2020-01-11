# https://exercism.io/my/solutions/a4b8a075fef3447893a9c6310065408e


class Clock:
    def __init__(self, hour, minute):
        self._min = minute % 60
        self._hour = (hour + (minute // 60)) % 24

    def __repr__(self):
        mm = str(self._min).zfill(2)
        hh = str(self._hour).zfill(2)
        return f'{hh}:{mm}'

    def __eq__(self, other):
        return self._hour == other._hour and self._min == other._min

    def __add__(self, minutes):
        new_min = (self._min + minutes) % 60
        new_hour = (self._hour + (self._min + minutes) // 60) % 24
        return Clock(new_hour, new_min)

    def __sub__(self, minutes):
        new_min = (self._min - minutes) % 60
        new_hour = (self._hour + (self._min - minutes) // 60) % 24
        return Clock(new_hour, new_min)
