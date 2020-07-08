// https://exercism.io/my/solutions/753d4bb58be34c148925b28656f5e3f9

package accumulate

type stringConverter func(string) string

// Accumulate applies the given function to each of the strings in an array.
func Accumulate(in []string, f stringConverter) []string {
	out := make([]string, len(in))
	for i, s := range in {
		out[i] = f(s)
	}
	return out
}
