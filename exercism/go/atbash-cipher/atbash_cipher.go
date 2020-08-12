// https://exercism.io/my/solutions/abde508f2a124bbf927c9f55836d9773
package atbash

import (
	"regexp"
	"strings"
	"unicode"
)

var abcPlain = []rune("abcdefghijklmnopqrstuvwxyz")
var abcCipher = []rune("zyxwvutsrqponmlkjihgfedcba")
var transTable map[rune]rune

func init() {
	transTable = make(map[rune]rune, len(abcPlain))
	for i, plain := range abcPlain {
		transTable[plain] = abcCipher[i]
	}
}

func encodeLetter(r rune) rune {
	if unicode.IsDigit(r) {
		return r
	}
	enc, ok := transTable[unicode.ToLower(r)]
	if !ok {
		return -1
	}
	return enc
}

func split5(s string) string {
	re, _ := regexp.Compile(".{5}")
	splitted := re.ReplaceAllString(s, "$0 ")
	return strings.Trim(splitted, " ")
}

// Atbash encodes a string using the Atbash cipher
func Atbash(s string) string {
	return split5(strings.Map(encodeLetter, s))
}
