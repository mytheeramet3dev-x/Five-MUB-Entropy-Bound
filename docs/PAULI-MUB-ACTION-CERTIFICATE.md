# Pauli–MUB Action Certificate: Reproducibility Notes

## Scope

The generator `verify_basis_action.py` attempts to certify all 80 actions of
the 16 two-qubit Pauli representatives on the five basis matrices in
`mub_data.py`.

For a Pauli representative \\(U\\) and input basis matrix \\(B_j\\), it
searches for exactly one \\(B_k\\) such that

\\[
R=B_k^\\dagger U B_j
\\]

is monomial unitary. A successful record gives the target basis and, for each
input column, its unique output row and exact phase.

## Output schema

Running the script is intended to write `pauli_basis_action_certificate.json`.
The JSON contains 80 records, each with:
- `pauli_label`: the four-bit label used by the generator;
- `input_basis`: zero-based index \\(j\\);
- `target_basis`: zero-based index \\(k\\);
- `column_action`: four entries, each containing zero-based input column,
  output row, and exact phase expression as a string.

## Verification logic

The generator checks:
1. every Pauli matrix is unitary;
2. each candidate overlap matrix has exactly one nonzero entry per row and column;
3. the overlap matrix is unitary;
4. every nonzero entry has unit modulus;
5. exactly one target basis matches for each Pauli/input pair;
6. exactly 80 records are generated.

## Current evidence status

**SCRIPT WRITTEN; NOT EXECUTED IN THIS environment.** No JSON output file,
80-record pass claim, or successful symmetry result is asserted yet.
After running, preserve the generated JSON, command output, Python version,
and SymPy version together. A generated certificate should be independently
rechecked rather than accepted solely because the generator produced it.

## Reproduction

From the repository root:

```bash
python -m pip install -r requirements.txt
python verify_basis_action.py
```

The output JSON is generated in the current working directory.
