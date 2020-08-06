;; tail-recursive (using accumulator)
(defun reverse-list (lst)
  (labels ((aux (pending reversed)
             (if (null pending)
                 reversed
                 (aux (cdr pending) (cons (car pending) reversed)))))
    (aux lst ())))
