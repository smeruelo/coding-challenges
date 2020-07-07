// https://exercism.io/my/solutions/6fe389266be0414ab8a2416ef78f94de

package proverb

import "fmt"

const (
	regVerse  = "For want of a %s the %s was lost."
	lastVerse = "And all for the want of a %s."
)

// Proverb generates a stupid poem from a list of words
func Proverb(rhyme []string) []string {
	length := len(rhyme)
	poem := make([]string, length)
	for i := 1; i < length; i++ {
		poem[i-1] = fmt.Sprintf(regVerse, rhyme[i-1], rhyme[i])
	}
	if length > 0 {
		poem[length-1] = fmt.Sprintf(lastVerse, rhyme[0])
	}
	return poem
}
