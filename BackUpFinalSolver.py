from z3 import *

i1, i2, i3, i4, i5 = Ints('i1 i2 i3 i4 i5')
g1, g2 = Ints('g1 g2')
gg1, gg2 = Ints('gg1 gg2')
k11, k21, k31, k41 = Ints('k11 k21 k31 k41')
k51, k61, k71 = Bools('k51 k61 k71')
k12, k22, k32, k42 = Ints('k12 k22 k32 k42')
k52, k62, k72 = Bools('k52 k62 k72')

def getSetGo(i1, i2, i3, i4, i5, g1, g2, gg1, gg2, k1, k2, k3, k4, k5, k6, k7):
    op1 = gg1 * i1
    op2 = gg2 * i2
    op3 = g1 * i2
    op4 = g2 * i1

    op5 = If(g1 > 10, (g1*i3)+gg1, i3*i4)
    op6 = If(g1 > 10, op5 - op4, op5 - op3)

    op6 = If(Not(Xor((op5 < op4), k7)), (g2 * i4) - i3, op6)

    op17 = op2 - op4
    op2 = If(Not(Xor((op5 < op4), k7)), op2, op4 - op17)
    op17 = If(Not(Xor((op5 < op4), k7)), op6 - g2, op17 - op2)

    op7 = g1 * i4
    op8 = g2 * i3

    op9 = op1 + op2
    op10 = op3 + op4
    op11 = op4 + op6
    op12 = op7 + op8

    op13 = op11 + g1
    o1 = op13 + k1

    op14 = i5 + op12
    o2 = op14 + k2

    op15 = g1 * op14
    op16 = op13 * g2

    op17 = If(op13 == op14, op17 * op11, op17)
    op14 = If(op13 == op14, op14 - op17, op13 * g1)
    op15 = If(op13 == op14, op15 + op17, op15)

    op18 = op14 * g2
    op19 = op15 * op16
    op20 = op17 + op18
    op21 = g1 * op20
    op22 = op19 * g2
    op23 = op19 * g1
    op24 = If(k5, op20 + g1, op20 * g2)
    op25 = op21 + op22
    op26 = If(k6, op23 + op24, op23 - 1)
    o3 = op9 + op25 / k3

    op28 = op10 + op26
    o4 = op28 + k4

    return simplify(o1), simplify(o2), simplify(o3), simplify(o4)


s = Solver()

s.add(k31 != 0)
s.add(k32 != 0)

## Iteration 1
a11, a21, a31, a41 = getSetGo(5, -1, -1, 1, -2, -2, 1, 3, -1, k11, k21, k31, k41, k51, k61, k71)
a12, a22, a32, a42 = getSetGo(5, -1, -1, 1, -2, -2, 1, 3, -1, k11, k21, k31, k41, k51, k61, k71)

s.add(-84 == a11)
s.add(-84 == a12)
s.add(1238 == a21)
s.add(1238 == a22)
s.add(25 == a31)
s.add(25 == a32)
s.add(-111 == a41)
s.add(-111 == a42)


# iteration 2
a11, a21, a31, a41 = getSetGo(1, -1, -1, 0, 1, -1, -1, 1, -1, k11, k21, k31, k41, k51, k61, k71)
a12, a22, a32, a42 = getSetGo(1, -1, -1, 0, 1, -1, -1, 1, -1, k11, k21, k31, k41, k51, k61, k71)

s.add(-92 == a11)
s.add(-92 == a12)
s.add(1245 == a21)
s.add(1245 == a22)
s.add(-2 == a31)
s.add(-2 == a32)
s.add(-5 == a41)
s.add(-5 == a42)


# iteration 3
a11, a21, a31, a41 = getSetGo(0, 1, -1, -1, -1, -2, 0, 1, -2, k11, k21, k31, k41, k51, k61, k71)
a12, a22, a32, a42 = getSetGo(0, 1, -1, -1, -1, -2, 0, 1, -2, k11, k21, k31, k41, k51, k61, k71)

s.add(-88 == a11)
s.add(-88 == a12)
s.add(1244 == a21)
s.add(1244 == a22)
s.add(5 == a31)
s.add(5 == a32)
s.add(-11 == a41)
s.add(-11 == a42)


# iteration 4
# a11, a21, a31, a41 = getSetGo(1, -1, 2, -1, -1, -1, -1, 1, -1, k11, k21, k31, k41, k51, k61, k71)
# a12, a22, a32, a42 = getSetGo(1, -1, 2, -1, -1, -1, -1, 1, -1, k11, k21, k31, k41, k51, k61, k71)

# s.add(-92 == a11)
# s.add(-92 == a12)
# s.add(1241 == a21)
# s.add(1241 == a22)
# s.add(2 == a31)
# s.add(2 == a32)
# s.add(-12 == a41)
# s.add(-12 == a42)


s11, s21, s31, s41 = getSetGo(i1, i2, i3, i4, i5, g1, g2, gg1, gg2, k11, k21, k31, k41, k51, k61, k71)
s12, s22, s32, s42 = getSetGo(i1, i2, i3, i4, i5, g1, g2, gg1, gg2, k12, k22, k32, k42, k52, k62, k72)


# s.add(s11 != s12)
# s.add(s21 != s22)
# s.add(s31 != s32)
# s.add(s41 != s42)
s.add(s11 == s12)
s.add(s21 == s22)
s.add(s31 == s32)
s.add(s41 == s42)
s.add(k11==k12,k21==k22,k31==k32,k41==k42,k51==k52,k61==k62,k71==k72)

if (s.check() == sat):
    print("sat")
    m = s.model()
    print("i1 = ", m[i1])
    print("i2 = ", m[i2])
    print("i3 = ", m[i3])
    print("i4 = ", m[i4])
    print("i5 = ", m[i5])
    print("g1 = ", m[g1])
    print("g2 = ", m[g2])
    print("gg1 = ", m[gg1])
    print("gg2 = ", m[gg2])
    print("------Keys-------")
    print("K11 = ", m[k11])
    print("K12 = ", m[k12])
    print("K21 = ", m[k21])
    print("K22 = ", m[k22])
    print("K31 = ", m[k31])
    print("K32 = ", m[k32])
    print("K41 = ", m[k41])
    print("K42 = ", m[k42])
    print("K51 = ", m[k51])
    print("K52 = ", m[k52])
    print("K61 = ", m[k61])
    print("K62 = ", m[k62])
    print("K71 = ", m[k71])
    print("K72 = ", m[k72])
else:
    print("unsat")


