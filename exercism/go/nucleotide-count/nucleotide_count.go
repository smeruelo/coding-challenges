// https://exercism.io/my/solutions/3f0c1907c36441068e686caf25c32069

package dna

import (
	"errors"
)

type nucleotide rune

const (
	a nucleotide = 'A'
	c nucleotide = 'C'
	g nucleotide = 'G'
	t nucleotide = 'T'
)

// Histogram is a mapping from nucleotide to its count in given DNA.
type Histogram map[nucleotide]int

// DNA is a list of nucleotides.
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
// Returns an error if d contains an invalid nucleotide.
func (strand DNA) Counts() (Histogram, error) {
	hist := Histogram{a: 0, c: 0, g: 0, t: 0}
	for _, c := range strand {
		n := nucleotide(c)
		_, ok := hist[n]
		if ok {
			hist[n]++
		} else {
			return hist, errors.New("invalid DNA strand")
		}
	}
	return hist, nil
}
