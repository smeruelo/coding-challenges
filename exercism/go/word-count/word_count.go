// https://exercism.io/my/solutions/e5e65127ef9f4458829ce0955ddc2be4

package wordcount

import (
	"regexp"
	"strings"
)

// Frequency represents a counter dictionary
type Frequency map[string]int

// Clean removes non-alphanumerical characters from a string
func clean(s string) string {
	re, _ := regexp.Compile("[^a-zA-Z0-9'\t\n]+")
	return re.ReplaceAllLiteralString(s, " ")
}

// WordCount counts the words in a sentence
func WordCount(sentence string) Frequency {
	counter := Frequency{}
	for _, w := range strings.Fields(clean(sentence)) {
		word := strings.ToLower(strings.Trim(w, "'\""))
		counter[word]++
	}
	return counter
}
