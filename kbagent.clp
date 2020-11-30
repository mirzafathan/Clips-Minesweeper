(deftemplate box
	(multislot P)
	(slot safety)
	(slot number)
	(slot marked)
	(slot neighboring))

(defrule check
	(declare (salience -101))
	(box
		(P ?i ?j)
		(safety TRUE)
		(number ?n)
		(marked FALSE)
		(neighboring ?))
	(box
		(P ? ?)
		(safety FALSE)
		(number ?)
		(marked FALSE)
		(neighboring ?))
	=>
	(if (> ?n 0) then
		(assert(check-around ?i ?j))
	)
)

(deffunction is-neighbor
	(?i ?j ?k ?l)
	(or
		(and (= ?i (+ ?k 1)) (= ?j (+ ?l 1)) )
		(and (= ?i (+ ?k 1)) (= ?j ?l))
		(and (= ?i (+ ?k 1)) (= ?j (- ?l 1)) )
		(and (= ?i (- ?k 1)) (= ?j (+ ?l 1)) )
		(and (= ?i (- ?k 1)) (= ?j ?l) )
		(and (= ?i (- ?k 1)) (= ?j (- ?l 1)) )
		(and (= ?i ?k) (= ?j (- ?l 1)) )
		(and (= ?i ?k) (= ?j (+ ?l 1)) )
		))

(defrule set-neighbors
	(check-around ?i ?j)
	?g <- (box
		(P ?p ?q)
		(safety ?)
		(number ?)
		(marked ?)
		(neighboring FALSE))
	=>
	(if (is-neighbor ?i ?j ?p ?q) then
		(modify ?g (neighboring TRUE))
	))

(defrule set-not-neighbors
	(check-around ?i ?j)
	?g <- (box
		(P ?p ?q)
		(safety ?)
		(number ?)
		(marked ?)
		(neighboring TRUE))
	=>
	(if (not (is-neighbor ?i ?j ?p ?q)) then
		(modify ?g (neighboring FALSE))
	))

(deffunction count-safe-neighbors
	(?i ?j)
	(length$ (find-all-facts ((?f box)) (and (eq ?f:safety TRUE) (eq ?f:neighboring TRUE))))
	)

(deffunction count-marked-neighbors
	(?i ?j)
	(length$ (find-all-facts ((?f box)) (and (eq ?f:marked TRUE) (eq ?f:neighboring TRUE))))
	)

(defrule mark-box
	(declare (salience -99))
	?temp1 <- (check-around ?i ?j)
	(box
		(P ?i ?j)
		(safety TRUE)
		(number ?n)
		(marked FALSE)
		(neighboring FALSE))
	(box
		(P ?r ?s)
		(safety FALSE)
		(number ?)
		(marked FALSE)
		(neighboring TRUE))
	=>
;	(printout t "tes" ?r ?s crlf)
;	(printout t "ceking " ?i ?j crlf)
;	(printout t "nilai n " ?n crlf)
;	(printout t (count-safe-neighbors ?i ?j) crlf)
;	(printout t (= (count-safe-neighbors ?i ?j) (- 8 ?n)) crlf)
	(if (= (count-safe-neighbors ?i ?j) (- 8 ?n)) then
;		(printout t "sampe sini lancar" ?r ?s crlf)
		(assert(mark ?r ?s))
		(retract ?temp1)
		else
		(retract ?temp1))
)

(defrule open-box-safe
	(declare (salience -98))
	?temp <- (check-around ?i ?j)
	(box
		(P ?i ?j)
		(safety TRUE)
		(number ?n)
		(marked FALSE)
		(neighboring FALSE))
	(box
		(P ?r ?s)
		(safety FALSE)
		(number ?)
		(marked FALSE)
		(neighboring TRUE))
	=>
	(if (= (count-marked-neighbors ?i ?j) ?n) then
		(assert(open ?r ?s))
		(retract ?temp)
	)
)
