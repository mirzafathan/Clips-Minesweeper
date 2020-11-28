(deffacts init
	(open 0 0))

;(deffunction)

(defrule move
	?done <- (open ?i ?j)
	=>
	(retract ?done)
	(assert(safe ?i ?j)))

;(defrule mark-box-1-center
;	(size ?n)
;	(one ?i ?j)
;	(<> ?i 0)
;	(<> ?j 0)
;	(<> ?i -(?n 1))
;	(<> ?j -(?n 1))
;	((tostring ?x ?y) ~safe)
;	()
;	=>
;	(mark ?i ?j)
;)