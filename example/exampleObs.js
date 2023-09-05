const a = Z3.Int.const('a');
const b = Z3.Int.const('b');
const k11 = Z3.Int.const('k11');
const k21 = Z3.Int.const('k21');
const k12 = Z3.Int.const('k12');
const k22 = Z3.Int.const('k22');
// const out1 = Z3.Int.const('out1');
// const out2 = Z3.Int.const('out2');
const c1 = Z3.Bool.const('c1');
const c2 = Z3.Bool.const('c2');

function G(a: Int, b: Int) {
    return a > b;
}

function A(a, b, x1, x2, x3, c) {
    if (c ^ x3) {
        return a + x1;
    }
    return b * x2;
}

const out1 = A(a, b, k11, k21, c1, G(a, b))
const out2 = A(a, b, k12, k22, c2, G(a, b))

Z3.solve(out1.eq(out2));