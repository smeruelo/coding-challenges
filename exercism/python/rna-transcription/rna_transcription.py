# https://exercism.io/my/solutions/f5c71bd8f317474395b0b86c85c4d797

def to_rna(dna_strand):
    COMPLEMENTS = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    
    def complement(nucleotide):
        return COMPLEMENTS[nucleotide]

    return ''.join(map(complement, dna_strand))
        
