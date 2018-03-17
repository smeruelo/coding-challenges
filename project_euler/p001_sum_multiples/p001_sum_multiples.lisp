;;; https://projecteuler.net/problem=1

(defun multiple-p (i j)
  (and (not (zerop i)) (zerop (mod i j))))

(defun sum (n)
  (labels ((aux (i acc)
             (if (< i n)
                 (if (or (multiple-p i 3) (multiple-p i 5))
                     (aux (+ i 1) (+ acc i))
                     (aux (+ i 1) acc))
                  acc)))
    (aux 3 0)))

(format t "~a~%" (sum 1000))
