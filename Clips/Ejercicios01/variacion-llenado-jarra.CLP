;steps to run program
;(clear)
;load file
;(watch rules)
;(reset)
;(run)
;(unwatch rules)
;
;Facts:
(deffacts hechos-iniciales (contenido jarra 0) (agregar 1) (agregar 2))
;Rules:
(defrule aumentar-1-litro
	(contenido jarra ?litros)
	(agregar 1)
	(test(<= ?litros 2))
=>
	(assert(contenido jarra (+ ?litros 1)))
	(printout t (+ ?litros 1) "litros ahora  - (+1 litro)" crlf))

(defrule aumentar-2-litro
	(contenido jarra ?litros)
	(agregar 2)
	(test(<= ?litros 1))
=>
	(assert(contenido jarra (+ ?litros 2)))
	(printout t (+ ?litros 2) "litros ahora - (+2 litros)" crlf))

(defrule jarra-llena
	(contenido jarra 3)
=>
	(printout t "jarra de 3 litros llena" crlf)
	(halt))
