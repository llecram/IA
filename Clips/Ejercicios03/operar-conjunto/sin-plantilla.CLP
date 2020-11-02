(deffacts conjuntos-iniciales (conjunto01 A B D E L O P M N K) (conjunto02 H I J K L M B O E Q))
(defglobal ?*e1* = "")
(defglobal ?*e2* = "")
(defglobal ?*contador01* = 1)
(defglobal ?*contador02* = 1)
(defglobal ?*conjuntoFinal* = "")
(defglobal ?*valorIgual* = 0)

(defrule union-conjunto
	(conjunto01 $?valores01)
	(conjunto02 $?valores02)
=>
(bind ?*contador01* 1)
(bind ?*contador02* 1)
(bind ?*conjuntoFinal* "")
(while (<= ?*contador01* (length$ (mv-append $?valores01)))
	(bind ?*e1* (nth$ ?*contador01* (mv-append $?valores01)))
	(bind ?*conjuntoFinal* (str-cat ?*conjuntoFinal* " " ?*e1* " "))
	(bind ?*contador01* (+ ?*contador01* 1))
)
(while (<= ?*contador02* (length$ (mv-append $?valores02)))
	(bind ?*valorIgual* 0)
	(bind ?*contador01* 1)
	(bind ?*e2* (nth$ ?*contador02* (mv-append $?valores02)))
	(while (<= ?*contador01* (length$ (mv-append $?valores01)))
		(bind ?*e1* (nth$ ?*contador01* (mv-append $?valores01)))
		(if (eq ?*e1* ?*e2*) then (bind ?*valorIgual* 1))
		(bind ?*contador01* (+ ?*contador01* 1))
	)
	(if (= ?*valorIgual* 0) then (bind ?*conjuntoFinal* (str-cat ?*conjuntoFinal* " " ?*e2* " ")))
	(bind ?*contador02* (+ ?*contador02* 1))
)
(assert-string (str-cat "(conjunto03 " ?*conjuntoFinal* ")"))
(printout t "union: "  ?*conjuntoFinal* crlf))


(defrule interseccion-conjunto
	(conjunto01 $?valores01)
	(conjunto02 $?valores02)
=>
(bind ?*contador01* 1)
(bind ?*contador02* 1)
(bind ?*conjuntoFinal* "")
(while (<= ?*contador01* (length$ (mv-append $?valores01)))
	(bind ?*contador02* 1)
	(bind ?*e1* (nth$ ?*contador01* (mv-append $?valores01)))
	(while (<= ?*contador02* (length$ (mv-append $?valores02)))
		(bind ?*e2* (nth$ ?*contador02* (mv-append $?valores02)))
		(if (eq ?*e1* ?*e2*) then (bind ?*conjuntoFinal* (str-cat ?*conjuntoFinal* " " ?*e1* " ")))
		(bind ?*contador02* (+ ?*contador02* 1))
	)
	(bind ?*contador01* (+ ?*contador01* 1))
)
(assert-string (str-cat "(conjunto04 " ?*conjuntoFinal* ")"))
(printout t "intersection: "  ?*conjuntoFinal* crlf))





