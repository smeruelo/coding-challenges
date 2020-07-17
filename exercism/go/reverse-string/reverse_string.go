// https://exercism.io/my/solutions/856cf8f8a5984c8fabaef8542873f2ab

package reverse

import "strings"

// Reverse returns a reversed copy of the given string
func Reverse(s string) string {
	runes := []rune(s)
	var b strings.Builder
	for i := len(runes) - 1; i >= 0; i-- {
		_, _ = b.WriteRune(runes[i])
	}
	return b.String()
}
