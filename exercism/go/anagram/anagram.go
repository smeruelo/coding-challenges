// https://exercism.io/my/solutions/e38d33e70e494d4d9a08697237e251b4

package anagram

import "strings"

func counter(word string) map[rune]int {
	c := map[rune]int{}
	for _, letter := range word {
		c[letter]++
	}
	return c
}

func sameLetters(c1, c2 map[rune]int) bool {
	if len(c1) != len(c2) {
		return false
	}
	for k1, v1 := range c1 {
		if v1 != c2[k1] {
			return false
		}
	}
	return true
}

// Detect filters which words in a list are anagrams of a given word
func Detect(word string, candidates []string) []string {
	anagrams := []string{}
	wordLower := strings.ToLower(word)
	c := counter(wordLower)
	for _, w := range candidates {
		wLower := strings.ToLower(w)
		if wLower != wordLower && sameLetters(c, counter(wLower)) {
			anagrams = append(anagrams, w)
		}
	}
	return anagrams
}
