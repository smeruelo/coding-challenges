// https://exercism.io/my/solutions/856cf8f8a5984c8fabaef8542873f2ab

package reverse

// Reverse returns a reversed copy of the given string
func Reverse(s string) string {
	rev := ""
	for _, char := range s {
		rev = string(char) + rev
	}
	return rev
}
