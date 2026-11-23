# Source-data audit checkpoint

## Scope
`audit_mub_source.py` independently repeats the exact algebraic checks for the
five basis matrices and audits the Pauli label convention used by
`pauli_operators()`. It compares the yielded operators against an explicit
construction using tensor products of \\(X^x Z^z\\), checks exact Hilbert–Schmidt orthogonality and normalization of the Pauli representatives (stronger than distinctness modulo phase), and confirms the equality-state probabilities.

## Check list
- Five 4x4 basis matrices are unitary.
- All ten distinct basis pairs are mutually unbiased (every squared overlap is 1/4).
- All 16 Pauli labels are present and correspond to the declared
  \\(X^xZ^z\\) convention.
- Pauli representatives are distinct modulo global phase.
- The equality representative is normalized and its five probability
  distributions match the recorded table exactly.

## Evidence status
**SCRIPT WRITTEN; NOT EXECUTED.** This artifact is intended to make the audit
reproducible. It has not produced a pass log in the current environment.
The source matrices and audit code are fetched back from GitHub after commit.
A successful future run must preserve output, Python version, and SymPy version.

## Strengthening checkpoint — Pauli orthogonality

The audit now checks the exact Hilbert–Schmidt relations \(\operatorname{Tr}(P_a^\dagger P_b)=4\delta_{ab}\), exact unitarity, trace zero for every nonidentity label, and label uniqueness. This catches duplicate or malformed representatives directly. Checks are written but not executed. Expected and production constructions share the X/Z primitives; this is not an external source derivation.
