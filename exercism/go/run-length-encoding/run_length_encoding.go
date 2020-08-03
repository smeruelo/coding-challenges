// https://exercism.io/my/solutions/e805eb4202744e1390172f0ba7bc336b

package encode

import (
	"strconv"
	"strings"
	"unicode"
)

// RunLengthEncode takes a string and returns its RLE encoding
func RunLengthEncode(plain string) string {
	var b strings.Builder
	writeEncoded := func(r rune, count int) {
		if count > 0 { // count == 0 means rune is not inizialized (it would write a '\x00' byte)
			if count > 1 {
				b.WriteString(strconv.Itoa(count))
			}
			b.WriteRune(r)
		}
	}

	var prev rune
	count := 0
	for _, current := range plain {
		if current == prev {
			count++
		} else {
			writeEncoded(prev, count)
			count = 1
		}
		prev = current
	}
	writeEncoded(prev, count)
	return b.String()
}

// RunLengthDecode takes an RLE encoded string and decodes it
func RunLengthDecode(encoded string) string {
	var b strings.Builder
	n := 0
	for _, r := range encoded {
		if unicode.IsDigit(r) {
			n = n*10 + int(r-'0')
		} else {
			if n == 0 {
				n = 1
			}
			b.WriteString(strings.Repeat(string(r), n))
			n = 0
		}
	}
	return b.String()
}
