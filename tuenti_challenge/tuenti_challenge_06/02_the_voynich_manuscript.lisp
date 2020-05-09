#!/usr/bin/sbcl --script

(load "~/quicklisp/setup.lisp")
(with-output-to-string (*standard-output*) (ql:quickload :split-sequence))
(use-package :split-sequence)

(defun sublist (lst a b)
;; a,b must be < length; sublist is reversed
  (labels ((aux (list sublist i)
             (if (< i a)
                 (aux (cdr list) sublist (1+ i))
                 (if (<= i b)
                     (aux (cdr list) (cons (car list) sublist) (1+ i))
                     sublist))))
    (aux lst nil 0)))

(defun frequencies (lst)
  (let ((ht (make-hash-table :test 'equal)))
    (dolist (item lst)
      (incf (gethash item ht 0)))
    (let ((result-lst nil))
      (maphash #'(lambda (k v) (push (list k v) result-lst)) ht)
      result-lst)))

(defun three-most-frequent (corpus)
  (let ((ordered (sort (frequencies corpus) #'> :key #'cadr)))
    (list (first ordered) (second ordered) (third ordered))))

(defun process-in ()
  (let ((full-corpus (with-open-file (*standard-input* (second sb-ext:*posix-argv*))
                       (split-sequence #\Space (read-line) :remove-empty-subseqs t))))
    (dotimes (num-case (read))
      (let* ((a (read))
             (b (read))
             (corpus (sublist full-corpus (1- a) (1- b)))
             (result (three-most-frequent corpus)))
        (format t "Case #~a: ~{~{~a~^ ~}~^,~}~%" (1+ num-case) result)))))

(process-in)
