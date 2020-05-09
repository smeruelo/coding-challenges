#!/usr/bin/sbcl --script

(load "quicklisp/setup.lisp")
(require :split-sequence)
(require :alexandria)
(use-package :split-sequence)
(use-package :alexandria)

;; why calculate them if they're well known
(defvar *primes* '(2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97))
(defvar *days* 30000)

(defun exhaust-prime (product prime count)
  (if (zerop (mod product prime))
      (exhaust-prime (/ product prime) prime (1+ count))
      (values product count)))

(defun iter-primes (product remaining-primes new-primes)
  (if remaining-primes
      (multiple-value-bind (prod count) (exhaust-prime product (caar remaining-primes) (cdar remaining-primes))
	(iter-primes prod
		     (cdr remaining-primes)
		     (cons (cons (caar remaining-primes) count) new-primes)))
      (reverse new-primes)))

(defun primes-day (product)
  (iter-primes product (mapcar (rcurry #'cons 0) *primes*) nil))

(defun primes-period (begin end combos)
  (labels ((aux (i accum)
	     (if (< i end)
		 (aux (1+ i) (sum-combos (aref combos i) accum))
		 accum)))
    (aux begin (mapcar (rcurry #'cons 0) *primes*))))

(defun sum-combos (combo1 combo2)
  (mapcar #'(lambda (x y) (cons (car x) (+ (cdr x) (cdr y)))) combo1 combo2))

(defun calc-combinations (combos products)
  (labels ((aux (prod i)
	     (when prod
		 (setf (aref combos i) (primes-day (car prod)))
		 (aux (cdr prod) (1+ i)))))
    (aux products 0)))

(defun process-out (chosen-primes)
  (let* ((sorted (sort chosen-primes #'> :key #'cdr))
	 (repetitions (cdar sorted)))
    (labels ((aux (primes output)
	       (if (and primes (eq (cdar primes) repetitions))
		   (aux (cdr primes) (cons (caar primes) output))
		   (reverse output))))
      (aux (cdr sorted) (cons (caar sorted) (list repetitions))))))

(defun read-file ()
  (with-open-file (numbers "numbers.txt")
    (labels ((aux (lst)
	       (let ((n (read numbers nil nil)))
		 (if n
		     (aux (cons n lst))
		     (reverse lst)))))
      (aux nil))))

(defun process-in ()
  (let* ((products (read-file))
	 (combinations (make-array *days*)))
    (calc-combinations combinations products)
    (dotimes (i (read *standard-input*))
      (let ((line (mapcar #'parse-integer
			  (split-sequence #\Space (read-line *standard-input*) :remove-empty-subseqs t))))
	(format t "~{~a~^ ~}~%" (process-out (primes-period (car line) (cadr line) combinations)))))))

(process-in)
