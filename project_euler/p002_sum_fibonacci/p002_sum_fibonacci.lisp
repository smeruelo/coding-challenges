;;; https://projecteuler.net/problem=2

(defun fibonacci (n)
  (labels ((aux (fib last1 last2)
             (let ((current (+ last1 last2)))
               (if (> current n)
                 fib
                 (aux (cons current fib) current last1)))))
    (aux '(1 1) 1 1)))

(format t "~a~%" (reduce '+ (remove-if-not 'evenp (fibonacci 4000000))))
