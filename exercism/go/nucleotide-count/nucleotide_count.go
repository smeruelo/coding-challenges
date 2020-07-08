package dna

import (
	"errors"
)

type nucleotide rune

const (
	A nucleotide = 'A'
	C nucleotide = 'C'
	G nucleotide = 'G'
	T nucleotide = 'T'
)

// Histogram is a mapping from nucleotide to its count in given DNA.
type Histogram map[nucleotide]int

// DNA is a list of nucleotides.
type DNA string

// Counts generates a histogram of valid nucleotides in the given DNA.
// Returns an error if d contains an invalid nucleotide.
func (strand DNA) Counts() (Histogram, error) {
	var hist Histogram = Histogram{A: 0, C: 0, G: 0, T: 0}
	var err error

	for _, c := range strand {
		n := nucleotide(c)
		_, ok := hist[n]
		if ok {
			hist[n] += 1
		} else {
			err = errors.New("invalid DNA strand.")
		}
	}
	return hist, err
}
