from z3 import *
a = Int('a')
b = Int('b')
c1 = Bool('c1')
c2 = Bool('c2')

k11 = Int('k11')
k12 = Int('k12')

k21 = Int('k21')
k22 = Int('k22')


# def A(a, b, x1, x2, x3):
#     # print(x3)
#     # print(a)
#     # print(b)
#     # print(type(a))
#     # print(type(x3))
#     print((a>b) == x3)
#     t = simplify(a>b)
#     t1 = simplify(t ^ x3)

#     t2 = If((a>b) == x3, b * x2, a + x1)
#     return simplify(t2)


# out1 = A(a, b, k11, k21, c1)
# out2 = A(a, b, k12, k22, c2)

# print(out1)
# print(out2)

s = Solver()

# s.add(out1 != out2)
# solve(out1 != out2)
# out1 = simplify(If(Xor((a>b), c1), b * k21, a + k11))
# out2 = simplify(If(Xor((a>b), c2), b * k22, a + k12))
# s.add(If(Xor((a>b), c1), b * k21, a + k11))
# s.add(out2)

# s.add(out1 != out2)

def A(a, b, c, k1, k2):
    t1 = Xor((a>b), c)

    o1 = simplify(If(t1, a + k1, b * k2))

    return o1


s.add(0 == A(0, 0, c1, k11, k21))
s.add(0 == A(0, 0, c2, k12, k22))

# s.add(0 == If(Xor((0>0), c1), 0 + k11, 0 * k21))
# s.add(0 == If(Xor((0>0), c2), 0 + k12, 0 * k22))

s.add(21 == A(-3, 7, c1, k11, k21))
s.add(21 == A(-3, 7, c2, k12, k22))

# s.add(21 == If(Xor((-3>7), c1), -3 + k11, 7 * k21))
# s.add(21 == If(Xor((-3>7), c2), -3 + k12, 7 * k22))


s.add(20 == A(15, 14, c1, k11, k21))
s.add(20 == A(15, 14, c2, k12, k22))
# s.add(20 == If(Xor((15>14), c1), 15 + k11, 14 * k21))
# s.add(20 == If(Xor((15>14), c2), 15 + k12, 14 * k22))

# t1 = Xor((a>b), c1)
# t2 = Xor((a>b), c2)

# o1 = simplify(If(t1, a + k11, b * k21))
# o2 = simplify(If(t2, a + k12, b * k22))
s.add(k11 == k12, k21 == k22, c1 == c2)
# s.add(A(a, b, c1, k11, k21) != A(a, b, c2, k12, k22))
s.add(A(a, b, c1, k11, k21) == A(a, b, c2, k12, k22))
# s.add(simplify(If(Xor((a>b), c1), a + k11, b * k21)) == simplify(If(Xor((a>b), c2), a + k12, b * k22)))

# print (s.check())
if (s.check() == sat):
    print("sat")
    print(s.model())
else:
    print("unsat")

