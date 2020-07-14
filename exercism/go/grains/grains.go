// https://exercism.io/my/solutions/230a5f79cd654c8bae0d806d9fae573b

package grains

import "errors"

// Square returns the number of grains on the given square
func Square(n int) (uint64, error) {
	if n <= 0 || n > 64 {
		return 0, errors.New("invalid square number")
	}
	return 1 << (n - 1), nil
}

// Total returns the total number of grains on the whole chessboard
func Total() uint64 {
	// There's no need to loop over Square(), we already know that sum's result:
	// 2^1 + 2^2 + .. + 2^63 = 2^64 - 1  (a.k.a. math.MaxUint64)

	// Surprisingly, go handles this expresion without making us use bignums
	// so let's make it explicit instead of returning math.MaxUint64
	return 1<<64 - 1
}
