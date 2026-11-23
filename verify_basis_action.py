"""Exact certificate for the Pauli action on the five MUBs.

For every two-qubit Pauli U and input basis B_j, finds a target basis B_k
such that R = B_k^* U B_j is monomial unitary, then records the column
permutation and phases. This is stronger than checking one state's orbit.

Run: python verify_basis_action.py
"""
import sympy as sp
from mub_data import BASES, pauli_operators

def is_monomial_unitary(M):
    n = M.rows
    for r in range(n):
        if sum(sp.simplify(M[r, c]) != 0 for c in range(n)) != 1:
            return False
    for c in range(n):
        if sum(sp.simplify(M[r, c]) != 0 for r in range(n)) != 1:
            return False
    return sp.simplify(M.conjugate().T * M - sp.eye(n)) == sp.zeros(n)

def monomial_data(M):
    data = []
    for c in range(M.cols):
        rows = [r for r in range(M.rows) if sp.simplify(M[r, c]) != 0]
        assert len(rows) == 1
        r = rows[0]
        phase = sp.simplify(M[r, c])
        assert sp.simplify(phase * sp.conjugate(phase)) == 1
        data.append((r, phase))
    return tuple(data)

def main():
    total = 0
    for label, U in pauli_operators():
        for j, Bj in enumerate(BASES):
            matches = []
            for k, Bk in enumerate(BASES):
                R = sp.simplify(Bk.conjugate().T * U * Bj)
                if is_monomial_unitary(R):
                    matches.append((k, monomial_data(R)))
            assert len(matches) == 1, (
                f"Pauli {label}, input B_{j}: target count={len(matches)}"
            )
            k, data = matches[0]
            print(f"{label}: B_{j}->B_{k}; columns (row,phase)={data}")
            total += 1
    assert total == 80
    print("RESULT: 80 exact Pauli/basis actions certified as monomial.")
if __name__ == "__main__":
    main()
