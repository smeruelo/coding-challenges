// https://exercism.io/my/solutions/e19201440e64447b8467d42ae88bf21f

package strand

import "strings"

var complement = map[rune]rune{
	'G': 'C',
	'C': 'G',
	'T': 'A',
	'A': 'U',
}

// ToRNA transforms a DNA string into an RNA one
func ToRNA(dna string) string {
	return strings.Map(func(nucleotide rune) rune { return complement[nucleotide] }, dna)
}
