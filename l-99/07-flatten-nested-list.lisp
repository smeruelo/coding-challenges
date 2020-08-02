(defun flatten (lst)
  (if (null lst)
      nil
      (if (listp (car lst))
          (append (flatten (car lst)) (flatten (cdr lst)))
          (append (list (car lst)) (flatten (cdr lst))))))
