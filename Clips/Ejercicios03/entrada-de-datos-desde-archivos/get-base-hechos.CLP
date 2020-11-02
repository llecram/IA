(defglobal ?*linea* = "")
(defglobal ?*registro* = "(persona ")
(defrule leer-nombres
=>
(open "C:/Users/HECTOR/Desktop/IA/Clips/Ejercicios03/entrada-de-datos-desde-archivos/registro-datos.txt" fichero)
(while (neq (bind ?*linea* (readline fichero)) EOF)
	(bind ?*registro*(str-cat "(persona " ?*linea* " )"))
	(assert-string ?*registro*))
(close fichero))

