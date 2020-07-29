(defun k-th (lst k)
  (if (= k 1)
	  (car lst)
	  (k-th (cdr lst) (- k 1))))
