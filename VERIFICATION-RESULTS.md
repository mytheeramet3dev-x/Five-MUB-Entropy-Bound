# Exact Verification Package

## Environment and commands

Python 3.10 or newer is recommended. The only third-party dependency is SymPy.
From the repository root:

    python -m pip install -r requirements.txt
    python verify_mub.py
    python verify_equality.py
    python verify_pauli_orbit.py

All assertions use exact symbolic expressions, not floating-point tolerances.

## Scripts

- mub_data.py: fixed five-basis matrices, equality representative, exact probability and entropy helpers, and two-qubit Pauli operators.
- verify_mub.py: checks unitarity of all five matrices and mutual unbiasedness of all ten distinct pairs.
- verify_equality.py: checks normalization, five exact probability distributions, individual entropies, and total 7 bits.
- verify_pauli_orbit.py: checks that the 16 two-qubit Pauli operators produce four distinct rays and that each ray has entropy sum 7.

## Evidence status

The scripts are committed as reproducibility artifacts. Their execution outputs
have NOT yet been captured in this document. Do not interpret the existence of
the scripts as evidence that they have been executed in the current environment.
After running them, append complete terminal outputs, Python and SymPy versions,
and the commit hash used.

The Pauli script checks only the state orbit. It does not verify the full
matrix-level action on the five bases (basis permutation, column permutation,
and phases).

These checks do not prove the universal inequality
sum_j H(B_j)_psi >= 7 for every pure state. A global proof remains unresolved.
