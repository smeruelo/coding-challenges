;; 1. tail-recursive (using accumulator, then reversing it) (using temporal sublist)
(defun pack (lst)
  (labels ((aux (done current pending)
             (cond
               ((null pending) (reverse done))
               ((eql (car pending) (cadr pending)) (aux done
                                                        (cons (car pending) current)
                                                        (cdr pending)))
               (t (aux (cons (cons (car pending) current) done)
                       '()
                       (cdr pending))))))
    (aux '() '() lst)))



;; 2. no tail-recursive, building the output backwards
(defun pack (lst)
  (if (null lst)
      '()
      (let ((hd (car lst))
            (packed (pack (cdr lst))))
        (cond
          ((null packed) (list (list hd)))
          ((eql hd (caar packed)) (cons (cons hd (car packed)) (cdr packed)))
          (t (cons (list hd) packed))))))
