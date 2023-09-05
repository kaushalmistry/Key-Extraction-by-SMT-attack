( set-info:smt-lib-version 4.12 )
( declare-const a Int )
( declare−const b Int )
( declare−const k11 Int )
( declare−const k21 Int )
( declare−const k12 Int )
( declare−const k22 Int )
( declare−const out1 Int )
( declare−const out2 Int )
( declare−const c1 Bool )
( declare−const c2 Bool )
( define−fun G((a Int)(b Int)) Bool(> a b) )
(define−fun A((a Int)(b Int)(x1 Int)(x2 Int)(x3 Bool)(c Bool)) Int (ite (xor c x3) (+ a x1 ) (∗ b x2 ))

(assert (= out1 (A a b k11 k21 c1 (G a b ) ) ) )
(assert (= out2 (A a b k12 k22 c2 (G a b ) ) ) )




(assert (not(= out1 out2)))
(check−sat )
(get−model )
