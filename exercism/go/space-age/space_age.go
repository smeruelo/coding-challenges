// https://exercism.io/my/solutions/f38b588757c7462dae0c5197b2d568fe

// Package space provides awesome tools to compare human vs alien stuff.
package space

// Planet type represents planets.
type Planet string

// Age returns the age, in Earth years, of someone (given their planet and their age in seconds).
func Age(seconds float64, planet Planet) float64 {
	const earthYearSeconds = 31557600.0
	earthYears := map[Planet]float64{
		"Mercury": 0.2408467,
		"Venus":   0.61519726,
		"Earth":   1.0,
		"Mars":    1.8808158,
		"Jupiter": 11.862615,
		"Saturn":  29.447498,
		"Uranus":  84.016846,
		"Neptune": 164.79132,
	}

	return seconds / (earthYears[planet] * earthYearSeconds)
}
