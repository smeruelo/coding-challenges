// https://exercism.io/my/solutions/753d4bb58be34c148925b28656f5e3f9

package accumulate

type stringConverter func(s string) string

// Accumulate applies the given function to each of the strings in an array.
func Accumulate(collection []string, f stringConverter) []string {
	result := make([]string, len(collection))
	for i, s := range collection {
		result[i] = f(s)
	}
	return result
}
