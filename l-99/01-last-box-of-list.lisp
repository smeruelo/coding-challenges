(defun last-box (lst)
  (if (cdr lst)
      (last-box (cdr lst))
      lst))
