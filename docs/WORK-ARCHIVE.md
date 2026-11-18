# Detailed Work Archive and Continuation Record

Last updated: 2026-11-19

This file preserves detailed prior research so future sessions do not restart completed reasoning. It is a research-memory record, not a substitute for source code or a formal proof. Labels distinguish derivations, reported computations, numerical observations, and unresolved items.

## 1. Fixed research target

Project short name: Five-MUB Entropy Bound.

\[
F(\psi)=\sum_{j=0}^4 H(B_j)_\psi\ge7,
\qquad
H(B_j)_\psi=-\sum_{a=0}^3p_{j,a}\log_2p_{j,a},
\]
for a complete set of five MUBs in dimension four.

Riccardi–Macchiavello–Maccone (2017), PRA 95, 032109, arXiv:1701.04304, reports the value 7 and equality examples; the relevant optimization is numerical. The possible contribution being investigated is a rigorous global proof and possibly complete minimizer classification. Do not claim the problem is formally open without authoritative evidence.

## 2. Literature and baseline bounds already investigated

### 2.1 Riccardi et al. (2017)
- Equation (51) reports the d=4, L=5 value 7.
- Equation (52) gives equality examples.
- Their MUB uncertainty bounds are derived through numerical optimization (Mathematica NMinimize), not a global analytic proof for this case.
- Explicit MUB matrices appear in their Eq. (46).
- arXiv: https://arxiv.org/abs/1701.04304
- DOI: 10.1103/PhysRevA.95.032109

### 2.2 Standard lower bounds

Ivanovic complete-MUB bound:
\[
q_I=(d+1)[\log_2(d+1)-1].
\]
At d=4:
\[
5\log_2(5/2)\approx6.60964.
\]

Sánchez-Ruiz bound:
\[
q_S=\frac d2\log_2\frac d2+
\frac{d+1}{2}\log_2\frac{d+1}{2}.
\]
At d=4:
\[
2+\frac52\log_2(5/2)\approx5.3048875.
\]
A prior value 6.75489 for this expression was wrong and was corrected.

### 2.3 Collision identity

For complete MUBs:
\[
\sum_{j=0}^4 C_j=1+\operatorname{Tr}(\rho^2),
\qquad C_j=\sum_a p_{j,a}^2.
\]
For pure states, \(\sum_jC_j=2\). The Shannon/collision entropy comparison and AM-GM yield the 6.60964 bound, not 7.

A probability-only illustration shows why the collision identity alone is insufficient: three ternary-uniform distributions and two binary-uniform distributions have total collision sum 2 but entropy sum
\[
3\log_2 3+2\approx6.75489<7.
\]
This is not a quantum counterexample.

## 3. Explicit MUB convention and equality state

The matrices are recorded in MATHEMATICAL-FOUNDATIONS.md. The following checks were actually performed in exact SymPy arithmetic in a prior session:
- all five matrices are unitary;
- all ten distinct pairs are mutually unbiased;
- for \(\psi_*=(1,1,0,0)^T/\sqrt2\), the five probability vectors are:
  - B0: (1/2, 1/2, 0, 0)
  - B1: (1/2, 0, 1/2, 0)
  - B2: (1/4, 1/4, 1/4, 1/4)
  - B3: (1/2, 1/2, 0, 0)
  - B4: (1/4, 1/4, 1/4, 1/4)
- entropies are 1, 1, 2, 1, 2, giving exactly 7 bits.

The Pauli orbit of this representative was also checked and has four rays:
\[
(1,1,0,0)^T/\sqrt2,\quad
(1,-1,0,0)^T/\sqrt2,\quad
(0,0,1,1)^T/\sqrt2,\quad
(0,0,1,-1)^T/\sqrt2.
\]
Each has entropy sum 7. The orbit has size 4 and stabilizer size 4 in the 16-element two-qubit Pauli group modulo phase.

Important: these computations were run, but the executable SymPy script and raw output were not saved to the repository. They must be recreated as artifacts before independent reproducibility can be claimed. Do not repeat the already established derivation from scratch unless the script is being produced to preserve it.

## 4. Pure-state and projector reconstruction route

For projectors \(P_{j,a}=|b_{j,a}\rangle\langle b_{j,a}|\):
\[
\rho=\frac{I_4}{4}+\sum_{j,a}(p_{j,a}-1/4)P_{j,a}.
\]
Set \(X=\rho-I_4/4\). For a pure state:
\[
\operatorname{Tr}X^2=3/4,
\qquad
X^2=\frac12X+\frac{3}{16}I.
\]
An earlier expression \(X^2=I/4\) was incorrect and corrected.

In SU(4) Gell-Mann coordinates with \(\operatorname{Tr}(\lambda_i\lambda_j)=2\delta_{ij}\):
\[
X=\frac12\sum_i r_i\lambda_i,
\quad
\sum_i r_i^2=\frac32,
\quad
\sum_{ij}d_{ijk}r_ir_j=r_k.
\]

Taking the trace of the pure-state quadratic identity against a projector yields 20 quadratic constraints involving triple products:
\[
\sum_{j,a,l,b}x_{j,a}x_{l,b}
\operatorname{Tr}(P_{k,c}P_{l,b}P_{j,a})
=\frac12x_{k,c}+\frac{3}{16},
\quad x_{j,a}=p_{j,a}-1/4.
\]
The triple-product coefficients have not been independently tabulated in a reproducible artifact.

A candidate probability table is physically realizable iff its reconstructed matrix is Hermitian PSD, trace one, and rank one (with the relevant normalization and complete-MUB reconstruction identities satisfied). For a PSD trace-one matrix, purity one is equivalent to rank one. Also:
\[
\sum_{r<s}(\rho_{rr}\rho_{ss}-|\rho_{rs}|^2)
=\frac{(\operatorname{Tr}\rho)^2-\operatorname{Tr}\rho^2}{2}=0.
\]
For a PSD pure state all these 2x2 principal minors vanish.

## 5. Moment and polynomial routes

Define:
\[
M_k=\sum_{j,a}p_{j,a}^k.
\]
At the known equality state:
\[
M_2=2,\quad M_3=7/8,\quad M_4=13/32,\quad M_5=25/128.
\]
Also:
\[
M_3=7/8+\sum_{j,a}(p_{j,a}-1/4)^3.
\]
The operator formulation considered was
\[
\Omega_3=\sum_{j,a}P_{j,a}^{\otimes3},
\qquad
M_3=\operatorname{Tr}(\rho^{\otimes3}\Omega_3).
\]
The conjecture \(M_3\ge7/8\) is not proved. A Rényi-3 lower bound by itself has not produced the Shannon target.

A proposed polynomial:
\[
G(z)=\sum_{j,a}q_{j,a}^3-\frac78N^3,
\quad q_{j,a}=|(B_jz)_a|^2,
\quad N=\|z\|^2,
\]
was considered as a homogeneous sextic. A scaled integer-coefficient form and its claimed monomial count were stated in earlier exploration but were not backed by a saved computation. Treat coefficient counts, SOS decompositions, and related representation dimensions as unverified until reconstructed.

For entropy:
\[
P_m(x)=\frac{x}{\ln2}\sum_{k=1}^m\frac{(1-x)^k}{k}
\le -x\log_2x,
\]
with remainder
\[
R_m(x)=\frac{x}{\ln2}\sum_{k=m+1}^{\infty}\frac{(1-x)^k}{k}
\ge\frac{x(1-x)^{m+1}}{(m+1)\ln2}.
\]
For m=3, the derived aggregate expression was:
\[
F\ge\frac1{\ln2}
\left(\frac{19}{6}+\frac32M_3-\frac13M_4+\frac14S_4\right),
\quad S_4=\sum p(1-p)^4.
\]
Using \(M_1=5,M_2=2\):
\[
S_4=-3+6M_3-4M_4+M_5,
\]
so
\[
F\ge\frac1{\ln2}
\left(\frac{29}{12}+3M_3-\frac43M_4+\frac14M_5\right).
\]
The elementary estimates used in one attempt gave only
\[
F\ge\frac{15}{4\ln2}\approx5.4101,
\]
not 6.128 or 7. The earlier stronger numerical claim was corrected.

A pointwise affine ansatz in collision and third moment was shown impossible under its imposed equality conditions:
\[
H(p)\ge\alpha+\beta C(p)+\gamma T(p).
\]
The equality constraints imply \(\alpha=3+\gamma/8\), \(\beta=-4-3\gamma/4\). Ternary-uniform test requires \(\gamma\gtrsim5.8827\), while deterministic test requires \(\gamma\le8/3\). This rules out that ansatz only.

## 6. Entropy-gap / KL route

Define:
\[
\Delta(p)=H(p)+\log_2 C(p),\quad C(p)=\sum_ap_a^2.
\]
Then:
\[
F=-\log_2\prod_jC_j+\sum_j\Delta(p_j).
\]
The target is equivalent to:
\[
\sum_j\Delta(p_j)\ge\log_2(128\prod_jC_j).
\]
For \(r_a=p_a^2/C(p)\):
\[
\Delta(p)=D_{\rm KL}(p\|r).
\]
Pinsker:
\[
\Delta(p_j)\ge\frac1{2\ln2}\|p_j-r_j\|_1^2,
\]
and hence:
\[
\sum_j\Delta(p_j)\ge\frac1{10\ln2}
\left(\sum_j\|p_j-r_j\|_1\right)^2.
\]
A sufficient condition in the difficult product regime is:
\[
\left(\sum_j\|p_j-r_j\|_1\right)^2
\ge10\ln2\log_2(128\prod_jC_j).
\]
The needed joint quantum lower bound on the five deviations has not been proved.

## 7. Local analysis at the equality state — critical corrections

Because the equality state has zero outcome probabilities, entropy is nonsmooth in ordinary coordinates. A tangent parameterization considered was:
\[
\psi(t)=\frac{\psi_*+t\eta}{\sqrt{1+t^2\|\eta\|^2}},
\quad \eta\perp\psi_*.
\]
For zero amplitudes of order t, probabilities are order t^2 and their entropy contributions contain \(-t^2\log t^2\).

Several different zero-amplitude derivative lists were stated in prior exploratory messages and were not consistently verified from the explicit matrices. Do not use any of those lists without re-deriving them directly.

**Critical invalid step:** for six nonnegative zero-outcome probabilities with total mass Z, \(Z\log_2(6/Z)\) is an upper bound (uniform distribution maximizes entropy), not a lower bound. All local certificates, radii, and constants relying on that lower bound are withdrawn.

A valid conditional observation is: if every zero probability satisfies \(q_i\le s<1\), then
\[
-\sum_iq_i\log_2q_i\ge Z\log_2(1/s),
\quad Z=\sum_iq_i.
\]
This still requires exact proof of each individual upper bound and a rigorous bound on the positive-outcome entropy variation. The previously quoted large Hessian constants and extremely small local radii are not accepted.

## 8. Symmetry route

Two-qubit Pauli commuting classes used:
\[
\mathcal C_0=\{ZI,IZ\},\quad
\mathcal C_1=\{XI,IX\},\quad
\mathcal C_2=\{YI,IY\},\quad
\mathcal C_3=\{ZX,XY\},\quad
\mathcal C_4=\{ZY,XZ\}.
\]
Pauli conjugation sends each Pauli operator to itself or its negative, so it preserves commutation and permutes maximal commuting classes. This is the structural reason the MUB set is preserved, provided the correspondence with the explicit matrices is verified.

The 16 elements modulo phase can be encoded as:
0000 II; 0001 IZ; 0010 IX; 0011 IY; 0100 ZI; 0101 ZZ; 0110 ZX; 0111 ZY; 1000 XI; 1001 XZ; 1010 XX; 1011 XY; 1100 YI; 1101 YZ; 1110 YX; 1111 YY.

The full matrix-level certificate still needs:
\[
R=B_{\pi(j)}^\dagger U B_j
\]
and exact verification that each R is monomial unitary (one nonzero entry per row/column, phases of unit modulus). The commuting-class permutation table alone is not the complete basis/column action table.

The Pauli group is isomorphic to \(\mathbb Z_2^4\) modulo global phase. Orbit sizes can only be 1,2,4,8,16. The known equality representative has reported orbit size 4 and stabilizer size 4.

## 9. Artificial probability-pattern feasibility scan

The pattern family examined:
- three ternary-uniform vectors (one zero, three entries 1/3);
- two binary-uniform vectors (two entries 1/2, two zeros);
- arbitrary assignment to five bases.

Count:
\[
\binom53\,4^3\,6^2=23,040.
\]
An exact SymPy principal-minor scan timed out. A later NumPy floating-point scan reported that all 23,040 reconstructed candidates had at least one negative 2x2 principal minor; the maximum, over candidates, of the minimum of the six such minors was approximately
\[
-0.0347222222\approx-5/144.
\]
This is numerical evidence only. A later statement claiming an exact integer-arithmetic exhaustive result was unsupported and is withdrawn. Do not rerun the whole scan unless specifically producing a new exact integer-arithmetic certificate; the floating-point observation is already recorded here.

## 10. Global proof design already considered

Projective state space is \(\mathbb{CP}^3\), six real dimensions. Four coordinate charts suffice: choose a largest component, fix its phase, and write the other three complex ratios with modulus at most one. Charts overlap.

For an interval box, bound each probability:
\[
p_{j,a}=
\frac{|(B_j^\dagger z)_a|^2}
{1+\sum_{\ell\ne k}|z_\ell|^2}.
\]
For \(h(p)=-p\log_2p\), the minimum over a closed interval \([L,U]\subseteq[0,1]\) is at an endpoint, because h is increasing up to 1/e and decreasing afterwards (with h(0)=0). A box lower bound can sum the individual endpoint minima. If below 7, subdivide.

A valid verifier still needs outward rounding, zero handling, exhaustive coverage, a termination certificate, and a treatment of equality neighborhoods. No such global computation has been run.

## 11. Previously mentioned but unverified calculations — do not repeat as facts

Earlier exploratory messages included claims about:
- spectra of \(\Omega_3\);
- dimensions of invariant symmetric-square spaces;
- orbit ranks and invariant Gram matrix dimensions;
- exact triple-product coefficient distributions;
- Jacobian ranks;
- polynomial nonzero monomial counts and integer coefficient maxima;
- a restricted representation and a complete SOS certificate.

These claims were not accompanied by a reproducible execution in the available record. They are intentionally not promoted to results. If a future proof strategy needs one, recompute it from the explicit matrices and save code/output.

## 12. Immediate continuation checklist

Do not restart the literature review, re-derive the collision bound, or re-discover the equality example without a reason.

Next concrete tasks:
1. Create a reproducible exact SymPy script for the five matrices, pairwise MUB checks, equality distributions, and four-ray orbit.
2. Re-derive the zero-outcome amplitudes directly from the explicit matrices, with exact complex arithmetic.
3. Verify the first derivative of the positive-outcome entropy contribution exactly; only then derive a local certificate with valid entropy bounds.
4. Build the exact Pauli class permutation and matrix-level monomial basis action tables.
5. Choose a global analytic/SOS/interval strategy and pursue an actual certificate.
6. Keep equality classification separate from the universal inequality.

## 13. Session handoff rule

At the start of a future session, read:
- docs/STATUS.md
- docs/VERIFICATION.md
- this file

Then continue from checklist item 1 or the latest explicit checkpoint. Do not claim that any item is complete unless the corresponding artifact is committed and independently checkable.
