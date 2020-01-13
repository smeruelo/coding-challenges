# https://exercism.io/my/solutions/a4b8a075fef3447893a9c6310065408e


class Clock:
    def __init__(self, hour, minute):
        self._min = minute % 60
        self._hour = (hour + (minute // 60)) % 24
        # self._hour, self._min = divmod((hour * 60 + minute) % (24 * 60), 60)

    def __repr__(self):
        return f'{self._hour:02d}:{self._min:02d}'

    def __eq__(self, other):
        return self._hour == other._hour and self._min == other._min

    def __add__(self, minutes):
        return Clock(self._hour, self._min + minutes)

    def __sub__(self, minutes):
        return Clock(self._hour, self._min - minutes)
