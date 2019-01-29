class SpaceAge(object):
    EARTH_YEAR_SECONDS = 31557600
    MERCURY_YEAR_SECONDS = 0.2408467 * EARTH_YEAR_SECONDS
    VENUS_YEAR_SECONDS = 0.61519726 * EARTH_YEAR_SECONDS
    MARS_YEAR_SECONDS = 1.8808158 * EARTH_YEAR_SECONDS
    JUPITER_YEAR_SECONDS = 11.862615 * EARTH_YEAR_SECONDS
    SATURN_YEAR_SECONDS = 29.447498 * EARTH_YEAR_SECONDS
    URANUS_YEAR_SECONDS = 84.016846 * EARTH_YEAR_SECONDS
    NEPTUNE_YEAR_SECONDS = 164.79132 * EARTH_YEAR_SECONDS

    def __init__(self, seconds):
        self._seconds = seconds

    @property
    def seconds(self):
        return self._seconds

    def on_earth(self):
        return round(self._seconds / self.EARTH_YEAR_SECONDS, 2)

    def on_mercury(self):
        return round(self._seconds / self.MERCURY_YEAR_SECONDS, 2)

    def on_venus(self):
        return round(self._seconds / self.VENUS_YEAR_SECONDS, 2)

    def on_mars(self):
        return round(self._seconds / self.MARS_YEAR_SECONDS, 2)

    def on_jupiter(self):
        return round(self._seconds / self.JUPITER_YEAR_SECONDS, 2)

    def on_saturn(self):
        return round(self._seconds / self.SATURN_YEAR_SECONDS, 2)

    def on_uranus(self):
        return round(self._seconds / self.URANUS_YEAR_SECONDS, 2)

    def on_neptune(self):
        return round(self._seconds / self.NEPTUNE_YEAR_SECONDS, 2)
