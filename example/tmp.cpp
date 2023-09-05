#include "minisat/core/Solver.h"
using namespace Minisat;

int main() {
    Solver solver;

    // Add variables A, B, and C to the solver
    Var a = solver.newVar();
    Var b = solver.newVar();
    Var c = solver.newVar();

    // Add clauses to the solver
    vec<Lit> clause1;
    clause1.push(mkLit(a)); clause1.push(mkLit(b));
    solver.addClause(clause1);

    vec<Lit> clause2;
    clause2.push(~mkLit(b)); clause2.push(mkLit(c));
    solver.addClause(clause2);

    vec<Lit> clause3;
    clause3.push(~mkLit(a)); clause3.push(~mkLit(c));
    solver.addClause(clause3);

    // Solve the formula
    bool result = solver.solve();

    if (result) {
        std::cout << "Satisfying assignment found: ";
        if (solver.modelValue(a) == l_True) std::cout << "A = true ";
        else std::cout << "A = false ";
        if (solver.modelValue(b) == l_True) std::cout << "B = true ";
        else std::cout << "B = false ";
        if (solver.modelValue(c) == l_True) std::cout << "C = true ";
        else std::cout << "C = false ";
        std::cout << std::endl;
    }
    else {
        std::cout << "Formula is unsatisfiable." << std::endl;
    }

    return 0;
}
