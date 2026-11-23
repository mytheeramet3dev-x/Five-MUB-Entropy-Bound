"""Exact Pauli action certificate for the five MUBs.

Each record stores a target basis and the monomial action's column mapping.
Indices are zero-based. Phase factors are serialized as exact SymPy strings.

Run: python verify_basis_action.py
Output: pauli_basis_action_certificate.json
"""
import json
from pathlib import Path
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
        data.append({"column": c, "row": r, "phase_exact": str(phase)})
    return data

def main():
    records = []
    for label, U in pauli_operators():
        assert sp.simplify(U.conjugate().T * U - sp.eye(4)) == sp.zeros(4)
        for j, Bj in enumerate(BASES):
            matches = []
            for k, Bk in enumerate(BASES):
                R = sp.simplify(Bk.conjugate().T * U * Bj)
                if is_monomial_unitary(R):
                    matches.append((k, monomial_data(R)))
            assert len(matches) == 1, (
                f"Pauli {label}, input B_{j}: target count={len(matches)}"
            )
            k, columns = matches[0]
            record = {
                "pauli_label": label,
                "input_basis": j,
                "target_basis": k,
                "column_action": columns,
            }
            records.append(record)
            print(f"{label}: B_{j}->B_{k}")
    assert len(records) == 80
    certificate = {
        "description": "Exact Pauli action on the five fixed MUB matrices",
        "index_convention": "zero-based basis, row, and column indices",
        "phase_convention": "exact SymPy expression for each nonzero matrix entry",
        "checked_records": len(records),
        "records": records,
    }
    output = Path("pauli_basis_action_certificate.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    print(f"RESULT: {len(records)} exact actions certified.")
    print(f"CERTIFICATE FILE: {output}")

if __name__ == "__main__":
    main()
