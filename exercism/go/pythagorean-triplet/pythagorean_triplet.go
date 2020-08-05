// https://exercism.io/my/solutions/ed41d40ae99a49b9a326a2ed8c6ba27d

package pythagorean

import "math"

// Triplet represents the length of the sides of a triangle
type Triplet [3]int

func (t Triplet) isPythagorian() bool {
	a, b, c := t[0], t[1], t[2]
	return a < b && b < c && c*c == a*a+b*b
}

func (t Triplet) sum() int {
	return t[0] + t[1] + t[2]
}

// Range calculates all the pythagorean triplets which sides are in the given range
func Range(min, max int) []Triplet {
	triplets := []Triplet{}
	for a := min; a < max; a++ {
		for b := a + 1; b < max; b++ {
			c := int(math.Sqrt(float64(a*a + b*b)))
			t := Triplet{a, b, c}
			if t.isPythagorian() {
				triplets = append(triplets, Triplet{a, b, c})
			}
		}
	}
	return triplets
}

// Sum calculates all the pythagorean triplets which sides add up p
func Sum(p int) []Triplet {
	triplets := []Triplet{}
	for _, t := range Range(1, p) {
		if t.sum() == p {
			triplets = append(triplets, t)
		}
	}
	return triplets
}
