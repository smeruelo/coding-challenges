package clock

import "fmt"

const minutesInADay = 1440

// modulo returns the unsigned reminder of x/y
func modulo(x, y int) int {
	return ((x % y) + y) % y
}

// Clock represents a time in the day, using hours (h in [0, 23]) and minutes (m in [0, 59])
type Clock struct {
	h int
	m int
}

// New takes an arbitrarly big (or even negative) number of hours and minutes and returns a Clock
func New(hours, minutes int) Clock {
	minuteOfDay := modulo(hours*60+minutes, minutesInADay)
	return Clock{h: minuteOfDay / 60, m: minuteOfDay % 60}
}

// Add sums the given number of minutes to a Clock and returns a new one
func (c Clock) Add(minutes int) Clock {
	return New(c.h, c.m+minutes)
}

// Subtract deducts the given number of minutes from a Clock and returns a new one
func (c Clock) Subtract(minutes int) Clock {
	return New(c.h, c.m-minutes)
}

// String returns a string representation of a Clock, in the form hh:mm
func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.h, c.m)
}
