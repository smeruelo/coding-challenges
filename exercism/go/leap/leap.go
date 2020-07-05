// https://exercism.io/my/solutions/86f03da6eee94991890115b9e7e0e7b7

// Package leap provides tools to handle leap years.
package leap

// multiple receives two nums and determines whether the first one is a multiple of the other.
func multiple(num1 int, num2 int) bool {
	return num1%num2 == 0
}

// IsLeapYear returns whether the given year is a leap one or not.
func IsLeapYear(year int) bool {
	return multiple(year, 4) && !multiple(year, 100) || multiple(year, 400)
}
