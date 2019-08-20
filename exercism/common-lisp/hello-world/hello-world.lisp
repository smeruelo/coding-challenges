;;; https://exercism.io/my/solutions/619c864ade5f460c887c66ad377ebc1e

(defpackage #:hello-world
  (:use #:common-lisp)
  (:export #:hello-world)
  (:nicknames #:hw))

(in-package #:hello-world)

(defun hello-world ()
  "Hello, World!")
