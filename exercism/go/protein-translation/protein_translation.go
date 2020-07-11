// https://exercism.io/my/solutions/43ed32284a96471587ea1563edbe92a8

package protein

import "errors"

const stop = "STOP"

var codons = map[string]string{
	"AUG": "Methionine",
	"UUU": "Phenylalanine", "UUC": "Phenylalanine",
	"UUA": "Leucine", "UUG": "Leucine",
	"UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
	"UAU": "Tyrosine", "UAC": "Tyrosine",
	"UGU": "Cysteine", "UGC": "Cysteine",
	"UGG": "Tryptophan",
	"UAA": stop, "UAG": stop, "UGA": stop,
}

// min receives two integers and returns the smaller one
func min(x int, y int) int {
	if x <= y {
		return x
	}
	return y
}

// Different error codes to return
var (
	ErrInvalidBase = errors.New("invalid codon")
	ErrStop        = errors.New("end")
)

// FromCodon translates one 3-letter string into its matching protein
func FromCodon(c string) (string, error) {
	protein, ok := codons[c]
	if !ok {
		err := ErrInvalidBase
		return "", err
	}
	if protein == stop {
		err := ErrStop
		return "", err
	}
	return protein, nil
}

// FromRNA takes an n-codons string, and returns its translation into a series of proteins
func FromRNA(rna string) ([]string, error) {
	proteins := []string{}
	for i := 0; i < len(rna); i += 3 {
		c := rna[i:min(i+3, len(rna))]
		p, err := FromCodon(c)
		if err == ErrStop {
			break
		}
		if err == ErrInvalidBase {
			return proteins, err
		}
		if err == nil {
			proteins = append(proteins, p)
		}
	}
	return proteins, nil
}
