// https://exercism.io/my/solutions/e09fd5018b2b4c0cbb59c442ba84de07

package twelve

import (
	"fmt"
	"strings"
)

var (
	presents = []string{
		"",
		"a Partridge in a Pear Tree.",
		"two Turtle Doves, ",
		"three French Hens, ",
		"four Calling Birds, ",
		"five Gold Rings, ",
		"six Geese-a-Laying, ",
		"seven Swans-a-Swimming, ",
		"eight Maids-a-Milking, ",
		"nine Ladies Dancing, ",
		"ten Lords-a-Leaping, ",
		"eleven Pipers Piping, ",
		"twelve Drummers Drumming, ",
	}
	ordinals = []string{
		"",
		"first",
		"second",
		"third",
		"fourth",
		"fifth",
		"sixth",
		"seventh",
		"eighth",
		"ninth",
		"tenth",
		"eleventh",
		"twelfth",
	}
)

// intro returns the begin part of the n-th verse of the Christmas song.
func intro(nth int) string {
	return fmt.Sprintf("On the %s day of Christmas my true love gave to me: ", ordinals[nth])
}

// Verse returns the n-th verse of the Christmas song.
func Verse(n int) string {
	var b strings.Builder
	b.WriteString(intro(n))
	for i := n; i > 1; i-- {
		b.WriteString(presents[i])
	}
	if n > 1 {
		b.WriteString("and ")
	}
	b.WriteString(presents[1])
	return b.String()
}

// Song returns the (whole) Christmas song.
func Song() string {
	var b strings.Builder
	for i := 1; i < len(presents)-1; i++ {
		b.WriteString(Verse(i))
		b.WriteString("\n")
	}
	b.WriteString(Verse(len(presents) - 1)) // No newline after last verse
	return b.String()
}
