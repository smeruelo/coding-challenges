;; 1. from scratch

;; tail-recursive (using accumulator)
(defun my-reverse (lst)
  (labels ((aux (pending reversed)
             (if (null pending)
                 reversed
                 (aux (cdr pending) (cons (car pending) reversed)))))
    (aux lst ())))

(defun palindromep (lst)
  (labels ((aux (pending pending-rev)
             (if (null pending)  ;; we could check just half the list
                 t
                 (if (eq (car pending) (car pending-rev))
                     (aux (cdr pending) (cdr pending-rev))
                     nil))))
    (aux lst (my-reverse lst))))


;; 2. using existing functions

(defun palindromep (lst)
  (equal lst (reverse list)))
