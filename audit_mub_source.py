"""Independent source audit for the fixed five-MUB matrices and Pauli labels.

This script repeats core checks and adds explicit checks that the Pauli labels
enumerate 16 distinct matrices modulo phase and that the generator convention
is X^x Z^z (not Z^z X^x). It is a reproducible audit, not an execution
claim until run.
"""
import sympy as sp
from mub_data import BASES, PSI_STAR, exact_probabilities, pauli_operators

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
EXPECTED_PROBS = (
    (sp.Rational(1, 2), sp.Rational(1, 2), 0, 0),
    (sp.Rational(1, 2), 0, sp.Rational(1, 2), 0),
    (sp.Rational(1, 4),) * 4,
    (sp.Rational(1, 2), sp.Rational(1, 2), 0, 0),
    (sp.Rational(1, 4),) * 4,
)

def main():
    I4 = sp.eye(4)
    assert len(BASES) == 5
    for j, B in enumerate(BASES):
        assert B.shape == (4, 4)
        assert sp.simplify(B.conjugate().T * B - I4) == sp.zeros(4)
    pair_count = 0
    for j in range(5):
        for k in range(j + 1, 5):
            C = sp.simplify(BASES[j].conjugate().T * BASES[k])
            assert all(sp.simplify(sp.expand_complex(c * sp.conjugate(c))) == sp.Rational(1, 4)
                       for c in C)
            pair_count += 1
    assert pair_count == 10

    expected_paulis = {}
    for x1, z1, x2, z2 in ((a, b, c, d) for a in (0, 1)
                              for b in (0, 1) for c in (0, 1) for d in (0, 1)):
        A = (X if x1 else I2) * (Z if z1 else I2)
        C = (X if x2 else I2) * (Z if z2 else I2)
        expected_paulis[f"{x1}{z1}{x2}{z2}"] = sp.kronecker_product(A, C)
    yielded = dict(pauli_operators())
    assert set(yielded) == set(expected_paulis)
    for label, matrix in expected_paulis.items():
        assert sp.simplify(yielded[label] - matrix) == sp.zeros(4)
        assert sp.simplify(matrix.conjugate().T * matrix - I4) == sp.zeros(4)
    # Distinctness is checked exactly up to global phase.
    matrices = list(yielded.values())
    for a in range(16):
        for b in range(a + 1, 16):
            overlap = sp.simplify(matrices[a].conjugate().T * matrices[b])
            assert overlap != I4 and overlap != -I4 and overlap != sp.I * I4 and overlap != -sp.I * I4

    assert sp.simplify(PSI_STAR.conjugate().T * PSI_STAR)[0] == 1
    for j, B in enumerate(BASES):
        p = exact_probabilities(PSI_STAR, B)
        assert p == EXPECTED_PROBS[j], f"equality-state probabilities mismatch for B{j}: {p}"
        assert sum(p) == 1

    print("SOURCE AUDIT PASS: five unitary bases, 10 MUB pairs, 16 Pauli labels,")
    print("Pauli convention X^x Z^z, and equality-state probability table all checked.")

if __name__ == "__main__":
    main()
