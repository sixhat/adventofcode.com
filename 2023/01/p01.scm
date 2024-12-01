#lang racket

(require 2htdp/batch-io)
(define data (read-lines "input"))

(define (process-line el)
  (displayln el)
  (let* (
      [line (string->list el)]
      [tam (length line)])
    (displayln tam)
    (displayln line)
    (for ([i (in-list line)])
      (displayln i))
    )
  )
            

;(for-each process-line data)
(displayln (url-html-neighbors "https://www.sixhat.net"))
