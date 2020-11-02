;steps to run program
;(clear)
;load file
;(watch rules)
;(reset)
;(run)
;(unwatch rules)
;
;Facts:
(deffacts hechos-iniciales (lista a b c d e f g))
;Rules:
(defrule obtener-primero
	(lista ?primero $?valores ?ultimo)
=>
	(assert (lista ?primero))
	(printout t ?primero " primer elemento de lista" crlf))

(defrule obtener-ultimo
	(lista ?primero $?valores ?ultimo)
=>
	(assert (lista ?ultimo))
	(printout t ?ultimo " ultimo elemento de lista" crlf))

(defrule intercambio-primero-ultimo
	(lista ?primero $?valores ?ultimo)
=>
	(assert (lista ?ultimo $?valores ?primero))
	(printout t "lista intercambiada: " ?ultimo $?valores ?primero crlf)
	(halt))
