#!/usr/bin/sbcl --script

(load "quicklisp/setup.lisp")
(require :cl-base64)
(use-package :cl-base64)


(defun little-endian (bits)
  (let ((bytes (truncate (/ (length bits) 8))))
    (labels ((iter (byte re-ordered)
	       (if (> byte 0)
		   (iter (1- byte)
			 (concatenate 'string re-ordered (subseq bits (* 8 (1- byte)) (* 8 byte))))
		   re-ordered)))
      (iter bytes (subseq bits (* 8 bytes))))))

(defun get-meal (type bits)
  (cond ((equal type "L") (parse-integer (little-endian bits) :radix 2))
	((equal type "LR") (parse-integer (reverse (little-endian bits)) :radix 2))
	((equal type "B") (parse-integer bits :radix 2))
	((equal type "BR") (parse-integer (reverse bits) :radix 2))))

(defun cut-bits (bits piece)
  (let* ((l (length piece))
	 (breakpt (if (eq (char piece (1- l)) #\R)
		      (- l 2)
		      (- l 1)))
	 (nbits (parse-integer (subseq piece 0 breakpt))))
    (values (subseq bits 0 nbits) (subseq bits nbits) (subseq piece breakpt))))

(defun process-in ()
  (let* ((bitstring (format nil "~B" (base64-string-to-integer (read-line *standard-input*))))
	 (n (read *standard-input*)))
    (labels ((iter (bits i)
	       (when (< i n)
		 (let ((piece (read-line *standard-input*)))
		   (multiple-value-bind (current-bits remaining-bits type) (cut-bits bits piece)
		     (format t "~a~%" (get-meal type current-bits))
		     (iter remaining-bits (1+ i)))))))
      (iter bitstring 0))))

(process-in)



