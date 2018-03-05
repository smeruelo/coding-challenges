;;#!/usr/bin/sbcl --script

(declaim (optimize (speed 3)))


(load "quicklisp/setup.lisp")
(require :split-sequence)
(use-package :split-sequence)

(defvar *num-scenarios* 75)
(defvar *scenarios* (make-array *num-scenarios*))
(defvar *stamina* (make-array *num-scenarios*))
(defvar *max-stamina* 4001)
(defvar *mt* (make-hash-table :test #'eq))
(defvar *roomlst* nil)
(defvar *mod* 1000000007)
(defvar *binomials* (make-array (list 500 500)))

;; functions to access door info
(defun door-target (door)
  (first door))
(defun door-keys (door)
  (second door))
(defun door-stamina (door)
  (third door))

;; functions to access room info
(defun room-label (room)
  (first room))
(defun room-ndoors (room)
  (second room))
(defun room-doorlst (room)
  (cddr room))

(defun prodmod (x y)
  (mod (* (mod x *mod*) (mod y *mod*)) *mod*))

(defun add-stamina (initial current extra)
  (let ((new (+ current extra)))
    (if (> new initial)
	initial
	new)))

(defun binomial-coefficient (m n)
  (aref *binomials* m n))

(defun bc (m n)
  (defun factorial (n)
    (labels ((iter (i accum)
	       (if (< i 2)
		   accum
		   (iter (1- i) (* accum i)))))
      (iter n 1)))
  (/ (factorial m) (* (factorial n) (factorial (- m n)))))

(defun calc-binomials ()
  (dotimes (i 500)
    (dotimes (j 500)
      (setf (aref *binomials* i j) (mod (bc i j) *mod*)))))

(defun init-mt ()
  (dolist (room *roomlst*)
    (setf (gethash room *mt*) (make-array *max-stamina* :initial-element nil))))

(defun room-ff (doorsff)
  (let ((nonull (remove nil doorsff)))
    (if nonull
	(reduce #'+ nonull)
	0)))

(defun sets (s)
  "ugliest code ever"
  (let ((init-stamina (svref *stamina* s)))
    (init-mt)
    (labels ((iter (stamina room ff)
	       (if (null room) ;; exit
		   ff
		   (let* ((known-value (svref (gethash (room-label room) *mt*) stamina)))
		     (if known-value
			 (prodmod ff known-value)
			 (prodmod ff (setf (svref (gethash (room-label room) *mt*) stamina)
				     (room-ff (loop for door in (remove-if #'(lambda (x) (> (door-stamina x) init-stamina)) (room-doorlst room)) collect
						   (let ((needed-keys (door-keys door))
							 (init-num-minions (room-ndoors room))
							 (current-stamina stamina)
							 (next-room (door-target door))
							 (stamina-needed (door-stamina door)))
						     (when (<= needed-keys init-num-minions)
						       (let ((minions-killed (if (> needed-keys 0) needed-keys 1)))
							 (setf current-stamina (add-stamina init-stamina current-stamina minions-killed))
							 (if (> stamina-needed current-stamina)
							     (when (>= (- init-num-minions minions-killed) (- stamina-needed current-stamina))
							       (setf minions-killed (+ minions-killed (- stamina-needed current-stamina)))
							       (iter 0
								     (gethash next-room (svref *scenarios* s))
								     (binomial-coefficient (1- init-num-minions) (1- minions-killed))))
							     (iter (add-stamina init-stamina current-stamina (- stamina-needed))
								   (gethash next-room (svref *scenarios* s))
								   (binomial-coefficient (1- init-num-minions) (1- minions-killed))))))))))))))))
      (mod (iter init-stamina (gethash (intern "start") (svref *scenarios* s)) 1) *mod*))))

(defun read-scenarios ()
  (with-open-file (file "scenarios.txt")
    (dotimes (s (read file))
      (setf (svref *scenarios* s) (make-hash-table :test #'eq))
      (setf (svref *stamina* s) (read file))
      (dotimes (room (read file))
	(let* ((line (split-sequence #\Space (read-line file) :remove-empty-subseqs t))
	       (room-label (intern (first line)))
	       (num-doors (parse-integer (second line))))
	  (push room-label *roomlst*)
	  (setf (gethash room-label (svref *scenarios* s)) (list room-label num-doors))
	  (dotimes (door num-doors)
	    (let* ((line (split-sequence #\Space (read-line file) :remove-empty-subseqs t))
		   (target (intern (first line)))
		   (keys (parse-integer (second line)))
		   (stamina (parse-integer (third line))))
	      (push (list target keys stamina) (cddr (gethash room-label (svref *scenarios* s)))))))))))

(defun process-in ()
  (read-scenarios)
  (calc-binomials)
  (format t "binomials done ~%")
  (labels ((iter (s)
                 (when s
                   (format t "Scenario ~a: ~a~%" s (sets s))
                   (iter (read *standard-input* nil)))))
    (iter (read))))

;; (require :sb-sprof)
;; (sb-sprof:with-profiling (:max-samples 1000
;; 				       :report :flat
;; 				       :loop nil)

(process-in)
