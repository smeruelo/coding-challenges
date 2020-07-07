package proverb

import "fmt"

// Proverb should have a comment documenting it.
func Proverb(rhyme []string) []string {
	length := len(rhyme)
	output := make([]string, length)
	if length > 0 {
		for i := 1; i < length; i++ {
			output[i-1] = fmt.Sprintf("For want of a %s the %s was lost.", rhyme[i-1], rhyme[i])
		}
		output[length-1] = fmt.Sprintf("And all for the want of a %s.", rhyme[0])
	}
	return output
}
