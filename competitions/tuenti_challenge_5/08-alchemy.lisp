#!/usr/bin/sbcl --script

(load "quicklisp/setup.lisp")
(require :split-sequence)
(use-package :split-sequence)

(defvar *num-basic* 10000)
(defvar *num-compound* 90000)
(defvar *datafile* "book.data")


(defun max-gold (available combinations)
  (let ((gold 0))
    (labels ((iter (unused used)
	       (if unused
		   (progn
		     (dolist (combo (possible-combos (car unused) combinations))
		       (multiple-value-bind (combinable-p new-used) (have-ingredients combo used)
			 (if combinable-p
			     (iter (cons (rcic combo)
					 (cdr unused))
				   new-used))))
		     (iter (cdr unused) (cons (car unused) used)))
		   (setf gold (max (value used combinations) gold)))))
      (iter available nil)
      gold)))

(defun have-ingredients (combo used)
  (labels ((iter (combo used)
	     (if combo
		 (if (member (car combo) used :test #'equal)
		     (iter (cdr combo) (remove (car combo) used :test #'equal :count 1))
		     (values nil nil))
		 (values t used))))
    (iter (inic combo) used)))

(defun value (elements combinations)
  (reduce #'+ (loop for e in elements collect
		  (first (gethash e combinations)))))

(defun possible-combos (element combinations)
  (cdr (gethash element combinations)))

(defun inic (combo)
  "ingredients needed in combo"
  (cddr combo))
(defun rcic (combo)
  "resulted compound in combo"
  (first combo))
(defun rgic (combo)
  "resulted gold in combo"
  (second combo))

(defun read-data (file combinations)
  (dotimes (_ *num-basic*)
    (let* ((line (split-sequence #\Space (read-line file) :remove-empty-subseqs t))
	   (basic (car line))
	   (gold (parse-integer (cadr line))))
      (setf (gethash basic combinations) (list gold))))
  (dotimes (_ *num-compound*)
    (let* ((line (split-sequence #\Space (read-line file) :remove-empty-subseqs t))
	   (compound (car line))
	   (gold (parse-integer (cadr line)))
	   (ingredients (cddr line)))
      (setf (gethash compound combinations) (list gold))
      (dolist (i ingredients)
	(pushnew (cons compound (cons gold (remove i ingredients))) (cdr (gethash i combinations)) :test #'equal)))))

(defun process-in ()
  (with-open-file (file *datafile*)
    (let* ((combinations (make-hash-table :test #'equal)))
      (read-data file combinations)
      (dotimes (_ (read))
	(let ((line (split-sequence #\Space (read-line *standard-input*) :remove-empty-subseqs t)))
	  (format t "~a~%" (max-gold line combinations)))))))

(process-in)