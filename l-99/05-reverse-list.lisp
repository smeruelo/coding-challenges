(defun reverse-list (lst)
  (defun aux (pending reversed)
	(if (null pending)
		reversed
		(aux (cdr pending) (cons (car pending) reversed))))
  (aux lst ()))
