(deffacts init
	("0 0" safe)
	(open 0 0))

(deffunction totuple
	(?s)
	(explode$ ?s))

(deffunction tostring
	(?i ?j)
	(implode$ (create$ ?i ?j)))

(deffunction)

(defrule move
	("")
	?done <- (open ?i ?j)
	=>
	(retract ?done))

(defrule mark-box-1-center
	(size ?n)
	(one ?i ?j)
	(<> ?i 0)
	(<> ?j 0)
	(<> ?i -(?n 1))
	(<> ?j -(?n 1))
	((tostring i j) safe
	=>
	(mark ?i ?j)
)