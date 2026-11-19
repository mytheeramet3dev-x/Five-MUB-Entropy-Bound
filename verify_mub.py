"""Exact checks for the five displayed bases. Run: python verify_mub.py"""
import sympy as sp
from mub_data import BASES

def main():
    identity = sp.eye(4)
    for j, basis in enumerate(BASES):
        assert sp.simplify(basis.conjugate().T*basis-identity) == sp.zeros(4), f"B_{j} not unitary"
        print(f"PASS: B_{j}^* B_{j} = I")
    pairs = 0
    for j in range(5):
        for k in range(j+1,5):
            overlap = sp.simplify(BASES[j].conjugate().T*BASES[k])
            for entry in overlap:
                value = sp.simplify(sp.expand_complex(entry*sp.conjugate(entry)))
                assert value == sp.Rational(1,4), f"B_{j}, B_{k}: |overlap|^2={value}"
            pairs += 1
            print(f"PASS: B_{j}, B_{k} mutually unbiased")
    assert pairs == 10
    print("RESULT: all five bases are unitary and all ten pairs are mutually unbiased.")

if __name__ == "__main__":
    main()
