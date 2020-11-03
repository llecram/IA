(defglobal ?*numero* = (random 0 100))
(defrule adivinar
	?h <- (adivinar)
	=>
	(retract ?h)
	(printout t "Escribe un numero ")
	(assert (numero (read))))
(defrule menor
	?h <- (numero ?n&:(< ?n ?*numero*))
	=>
	(retract ?h)
	(printout t ?n "es menor" crlf)
	(assert (adivinar)))
(defrule mayor
	?h <- (numero ?n&:(> ?n ?*numero*))
	=>
	(retract ?h)
	(printout t ?n "es mayor" crlf)
	(assert (adivinar)))
(defrule exacto
	?h <- (numero ?n&:(= ?n ?*numero*))
	=>
	(retract ?h)
	(printout t ?n "es el numero correcto" crlf))
