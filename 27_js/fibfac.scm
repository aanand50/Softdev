;; Team AY: Aditya and Stella
;; SoftDev pd5
;; K27 - Basic functions in Scheme
;; 2025-01-06m

;; Scheme implementation of factorial and Fibonacci functions

;; factorial:
(define (fact n)
  (if (= n 1)
      1
      (* n (fact (- n 1)))))


;; fib:
(define (fib n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib (- n 1)) (fib (- n 2))))))
