(defun last-but-one-box (lst)
  (if (<= (length lst) 2)
      lst
      (last-but-one-box (cdr lst))))
