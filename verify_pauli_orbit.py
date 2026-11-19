"""Exact state-orbit check. Does not certify the full basis action.
Run: python verify_pauli_orbit.py
"""
import sympy as sp
from mub_data import BASES, PSI_STAR, exact_probabilities, shannon_entropy_bits, pauli_operators

def ray_projector(state):
    return sp.simplify(state*state.conjugate().T)

def main():
    representatives = {}
    labels_by_ray = {}
    for label,operator in pauli_operators():
        state = sp.simplify(operator*PSI_STAR)
        key = sp.srepr(ray_projector(state))
        labels_by_ray.setdefault(key,[]).append(label)
        representatives.setdefault(key,state)
    assert len(labels_by_ray) == 4, f"Expected 4 rays, got {len(labels_by_ray)}"
    assert sum(len(v) for v in labels_by_ray.values()) == 16
    for index,(key,labels) in enumerate(sorted(labels_by_ray.items()),start=1):
        state = representatives[key]
        assert sp.simplify((state.conjugate().T*state)[0]) == 1
        total = sp.simplify(sum(
            shannon_entropy_bits(exact_probabilities(state,basis)) for basis in BASES
        ))
        assert total == 7, f"ray {index} entropy sum={total}"
        print(f"PASS: ray {index}; Pauli labels={labels}; entropy sum={total} bits")
    assert all(len(v)==4 for v in labels_by_ray.values())
    print("RESULT: 16 Pauli operators give 4 distinct rays; each has entropy 7.")
    print("NOTE: state orbit only; full basis/column/phase action is not checked.")

if __name__ == "__main__":
    main()
