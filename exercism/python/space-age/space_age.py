class SpaceAge(object):
    EARTH_YEAR_SECONDS = 31557600
    PLANETS_YEARS = {'mercury': 0.2408467,
                     'venus': 0.61519726,
                     'earth': 1,
                     'mars': 1.8808158,
                     'jupiter': 11.862615,
                     'saturn': 29.447498,
                     'uranus': 84.016846,
                     'neptune': 164.79132}

    def __init__(self, seconds):
        self._seconds = seconds
        for planet, ratio in self.PLANETS_YEARS.items():
            setattr(self, 'on_' + planet, self.age(planet))

    @property
    def seconds(self):
        return self._seconds

    def age(self, p):
        return lambda: round(self._seconds / (self.PLANETS_YEARS[p] * self.EARTH_YEAR_SECONDS), 2)
