"""Independent checker for pauli_basis_action_certificate.json.

Recomputes each overlap matrix from the source MUB/Pauli data and checks
that the JSON's target basis, column permutation, and exact phases match.
Run after verify_basis_action.py.
"""
import json
from pathlib import Path
import sympy as sp
from mub_data import BASES, pauli_operators

def main():
    path = Path("pauli_basis_action_certificate.json")
    cert = json.loads(path.read_text(encoding="utf-8"))
    paulis = dict(pauli_operators())
    assert len(paulis) == 16
    assert cert["checked_records"] == 80
    assert len(cert["records"]) == 80
    seen = set()
    checked = 0
    for rec in cert["records"]:
        label, j, k = rec["pauli_label"], rec["input_basis"], rec["target_basis"]
        key = (label, j)
        assert key not in seen, f"duplicate record: {key}"
        seen.add(key)
        U, Bj, Bk = paulis[label], BASES[j], BASES[k]
        assert 0 <= j < 5 and 0 <= k < 5
        # Reconfirm the target uniqueness condition independently.
        matching_targets = []
        for target, candidate_basis in enumerate(BASES):
            candidate = sp.simplify(candidate_basis.conjugate().T * U * Bj)
            if (all(sum(sp.simplify(candidate[r, c]) != 0 for c in range(4)) == 1 for r in range(4))
                    and all(sum(sp.simplify(candidate[r, c]) != 0 for r in range(4)) == 1 for c in range(4))
                    and sp.simplify(candidate.conjugate().T * candidate - sp.eye(4)) == sp.zeros(4)):
                matching_targets.append(target)
        assert matching_targets == [k], f"target mismatch or non-unique target for {label}, B{j}: {matching_targets}"
        R = sp.simplify(Bk.conjugate().T * U * Bj)
        assert R.rows == 4 and R.cols == 4
        assert sp.simplify(R.conjugate().T * R - sp.eye(4)) == sp.zeros(4)
        entries = rec["column_action"]
        assert len(entries) == 4
        used_rows = set()
        for expected_col, item in enumerate(entries):
            col = item["column"]
            row = item["row"]
            assert col == expected_col
            assert row not in used_rows
            used_rows.add(row)
            actual = sp.simplify(R[row, col])
            assert actual != 0
            assert sp.simplify(actual * sp.conjugate(actual) - 1) == 0
            recorded = sp.sympify(item["phase_exact"])
            assert sp.simplify(actual - recorded) == 0, (
                f"phase mismatch {label}, B{j}->B{k}, col {col}"
            )
            assert sum(sp.simplify(R[r, col]) != 0 for r in range(4)) == 1
        assert len(used_rows) == 4
        assert all(sum(sp.simplify(R[r, c]) != 0 for c in range(4)) == 1
                   for r in range(4))
        checked += 1
    assert len(seen) == 16 * 5
    assert seen == {(label, j) for label in paulis for j in range(5)}
    print(f"INDEPENDENT CHECK PASSED: {checked} records, all exact phases and permutations matched.")

if __name__ == "__main__":
    main()
