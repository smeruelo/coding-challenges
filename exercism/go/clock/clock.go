// https://exercism.io/my/solutions/d38168727e814b6ebfa1395366a34502

package clock

import "fmt"

// Clock represents a time in the day, in minutes (m in [0, 1440))
type Clock struct {
	m int
}

// New takes an arbitrarly big (or even negative) number of hours and minutes and returns a Clock
func New(hours, minutes int) Clock {
	m := (hours*60 + minutes) % (24 * 60)
	if m < 0 {
		m += 24 * 60
	}
	return Clock{m: m}
}

// Add sums the given number of minutes to a Clock and returns a new one
func (c Clock) Add(minutes int) Clock {
	return New(0, c.m+minutes)
}

// Subtract deducts the given number of minutes from a Clock and returns a new one
func (c Clock) Subtract(minutes int) Clock {
	return New(0, c.m-minutes)
}

// String returns a string representation of a Clock, in the form hh:mm
func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.m/60, c.m%60)
}
