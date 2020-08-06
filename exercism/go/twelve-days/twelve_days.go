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
	intro = "On the %s day of Christmas my true love gave to me: "
)

// Verse returns the n-th verse of the Christmas song.
func Verse(n int) string {
	return fmt.Sprintf(intro, ordinals[n]) + strings.Join(presents[12-n:], "")
}

// Song returns the (whole) Christmas song.
func Song() string {
	verses := make([]string, 12)
	for i := 1; i <= 12; i++ {
		verses[i-1] = Verse(i)
	}
	return strings.Join(verses, "\n")
}
