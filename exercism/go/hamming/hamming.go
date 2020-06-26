// https://exercism.io/my/solutions/36b1acdbd9904bee98ee2497b37d1861

// Package hamming provides cool DNA-related tools.
package hamming

import "errors"

// Distance returns the Hamming distance among two strings.
func Distance(s1, s2 string) (int, error) {
	if len(s1) != len(s2) {
		return 0, errors.New("strings have different length")
	}

	distance := 0
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			distance++
		}
	}
	return distance, nil
}
