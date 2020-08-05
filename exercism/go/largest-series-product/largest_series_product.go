// https://exercism.io/my/solutions/37c4f904c17442ebb83c3f85e1c1879b

package lsproduct

import (
	"fmt"
)

// LargestSeriesProduct returns the largest product for a contiguous substring of length n.
func LargestSeriesProduct(digits string, span int) (int, error) {
	runes := []rune(digits)
	if span < 0 || span > len(runes) {
		return 0, fmt.Errorf("invalid span %q (it must be >0 and <= input's length)", span)
	}

	maxProduct := 0
	for i := 0; i <= len(digits)-span; i++ {
		product := 1
		for j := 0; j < span; j++ {
			d := int(runes[i+j] - '0')
			if d < 0 || d > 9 {
				return 0, fmt.Errorf("invalid input %q (it must contain only digits)", digits)
			}
			product *= d
		}
		if product > maxProduct {
			maxProduct = product
		}
	}
	return maxProduct, nil
}
