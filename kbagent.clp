(deffacts init
	(check-around 8 8)
	(box (P 8 8) (safety TRUE) (number 2) (marked FALSE) (neighboring FALSE))
	(box (P 7 7) (safety TRUE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 7 8) (safety TRUE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 7 9) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 8 7) (safety TRUE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 8 9) (safety TRUE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 9 7) (safety TRUE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 9 8) (safety TRUE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 9 9) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 4 2) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 4 0) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
	(box (P 2 2) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
	)

	(deffacts init
		(check-around 8 8)
		(box (P 8 8) (safety TRUE) (number 2) (marked FALSE) (neighboring FALSE))
		(box (P 7 7) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 7 8) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 7 9) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 8 7) (safety FALSE) (number 10) (marked TRUE) (neighboring FALSE))
		(box (P 8 9) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 9 7) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 9 8) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 9 9) (safety FALSE) (number 10) (marked TRUE) (neighboring FALSE))
		(box (P 4 2) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 4 0) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		(box (P 2 2) (safety FALSE) (number 10) (marked FALSE) (neighboring FALSE))
		)

(deftemplate box
	(multislot P)
	(slot safety)
	(slot number)
	(slot marked)
	(slot neighboring))

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
	?f <- (box
		(P ?r ?s)
		(safety ?)
		(number ?)
		(marked ?)
		(neighboring ?n))
	?g <- (box
		(P ?r ?s)
		(safety ?)
		(number ?)
		(marked ?)
		(neighboring ?n))
	=>
	(if (and (is-neighbor ?i ?j ?r ?s) (eq ?n FALSE)) then
		(modify ?g (neighboring TRUE))
		(printout t "t" crlf)
	else (if (and (not (is-neighbor ?i ?j ?r ?s)) (eq ?n TRUE)) then
	(modify ?f (neighboring FALSE))
	))
)

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
	(check-around ?i ?j)
	(box
		(P ?i ?j)
		(safety TRUE)
		(number ?n)
		(marked FALSE)
		(neighboring FALSE))
	?temp2 <- (box
		(P ?r ?s)
		(safety FALSE)
		(number ?)
		(marked FALSE)
		(neighboring TRUE))
	=>
	(printout t ?r ?s crlf)
	(printout t ?i ?j crlf)
	(printout t (count-safe-neighbors ?i ?j) crlf)
	(if (= (count-safe-neighbors ?i ?j) (- 8 ?n)) then
		(modify ?temp2 (marked TRUE))
		(assert(mark ?r ?s))
	)
)

(defrule open-box-safe
	(declare (salience -98))
	(check-around ?i ?j)
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
	)
)
