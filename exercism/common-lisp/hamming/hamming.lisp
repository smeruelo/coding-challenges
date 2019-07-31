;;; https://exercism.io/my/solutions/5bd5e8b9924142c7a8b6fdf19b3bbcbe

(defpackage #:hamming
  (:use #:cl)
  (:export #:distance))

(in-package #:hamming)

(defun distance (dna1 dna2)
  "Number of positional differences in two equal length dna strands."
  (when (= (length dna1) (length dna2))
    (let ((c 0))
      (map nil (lambda (c1 c2) (when (char/= c1 c2) (incf c))) dna1 dna2)
      c)))
