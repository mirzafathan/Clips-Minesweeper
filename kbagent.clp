(deffacts init
	(safe 0 0)
	(open 0 0))

(defrule test
	(open 0 0)
	=>
	(assert (open 0 1))
	(printout t "0 0 safe" crlf))