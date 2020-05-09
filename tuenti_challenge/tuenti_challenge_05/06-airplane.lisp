#!/usr/bin/sbcl --script

(load "quicklisp/setup.lisp")
(require :split-sequence)
(use-package :split-sequence)


(defun quality (y0 x0 y1 x1 k full-sheet)
  (let* ((sr (- y1 y0 k -2))
	 (sc (- x1 x0 k -2))
	 (sheet-squares (make-array (list sr sc))))
    (slice full-sheet y0 x0 y1 x1 k sheet-squares sr sc)

    (reduce #'max (loop for y-axis from (+ y0 k) below (- y1 k -1) collect
		       (reduce #'max (loop for x-axis from (+ x0 k) below (- x1 k -1) collect
					  (+ (aref sheet-squares (- y-axis y0 k) (- x-axis x0 k))
					     (aref sheet-squares (- y-axis y0 -1) (- x-axis x0 -1)))))))))

(defun slice (full-sheet y0 x0 y1 x1 k sheet-squares sr sc)
  (let* ((sheet-verticals (make-array (list sr (- x1 x0 -1)))))
    ;; vertical slices
    (loop for col from x0 below (1+ x1) do
	 (setf (aref sheet-verticals 0 (- col x0)) (reduce #'+ (loop for r from y0 below (+ y0 k) collect
								    (aref full-sheet r col))))
	 (loop for row from (1+ y0) below (- y1 k -2) do
	      (setf (aref sheet-verticals (- row y0) (- col x0)) (- (aref sheet-verticals (- row y0 1) (- col x0))
								    (aref full-sheet (1- row) col)
								    (- (aref full-sheet (1- (+ row k)) col))))))
    ;; squares
    (loop for row from 0 below sr do
	 (setf (aref sheet-squares row 0) (reduce #'+ (loop for c from 0 below k collect
							   (aref sheet-verticals row c))))
	 (loop for col from 1 below sc do
	      (setf (aref sheet-squares row col) (- (aref sheet-squares row (1- col))
						    (aref sheet-verticals row (1- col))
						    (- (aref sheet-verticals row (1- (+ col k))))))))
    sheet-squares))

(defun read-sheet ()
  (with-open-file (file "sheet.data")
    (let* ((m (read file))
	   (n (read file))
	   (sheet (make-array (list m n))))
      (dotimes (row m)
	(dotimes (col n)
	  (setf (aref sheet row col) (read file))))
      sheet)))

(defun process-in ()
  (let ((full-sheet (read-sheet)))
    (dotimes (i (read))
	(let* ((line (mapcar #'parse-integer (split-sequence #\Space (read-line *standard-input*) :remove-empty-subseqs t))))
	  (format t "Case ~a: ~a~%" (1+ i) (quality (first line) (second line) (third line) (fourth line) (fifth line) full-sheet))))))

(process-in)
