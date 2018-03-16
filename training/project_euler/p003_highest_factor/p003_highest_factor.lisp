;;; https://projecteuler.net/problem=3

(defun prime-p (n)
  (labels ((aux (i)
             (if (= i 1)
                 t
                 (if (zerop (mod n i))
                     nil
                     (aux (- i 1))))))
    (aux (floor (sqrt n)))))

(defun highest-factor (n)
  (labels ((aux (i)
             (if (= i 1)
                 n
                 (if (and (zerop (mod n i)) (prime-p i))
                     i
                     (aux (- i 1))))))
    (aux (floor (sqrt n)))))

(format t "~a~%" (highest-factor 600851475143))
