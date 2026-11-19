"""Exact verification of the recorded equality representative.
Run: python verify_equality.py
"""
import sympy as sp
from mub_data import BASES, PSI_STAR, exact_probabilities, shannon_entropy_bits

EXPECTED = (
    (sp.Rational(1,2),sp.Rational(1,2),0,0),
    (sp.Rational(1,2),0,sp.Rational(1,2),0),
    (sp.Rational(1,4),)*4,
    (sp.Rational(1,2),sp.Rational(1,2),0,0),
    (sp.Rational(1,4),)*4,
)
EXPECTED_ENTROPIES = (sp.Integer(1),sp.Integer(1),sp.Integer(2),sp.Integer(1),sp.Integer(2))

def main():
    assert sp.simplify((PSI_STAR.conjugate().T*PSI_STAR)[0]) == 1
    print("PASS: equality representative is normalized")
    entropies = []
    for j,basis in enumerate(BASES):
        probabilities = exact_probabilities(PSI_STAR,basis)
        assert probabilities == EXPECTED[j], f"B_{j}: got {probabilities}"
        assert sum(probabilities) == 1
        entropy = shannon_entropy_bits(probabilities)
        assert entropy == EXPECTED_ENTROPIES[j], f"B_{j}: entropy {entropy}"
        entropies.append(entropy)
        print(f"PASS: B_{j} probabilities={probabilities}; entropy={entropy}")
    total = sp.simplify(sum(entropies))
    assert total == 7
    print("RESULT: exact entropy sum for PSI_STAR is 7 bits.")

if __name__ == "__main__":
    main()
