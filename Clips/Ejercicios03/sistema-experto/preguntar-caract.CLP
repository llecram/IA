;preguntando caracteristicas

(defrule tiene-sangre-caliente
=>
(printout t "el animal tiene sangre caliente? (si/no): " crlf)
(assert-string (str-cat "(sangre-caliente " (readline) " )")) )

(defrule tiene-piel-con-pelo
=>
(printout t "el animal tiene piel con pelo? (si/no): " crlf)
(assert-string (str-cat "(piel-con-pelo " (readline) " )")) )

(defrule tiene-piel-con-plumas
=>
(printout t "el animal tiene piel con plumas? (si/no): " crlf)
(assert-string (str-cat "(piel-con-plumas " (readline) " )")) )

(defrule tiene-piel-con-escamas
=>
(printout t "el animal tiene piel con escamas? (si/no): " crlf)
(assert-string (str-cat "(piel-con-escamas " (readline) " )")) )

(defrule tiene-piel-porosa
=>
(printout t "el animal tiene piel porosa? (si/no): " crlf)
(assert-string (str-cat "(piel-porosa " (readline) " )")) )

(defrule movimiento-andante
=>
(printout t "el animal se mueve andando? (si/no): " crlf)
(assert-string (str-cat "(se-mueve-andando " (readline) " )")) )

(defrule movimiento-volando
=>
(printout t "el animal se mueve volando? (si/no): " crlf)
(assert-string (str-cat "(se-mueve-volando " (readline) " )")) )

;identificando categoria animal

(defrule mamifero
	(sangre-caliente si)
	(piel-con-pelo si)
	(se-mueve-andando si)
=>
(printout t "el animal descrito es un mamifero" crlf)(halt))

(defrule ave
	(sangre-caliente si)
	(piel-con-plumas si)
	(se-mueve-volando si)
=>
(printout t "el animal descrito es un ave" crlf)(halt))

(defrule reptil
	(sangre-caliente no)
	(piel-con-escamas si)
=>
(printout t "el animal descrito es un reptil" crlf)(halt))

(defrule anfibio
	(sangre-caliente no)
	(piel-porosa si)
=>
(printout t "el animal descrito es un anfibio" crlf)(halt))

(defrule murcielago
	(sangre-caliente si)
	(piel-con-pelo si)
	(se-mueve-andando no)
=>
(printout t "el animal descrito es un murcielago" crlf)(halt))

(defrule avestruz
	(sangre-caliente si)
	(piel-con-plumas si)
	(se-mueve-volando no)
=>
(printout t "el animal descrito es un avestruz" crlf)(halt))

(defrule sin-categoria
	(piel-con-pelo ?var1)
	(se-mueve-andando ?var2)
	(piel-con-plumas ?var3)
	(se-mueve-volando ?var4)
	(piel-con-escamas ?var5)
	(piel-porosa ?var6)
	(sangre-caliente ?var7)
=>
(printout t "el animal descrito no tiene categoria" crlf))
