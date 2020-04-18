# https://exercism.io/my/solutions/f5c71bd8f317474395b0b86c85c4d797

TABLE = str.maketrans('ACGT', 'UGCA')

def to_rna(dna_strand):
    return dna_strand.translate(TABLE)
