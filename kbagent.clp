(deffacts init
	(open 0 0))

(defrule neighbors
	(check ?i ?j)
	=>
	(assert(around -(?i 1) -(?j 1)))
	(assert(around -(?i 1) ?j))
	(assert(around -(?i 1) +(?j 1)))
	(assert(around ?i -(?j 1)))
	(assert(around ?i +(?j 1)))
	(assert(around +(?i 1) -(?j 1)))
	(assert(around +(?i 1) ?j))
	(assert(around +(?i 1) +(?j 1)))
	)

(deffunction notsame
	(?a ?b ?c ?d ?e ?f ?g ?h ?i ?j ?k ?l ?m ?n ?o ?p)
	( and
		(or (<> ?a ?c) (<> ?b ?d))
		(or (<> ?a ?e) (<> ?b ?f))
		(or (<> ?a ?g) (<> ?b ?h))
		(or (<> ?a ?i) (<> ?b ?j))
		(or (<> ?a ?k) (<> ?b ?l))
		(or (<> ?a ?m) (<> ?b ?n))
		(or (<> ?a ?o) (<> ?b ?p))
		(or (<> ?c ?e) (<> ?d ?f))
		(or (<> ?c ?g) (<> ?d ?h))
		(or (<> ?c ?i) (<> ?d ?j))
		(or (<> ?c ?k) (<> ?d ?l))
		(or (<> ?c ?m) (<> ?d ?n))
		(or (<> ?c ?o) (<> ?d ?p))
		(or (<> ?e ?g) (<> ?f ?h))
		(or (<> ?e ?i) (<> ?f ?j))
		(or (<> ?e ?k) (<> ?f ?l))
		(or (<> ?e ?m) (<> ?f ?n))
		(or (<> ?e ?o) (<> ?f ?p))
		(or (<> ?g ?i) (<> ?h ?j))
		(or (<> ?g ?k) (<> ?h ?l))
		(or (<> ?g ?m) (<> ?h ?n))
		(or (<> ?g ?o) (<> ?h ?p))
		(or (<> ?i ?k) (<> ?j ?l))
		(or (<> ?i ?m) (<> ?j ?n))
		(or (<> ?i ?o) (<> ?j ?p))
		(or (<> ?k ?m) (<> ?l ?n))
		(or (<> ?k ?o) (<> ?l ?p))
		(or (<> ?m ?o) (<> ?n ?p))
		))

(defrule check-box-one
	(one ?x ?y)
	(unsafe ? ?)
	=>
	(check ?x ?y))

(defrule check-box-two
	(two ?x ?y)
	(unsafe ? ?)
	=>
	(check ?x ?y))

(defrule check-box-three
	(three ?x ?y)
	(unsafe ? ?)
	=>
	(check ?x ?y))

(defrule check-box-four
	(four ?x ?y)
	(unsafe ? ?)
	=>
	(check ?x ?y))

(defrule mark-box-one-unsafe
	(check ?x ?y)
	(one ?x ?y)
	(around ?a ?b)
	(safe ?a ?b)
	(around ?c ?d)
	(safe ?c ?d)
	(around ?e ?f)
	(safe ?e ?f)
	(around ?g ?h)
	(safe ?g ?h)
	(around ?i ?j)
	(safe ?i ?j)
	(around ?k ?l)
	(safe ?k ?l)
	(around ?m ?n)
	(safe ?m ?n)
	(around ?o ?p)
	(unsafe ?o ?p)
	=>
	(if(notsame (?a ?b ?c ?d ?e ?f ?g ?h ?i ?j ?k ?l ?m ?n ?o ?p)) then
		(assert(mark ?o ?p)))
	)

(defrule mark-box-one-safe
	(check ?x ?y)
	(one ?x ?y)
	(around ?a ?b)
	(around ?c ?d)
	(around ?e ?f)
	(around ?g ?h)
	(around ?i ?j)
	(around ?k ?l)
	(around ?m ?n)
	(around ?o ?p)
	(mark ?o ?p)
	=>
	(if(notsame (?a ?b ?c ?d ?e ?f ?g ?h ?i ?j ?k ?l ?m ?n ?o ?p)) then
		(assert(safe ?a ?b))
		(assert(safe ?c ?d))
		(assert(safe ?e ?f))
		(assert(safe ?g ?h))
		(assert(safe ?i ?j))
		(assert(safe ?k ?l))
		(assert(safe ?m ?n)))
	))


(defrule mark-box-two
	(check ?x ?y)
	(two ?x ?y)
	(around ?a ?b)
	(safe ?a ?b)
	(around ?c ?d)
	(safe ?c ?d)
	(around ?e ?f)
	(safe ?e ?f)
	(around ?g ?h)
	(safe ?g ?h)
	(around ?i ?j)
	(safe ?i ?j)
	(around ?k ?l)
	(safe ?k ?l)
	(around ?m ?n)
	(unsafe ?m ?n)
	(around ?o ?p)
	(unsafe ?o ?p)
	=>
	if(notsame (?a ?b ?c ?d ?e ?f ?g ?h ?i ?j ?k ?l ?m ?n ?o ?p) then
		(assert(mark ?m ?n))
		(assert(safe ?m ?n))
		(assert(mark ?o ?p))
		(assert(safe ?o ?p))
	))

(defrule mark-box-three
	(check ?x ?y)
	(two ?x ?y)
	(around ?a ?b)
	(safe ?a ?b)
	(around ?c ?d)
	(safe ?c ?d)
	(around ?e ?f)
	(safe ?e ?f)
	(around ?g ?h)
	(safe ?g ?h)
	(around ?i ?j)
	(safe ?i ?j)
	(around ?k ?l)
	(unsafe ?k ?l)
	(around ?m ?n)
	(unsafe ?m ?n)
	(around ?o ?p)
	(unsafe ?o ?p)
	=>
	if(notsame (?a ?b ?c ?d ?e ?f ?g ?h ?i ?j ?k ?l ?m ?n ?o ?p) then
		(assert(mark ?k ?l))
		(assert(safe ?k ?l))
		(assert(mark ?m ?n))
		(assert(safe ?m ?n))
		(assert(mark ?o ?p))
		(assert(safe ?o ?p))
	))
