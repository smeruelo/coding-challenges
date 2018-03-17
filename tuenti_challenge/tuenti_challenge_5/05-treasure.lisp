#!/usr/bin/sbcl --script

(load "quicklisp/setup.lisp")
(require :split-sequence)
(use-package :split-sequence)


(defstruct island name cost adj)
(defstruct ship gold origin)

(defun new-island (name cost max-turns)
    (make-island :name name
		 :cost (make-array max-turns :initial-element cost)
		 :adj nil))

(defun new-ship (gold origin)
  (make-ship :gold gold
	     :origin origin))

(defun ships-costs (graph ships)
"adds ships costs to islands, returns number of turns for the fastest ship to reach Raftel"
  (reduce #'min (loop for s from 2 below (length ships) collect
		     (let ((cost (ship-gold (svref ships s)))
			   (origin (ship-origin (svref ships s))))
		       (ship-path 1 graph origin cost (if (oddp s) #'< #'>))))))

(defun ship-path (turn graph origin cost f)
  (let* ((adj (island-adj (gethash origin graph)))
	 (next (reduce #'(lambda (x y) (if (funcall f (cadr x) (cadr y)) x y)) adj)))
    (if (equal (car next) "Raftel")
	turn
	(progn
	  (incf (aref (island-cost (gethash (car next) graph)) turn) cost)
	  (ship-path (1+ turn) graph (car next) cost f)))))

(defun money-in-raftel (graph gold isle turn max-turns)
  (if (equal isle "Raftel")
      gold
      (when (< turn max-turns)
	(let ((no-nil-results (remove nil (mapcar #'(lambda (next)
						      (if (equal (car next) isle) ;;pillage
							  (money-in-raftel graph
									   (+ gold 10)
									   isle
									   (1+ turn)
									   max-turns)
							  (when	(>= gold (+ (cadr next)
									    (svref (island-cost (gethash (car next) graph)) 0)))
							    (let ((new-gold (- gold
									       (cadr next)
									       (svref (island-cost (gethash (car next) graph)) (1+ turn)))))
							      (money-in-raftel graph
									       (if (< new-gold 0) 0 new-gold)
									       (car next)
									       (1+ turn)
									       max-turns)))))
						  (cons (list isle -10)  ;; pillage
							(island-adj (gethash isle graph)))))))
	  (when no-nil-results
	    (reduce #'max no-nil-results))))))

(defun reverse-adj (name isle)
  (declare (ignore name))
  (setf (island-adj isle) (reverse (island-adj isle))))

(defun read-graph (turns)
  (let ((graph (make-hash-table :test #'equal)))
    ;; islands
    (dotimes (_ turns)
      (let ((line (split-sequence #\Space (read-line *standard-input*) :remove-empty-subseqs t)))
	(setf (gethash (first line) graph) (new-island
					    (first line)
					    (parse-integer (second line))
					    turns))))
    ;; routes
    (dotimes (_ (read))
      (let ((line (split-sequence #\Space (read-line *standard-input*) :remove-empty-subseqs t)))
	(push (list (second line) (parse-integer (third line)))
	      (island-adj (gethash (first line) graph)))))
    ;; adjacencies need to be reversed
    (maphash #'reverse-adj graph)
    graph))

(defun read-ships ()
  (let* ((num-ships (read))
	 (ships (make-array (1+ num-ships))))
    (dotimes (i num-ships)
      (let ((line (split-sequence #\Space (read-line *standard-input*) :remove-empty-subseqs t)))
	(setf (svref ships (1+ i)) (new-ship (parse-integer (third line)) (fourth line)))))
    ships))

(defun process-in ()
  (let* ((max-turns (read))
	 (graph (read-graph max-turns))
	 (ships (read-ships)))
    (format t "~a~%" (money-in-raftel graph
				      (ship-gold (svref ships 1))
				      (ship-origin (svref ships 1))
				      0
				      (ships-costs graph ships)))))
;;    (maphash #'(lambda (x y) (format t "~a ~a ~%" x y)) graph)
;;    (format t "fastest: ~a~%" (ships-costs graph ships))
;;    (format t "~%")
;;    (maphash #'(lambda (x y) (format t "~a ~a ~%" x y)) graph)))

(process-in)
