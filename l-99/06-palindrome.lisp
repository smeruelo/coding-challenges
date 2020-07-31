;; from scratch

(defun my-reverse (lst)
  (defun aux1 (pending reversed)
	(if (null pending)
		reversed
		(aux1 (cdr pending) (cons (car pending) reversed))))
  (aux1 lst ()))

(defun palindromep (lst)
  (defun aux2 (pending pending-rev)
	(if (null pending)  ;; we could check just half the list
		t
		(if (eq (car pending) (car pending-rev))
			(aux2 (cdr pending) (cdr pending-rev))
			nil)))
  (aux2 lst (my-reverse lst)))


;; using existing functions

(defun palindromep (lst)
  (equal lst (reverse list)))
