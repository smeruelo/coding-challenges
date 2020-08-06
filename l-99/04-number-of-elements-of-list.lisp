;; no tail-recursive
(defun count-elements (lst)
  (if (null lst)
      0
      (+ 1 (count-elements (cdr lst)))))

;; tail-recursive
(defun count-elements (lst)
  (labels ((aux (l c)
             (if (null l)
                 c
                 (aux (cdr l) (+ c 1)))))
    (aux lst 0)))
