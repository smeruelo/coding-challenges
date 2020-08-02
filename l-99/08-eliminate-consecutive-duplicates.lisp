;; no tail-recursive
(defun no-consecutive-dups (lst)
  (if (null lst)
	  nil
	  (if (eql (car lst) (cadr lst))
		  (no-consecutive-dups (cdr lst))
		  (cons (car lst) (no-consecutive-dups (cdr lst))))))


;; tail-recursive
(defun no-consecutive-dups (lst)
  (defun aux (done pending)
	(if (null pending)
		(reverse done)
		(if (eql (car done) (car pending))
			(aux done (cdr pending))
			(aux (cons (car pending) done) (cdr pending)))))
  (aux () lst))
