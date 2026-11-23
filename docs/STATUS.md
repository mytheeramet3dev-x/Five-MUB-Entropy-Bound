# Research Status and Roadmap

Last updated: 2026-11-23

## Target theorem

For a complete set of five pairwise mutually unbiased orthonormal bases in \(\mathbb C^4\),
\[
F(\psi):=\sum_{j=0}^4H(B_j)_\psi\ge 7.
\]

The value 7 and equality examples were reported by Riccardi, Macchiavello, and Maccone (2017). Their treatment uses numerical optimization for the relevant multi-MUB bounds; this project seeks a rigorous global proof and studies equality structure. Do not describe the problem as formally open without a current, authoritative literature review.

## Current status snapshot

| Component | Status | Notes |
|---|---|---|
| Target statement and conventions | PROVED / DEFINED | Formal statement recorded in this repository |
| Literature baseline | PARTIALLY AUDITED | Main 2017 source identified; full citation list in REFERENCES |
| Explicit five-basis convention | EXACTLY VERIFIED (reported) | Exact unitarity and pairwise MUB checks were performed in SymPy in prior work; scripts/output are not yet committed |
| Equality example | EXACTLY VERIFIED (reported) | The representative below gives entropy sum 7 for the stated matrices |
| Pauli orbit of the representative | EXACTLY VERIFIED (reported) | Four rays found; reproducible script still required |
| Complete equality classification | UNRESOLVED | Four known orbit rays are not asserted to be all minimizers |
| Collision-entropy lower bound | PROVED | Gives 5 log2(5/2), weaker than 7 |
| Third-moment strengthening | CONJECTURED / UNRESOLVED | No universal proof recorded |
| Local minimum certificate | UNRESOLVED | Earlier derivative calculations need fresh exact verification |
| Global analytical proof | NOT ESTABLISHED | No proof yet |
| Global certified computational proof | NOT ESTABLISHED | No completed interval/branch-and-bound certificate |
| Independent verification package | NOT ESTABLISHED | Must be created after proof artifacts exist |
| Source-data audit script | ARTIFACT WRITTEN; NOT EXECUTED | Strengthened: MUB unitarity, 10 overlaps, Pauli HS orthogonality/trace/unitarity/labels, equality distributions |
| Pauli basis-action generator and checker | ARTIFACTS WRITTEN; NOT EXECUTED | Generator and independent record checker committed; both share `mub_data.py`; no certificate output yet |
| Conditional entropy symmetry theorem | PROVED (conditional) | If exact monomial basis action (PS) holds, \(F(U\psi)=F(\psi)\); concrete Pauli application still unverified |


## Priority order

1. **Freeze conventions and add executable exact matrix checks.** Commit exact matrices, verify unitarity and all ten pairwise MUB conditions, and record software versions and outputs.
2. **Re-derive the equality-state local analysis.** Start from the matrices in MATHEMATICAL-FOUNDATIONS.md. Derive zero-outcome amplitudes and the smooth positive-outcome variation independently. Do not rely on earlier unverified derivative tables.
3. **Complete the symmetry certificate.** Verify the Pauli action on the five commuting classes and, separately, the induced basis/column permutations and phases. A class permutation alone is not a complete basis-action certificate.
4. **Develop a global proof.** Any interval method must cover all of projective state space, use rigorous outward rounding, handle entropy at zero, and terminate with a complete certificate or report unresolved boxes.
5. **Independent verification.** A separate checker should validate the proof artifacts without trusting the search/derivation code.
6. **Equality classification.** Only after the universal inequality is established, prove whether the four known rays exhaust the equality set.

## Important distinction

Proving \(F(\psi)\ge7\) for all states does not prove that the four known rays are the only equality states. These are separate theorem obligations.

## Completion criteria

The project is not complete until:
- the universal lower bound is proved or rigorously certified;
- every assumption and convention is explicit;
- all computational certificates are independently checkable;
- no unverified numerical claim is presented as exact;
- equality classification is either proved or explicitly left open.

## 2026-11-23 — Finite-group domain coverage clarification

Conditional on exact verification of a finite symmetry group \(G\), a fundamental-domain coverage argument exists abstractly: canonicalize each ray's global phase, order its real coordinates lexicographically, and choose the lexicographically minimal member of each finite orbit. Every orbit has a minimum, so the domain covers projective space modulo \(G\). This is only an abstract coverage theorem; it is not a useful explicit domain or a computational reduction yet. The Pauli action certificate remains unexecuted, and the global inequality remains unproved.


## 2026-11-23 — Finite-group domain coverage clarification

Conditional on exact verification of a finite symmetry group \(G\), an abstract coverage argument is available: canonicalize ray phase, order its six real coordinates lexicographically, and select the lexicographically minimal member of each finite orbit. Every orbit has a minimum, so the domain covers projective space modulo \(G\). This is only an abstract coverage theorem, not an explicit convenient domain or computational reduction. The Pauli action certificate remains unexecuted; the global inequality remains unproved.


## Symmetry reduction scale

Even if the full two-qubit Pauli action is certified, the group modulo global phase has only 16 elements. The generic ray orbit has size 16 (trivial stabilizer), so the discrete search reduction is at most a factor of 16; it does not reduce the six real dimensions of projective state space. Symmetry is a useful discrete redundancy control, not a standalone global proof strategy.
