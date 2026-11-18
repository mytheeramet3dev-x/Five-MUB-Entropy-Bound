# Research Log

## Project origin and scope

The project studies the tight Shannon entropic uncertainty relation for a complete set of five MUBs in \(\mathbb C^4\):
\[
\sum_{j=0}^4H(B_j)_\psi\ge7.
\]
The 7-bit value and equality examples were already reported in the literature. The research goal is a rigorous global proof and, separately, a complete understanding of equality states.

## Main mathematical routes explored

### 1. Collision-entropy route

The complete-MUB identity \(\sum_jC_j=2\) gives the valid lower bound
\[
F\ge5\log_2(5/2)\approx6.60964.
\]
It falls short of 7. A probability-only construction shows that the collision identity by itself cannot bridge the gap.

### 2. Moment route

Higher moments \(M_k=\sum_{j,a}p_{j,a}^k\) were investigated. At the known equality example:
\[
(M_2,M_3,M_4,M_5)
=(2,7/8,13/32,25/128).
\]
The conjecture \(M_3\ge7/8\) is not proved. Rényi-3 bounds alone have not yielded the Shannon target.

### 3. Pure-state reconstruction route

Complete MUB probabilities reconstruct the density matrix:
\[
\rho=I_4/4+\sum_{j,a}(p_{j,a}-1/4)P_{j,a}.
\]
For pure states, \(\rho^2=\rho\), equivalently
\[
X^2=X/2+3I_4/16,\qquad X=\rho-I_4/4.
\]
This gives algebraic feasibility constraints for probability tables. A useful future direction is to combine these constraints with entropy lower bounds without relaxing away the quantum compatibility conditions.

### 4. Entropy-gap / KL route

For \(r_a=p_a^2/C(p)\),
\[
H(p)+\log_2C(p)=D_{\rm KL}(p\|r)\ge0.
\]
The target is equivalent to a quantitative lower bound on the sum of these five KL gaps when the product of collision terms is too large. Pinsker gives a generic but currently insufficient estimate. The missing ingredient is a strong joint quantum constraint across the five bases.

### 5. Local analysis near equality

The equality representative has zero probabilities in three bases. Entropy is therefore nonsmooth in ordinary coordinates at that point. A valid local proof must:
- parameterize tangent directions in projective space;
- derive every zero-outcome amplitude exactly;
- prove individual probability upper bounds for those outcomes;
- bound the smooth contribution from positive outcomes;
- verify all first-order cancellations exactly;
- control all remainders with explicit constants.

An earlier proposed lower bound \(Z\log_2(6/Z)\) for six zero probabilities was wrong: it is an upper bound, not a lower bound. Any local certificate using it is withdrawn. A valid alternative is \(H_{zero}\ge Z\log_2(1/s)\) if each zero probability is individually bounded above by \(s\).

### 6. Symmetry route

The two-qubit Pauli group modulo phase has 16 elements and acts on the five commuting Pauli classes. The equality representative has a reported orbit of four rays and stabilizer size four. To certify symmetry for the concrete matrices, produce the exact induced class permutation and the monomial basis-change matrices (basis permutation, column permutation, and phases).

### 7. Global certified computation route

A possible route is a projective-coordinate covering. Choose a largest coordinate of \(\psi\), fix its phase, and represent the ray in one of four charts with the other three complex coordinate ratios of modulus at most one. This covers projective state space, with overlaps.

An interval verifier would need:
- rigorous interval evaluation of all probabilities;
- outward-rounded entropy bounds, including intervals touching zero;
- exhaustive subdivision and a termination certificate;
- treatment of chart overlaps and equality neighborhoods;
- a machine-readable proof log and independent checker.

This is a design proposal only. No global interval proof has been run.

## Current next actions

1. Add exact symbolic matrix verification scripts.
2. Re-derive the local zero-amplitude formulas from scratch.
3. Build the Pauli symmetry action table for the actual displayed matrices.
4. Decide between an analytic global inequality, a sum-of-squares/algebraic certificate, or a rigorous interval proof.
5. Keep a separate issue list for all unresolved lemmas.
6. Do not claim completion until an independently checkable global proof exists.