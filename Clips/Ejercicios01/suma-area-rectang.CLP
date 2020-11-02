;steps to run program
;(clear)
;load file
;(watch rules)
;(reset)
;(run)
;(unwatch rules)
;
;Global Variables
(defglobal ?*idx* = 0)
(defglobal ?*sum* = 0)
;Facts:
(deffacts hechos-iniciales (rectangulo A 9 6) (rectangulo B 7 5) (rectangulo C 6 9) (rectangulo D 2 5) )
;Rules:
(defrule sumar-areas
	(rectangulo ?nombre ?base ?altura)
	(test(< ?*idx* 4))
=>
	(bind ?*idx* (+ ?*idx* 1))
	(bind ?*sum* (+ (* ?base ?altura) ?*sum*)))

(defrule suma-total
=>
	(printout t ?*sum* " suma de areas total" crlf)
	(halt))




