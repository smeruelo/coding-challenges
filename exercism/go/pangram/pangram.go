// https://exercism.io/my/solutions/8de4b7fc7e534cefa397ce9fa340b513

package pangram

import "unicode"

// IsPangram determines if every letter in an alphabet appears or not in a sentence.
func IsPangram(sentence string) bool {
	const alphabet = "abcdefghijklmnopqrstuvwxyz"

	present := make(map[rune]bool, len(alphabet))
	for _, letter := range alphabet {
		present[letter] = false
	}

	for _, letter := range sentence {
		present[unicode.ToLower(letter)] = true
	}

	for _, v := range present {
		if !v {
			return false
		}
	}
	return true
}
