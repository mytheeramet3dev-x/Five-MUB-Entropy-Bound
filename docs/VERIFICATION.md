# Verification Ledger and Claim Audit

Last updated: 2026-11-19

This file is deliberately conservative. It records what is known, what was reported in prior exploratory work, and what must not be treated as established.

## A. Results supported by mathematical derivation

### A1. Collision lower bound

For a complete set of five MUBs in dimension four and a pure state,
\[
\sum_jC_j=2.
\]
Using \(H(p)\ge-\log_2C(p)\) and AM-GM gives
\[
F\ge5\log_2(5/2)\approx6.60964.
\]
This does not prove 7.

### A2. A probability-only obstruction to a naive moment argument

Three ternary-uniform probability vectors and two binary-uniform vectors have total collision sum 2, but entropy sum
\[
3\log_2 3+2\approx6.75489<7.
\]
This is **not** a quantum counterexample: it only shows that the collision identity alone does not force the desired Shannon bound.

### A3. Failed affine entropy ansatz

An attempted pointwise lower bound
\[
H(p)\ge\alpha+\beta C(p)+\gamma T(p),
\quad T(p)=\sum_ap_a^3,
\]
with equality imposed at the uniform and binary-uniform distributions leads to
\[
\alpha=3+\gamma/8,\qquad
\beta=-4-3\gamma/4.
\]
Testing the ternary-uniform distribution requires
\[
\gamma\ge72(5/3-\log_2 3)\approx5.8827,
\]
whereas testing a deterministic distribution requires \(\gamma\le8/3\). Thus this particular affine-in-\(C,T\) pointwise ansatz cannot work. This is not a disproof of the quantum theorem.

## B. Exact checks reported in prior computation; scripts still required

The following were reported as exact SymPy checks in prior work:
- all five displayed matrices are unitary;
- all ten pairs are mutually unbiased;
- the equality-state probability vectors in MATHEMATICAL-FOUNDATIONS.md;
- the four-ray Pauli orbit of the displayed equality representative;
- entropy sum 7 for those four rays.

Because the executable notebook/script and raw logs are not yet stored here, these are recorded as **reported exact checks**, not as a self-contained reproducibility artifact. Re-run and commit the code before relying on this repository as independent verification.

## C. Numerical evidence only

A numerical scan was reported for 23,040 artificial combinations of three ternary-uniform and two binary-uniform probability patterns, reconstructed into candidate density matrices. The reported floating-point scan found a negative 2x2 principal minor for every pattern, with the largest minimum minor approximately \(-5/144\).

This is **numerical evidence only**, not an exact exhaustive certificate. The attempted exact symbolic scan timed out. No exact integer-arithmetic proof of this exclusion is currently included. Do not state that all 23,040 cases have been exactly ruled out.

## D. Unproved conjectures / open obligations

- \(M_3\ge7/8\) for all pure states.
- Any implication from a third-moment bound to the required Shannon sum.
- A local-minimum certificate at the equality representative.
- Exact cancellation of first-order terms in the smooth positive-outcome entropy contribution.
- A complete Pauli basis/column action table for the displayed matrices.
- A rigorous global interval or algebraic certificate proving \(F\ge7\).
- Complete equality classification.

## E. Withdrawn or invalid earlier claims

1. **False zero-outcome entropy bound.** For six nonnegative zero-outcome probabilities with total mass \(Z\), the expression \(Z\log_2(6/Z)\) is an upper bound attained by the uniform distribution, not a lower bound. It cannot be used to prove local minimality.
2. **Local radius and constants based on that bound.** Previously quoted very small radii and Hessian constants relied on the invalid inequality and are withdrawn.
3. **Unverified representation dimensions, Gram dimensions, ranks, and polynomial coefficient counts.** Earlier exploratory messages included claims about dimensions such as 112, 196, orbit ranks, and polynomial coefficient counts without a reproducible computation. They are not accepted as results in this repository.
4. **Unverified exact pattern scan.** Any prior claim that the 23,040-pattern scan was completed exactly is withdrawn. Only the floating-point scan described in section C is supported by the available record.
5. **Unverified derivative tables.** Several versions of zero-amplitude derivative formulas were stated during exploration. They conflict in form and have not been independently re-derived from the explicit matrices. Do not use them as a certificate.

## F. Correct local entropy observation

If six zero-outcome probabilities \(q_i\) satisfy \(0\le q_i\le s\) and \(Z=\sum_iq_i\), then
\[
-\sum_iq_i\log_2q_i
\ge Z\log_2(1/s)
\]
for \(0<s<1\), because each nonzero \(q_i\le s\) implies \(-\log_2q_i\ge\log_2(1/s)\). This is a valid lower bound, provided the individual upper bounds \(q_i\le s\) are proved from the chosen parameterization. It does not by itself complete the local proof.

## G. Required reproducibility record

Every future computational claim must include:
- source script or notebook;
- exact matrix and basis conventions;
- software and version;
- command to reproduce;
- complete output or a cryptographic hash plus machine-readable artifact;
- whether arithmetic is exact, interval-certified, or floating point;
- precise scope of the check;
- independent checker where feasible.