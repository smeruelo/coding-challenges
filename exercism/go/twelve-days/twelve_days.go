// https://exercism.io/my/solutions/e09fd5018b2b4c0cbb59c442ba84de07

package twelve

import (
	"fmt"
	"strings"
)

var (
	presents = []string{
		"twelve Drummers Drumming, ",
		"eleven Pipers Piping, ",
		"ten Lords-a-Leaping, ",
		"nine Ladies Dancing, ",
		"eight Maids-a-Milking, ",
		"seven Swans-a-Swimming, ",
		"six Geese-a-Laying, ",
		"five Gold Rings, ",
		"four Calling Birds, ",
		"three French Hens, ",
		"two Turtle Doves, and ",
		"a Partridge in a Pear Tree.",
	}
	ordinals = []string{
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
	intro  = "On the %s day of Christmas my true love gave to me: "
	verses = make([]string, 12)
	song   string
)

// Generates every verse and the whole song only once
func init() {
	for i := 1; i <= 12; i++ {
		verses[i-1] = fmt.Sprintf(intro, ordinals[i-1]) + strings.Join(presents[12-i:], "")
	}
	song = strings.Join(verses, "\n")
}

// Verse returns the n-th verse of the Christmas song.
func Verse(n int) string {
	return verses[n-1]
}

// Song returns the (whole) Christmas song.
func Song() string {
	return song
}
