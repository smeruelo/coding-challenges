// https://exercism.io/my/solutions/b8992f532aad429381b97e5ff6c333f3

package triangle

import (
	"math"
)

// Kind represents the type of a triangle
type Kind int

// Possibilities for Kind type
const (
	NaT Kind = iota // not a triangle
	Equ Kind = iota // equilateral
	Iso Kind = iota // isosceles
	Sca Kind = iota // scalene
)

// KindFromSides determines the kind of a triangle according to its sides' lengths
func KindFromSides(a, b, c float64) Kind {
	if math.IsNaN(a+b+c) || math.IsInf(a+b+c, 1) || math.IsInf(a+b+c, -1) {
		return NaT
	}
	if a <= 0 || b <= 0 || c <= 0 {
		return NaT
	}
	if a > b+c || b > a+c || c > a+b {
		return NaT
	}
	if a == b && a == c {
		return Equ
	}
	if a == b || a == c || b == c {
		return Iso
	}
	return Sca
}
