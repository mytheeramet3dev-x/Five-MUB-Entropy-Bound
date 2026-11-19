# Five-MUB Entropy Bound

**Full research title:** *The Global Shannon-Entropy Problem for Complete Sets of Five Mutually Unbiased Bases in Dimension Four*

Research project on the tight Shannon entropic uncertainty relation for a complete set of five mutually unbiased bases (MUBs) in dimension four.

> **Research status: IN PROGRESS.** The target inequality and equality examples are known in the literature. This repository investigates a rigorous global proof and the equality structure. It does **not** currently claim that a new global proof or a complete equality classification has been established.

## Target

For five orthonormal bases \\(B_0,\\ldots,B_4\\) in \\(\\mathbb C^4\\) that are pairwise mutually unbiased, let
\\[
p_{j,a}=|\\langle b_{j,a}|\\psi\\rangle|^2,\\qquad
H(B_j)_\\psi=-\\sum_{a=0}^3p_{j,a}\\log_2p_{j,a}.
\\]
The target is
\\[
\\boxed{\\sum_{j=0}^4H(B_j)_\\psi\\ge 7\\text{ bits}.}
\\]
The inequality is to be proved for every unit vector \\(\\psi\\in\\mathbb C^4\\). Equality examples are known.

## Repository map

- [Research status and roadmap](docs/STATUS.md)
- [Mathematical foundations](docs/MATHEMATICAL-FOUNDATIONS.md)
- [Verification ledger and caveats](docs/VERIFICATION.md)
- [Research log](docs/RESEARCH-LOG.md)
- [Detailed work archive and continuation record](docs/WORK-ARCHIVE.md)
- [References](REFERENCES.md)

## Exact verification package

- [Verification instructions and evidence status](VERIFICATION-RESULTS.md)
- [Exact MUB and Pauli data](mub_data.py)
- [MUB unitarity and mutual-unbiasedness checks](verify_mub.py)
- [Equality-state checks](verify_equality.py)
- [Pauli state-orbit checks](verify_pauli_orbit.py)
- [Python dependencies](requirements.txt)

Run the commands in VERIFICATION-RESULTS.md from the repository root. The
scripts are committed, but their execution logs have not yet been captured.
The state-orbit script is not a full basis-action certificate.

## Proof-status policy

Every result must be labeled as one of:
- **PROVED** — a complete mathematical derivation is present.
- **EXACTLY VERIFIED** — finite symbolic/algebraic computation with reproducible details.
- **NUMERICALLY OBSERVED** — numerical evidence only; not an exact proof.
- **CONJECTURED** — plausible but unproved.
- **UNRESOLVED** — an explicit open obligation.
- **WITHDRAWN** — an earlier claim found unsupported or incorrect.

Do not promote numerical evidence to proof. Do not report a computation as executed unless its code, output, and exact scope are recorded. Preserve failed approaches and corrections.

## Scope

Primary objective: establish the universal 7-bit lower bound with a rigorous global argument. Secondary objective: classify all equality states, if possible. The equality-classification objective is strictly stronger and must not be conflated with proving the inequality.

## Reproducibility

All matrices, conventions, scripts, exact outputs, software versions, and proof artifacts should eventually be committed. At present, some matrix and equality-state checks are recorded as completed in the research notes, but the corresponding executable verification artifacts still need to be added.
