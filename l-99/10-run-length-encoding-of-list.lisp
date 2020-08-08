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

(defun encode-sublst (sublst)  ;; assume non empty sublst, and every element is the same
  (cons (length sublst) (list (car sublst))))

(defun encode (lst)
  (labels ((aux (done pending)
             (if (null pending)
                 (reverse done)
                 (aux (cons (encode-sublst (car pending)) done) (cdr pending)))))
    (aux '() (pack lst))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; 2. tail-recursive (not reusing pack function, but modifying it)
(defun encode (lst)
  (labels ((aux (done count pending)
             (cond
               ((null pending) (reverse done))
               ((eql (car pending) (cadr pending)) (aux done
                                                        (+ count 1)
                                                        (cdr pending)))
               (t (aux (cons (list (+ count 1) (car pending)) done)
                       0
                       (cdr pending))))))
    (aux '() 0 lst)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; 3. no tail-recursive, building the output backwards
(defun pack (lst)
  (if (null lst)
      '()
      (let ((hd (car lst))
            (packed (pack (cdr lst))))
        (cond
          ((null packed) (list (list hd)))
          ((eql hd (caar packed)) (cons (cons hd (car packed)) (cdr packed)))
          (t (cons (list hd) packed))))))

(defun encode-sublst (sublst)  ;; assume non empty sublst, and every element is the same
  (cons (length sublst) (list (car sublst))))

(defun encode (lst)
  (labels ((aux (pending)
             (if (null pending)
                 '()
                 (cons (encode-sublst (car pending)) (aux (cdr pending))))))
    (aux (pack lst))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; 4. no tail-recursive, (not reusing pack function, but modifying it)
(defun encode (lst)
  (if (null lst)
      '()
      (let ((hd (car lst))
            (encoded (encode (cdr lst))))
        (cond
          ((null encoded) (list (list 1 hd)))
          ((eql hd (cadar encoded)) (cons (list (+ (caar encoded) 1) (cadar encoded))
                                          (cdr encoded)))
          (t (cons (list 1 hd) encoded))))))
