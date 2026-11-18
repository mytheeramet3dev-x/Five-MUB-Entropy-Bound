# Mathematical Foundations

## 1. Entropy convention

All logarithms in entropy expressions are base 2, and \(0\log_2 0:=0\).

For an orthonormal basis \(B_j=(b_{j,0},\ldots,b_{j,3})\), define
\[
p_{j,a}=|\langle b_{j,a}|\psi\rangle|^2,\qquad
H_j(\psi)=-\sum_{a=0}^3p_{j,a}\log_2p_{j,a}.
\]
The objective is \(F(\psi)=\sum_{j=0}^4H_j(\psi)\).

## 2. Explicit MUB convention

The following matrices are used, with columns as basis vectors:
\[
B_0=I_4,
\]
\[
B_1=\frac12\begin{pmatrix}
1&-1&-1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&1&1&1
\end{pmatrix},
\quad
B_2=\frac12\begin{pmatrix}
-1&1&1&-1\\
-i&-i&i&i\\
-i&i&-i&i\\
1&1&1&1
\end{pmatrix},
\]
\[
B_3=\frac12\begin{pmatrix}
-i&i&-i&i\\
-i&i&i&-i\\
-1&-1&1&1\\
1&1&1&1
\end{pmatrix},
\quad
B_4=\frac12\begin{pmatrix}
i&-i&-i&i\\
-1&1&-1&1\\
i&i&-i&-i\\
1&1&1&1
\end{pmatrix}.
\]

The convention is reported to have been checked exactly in SymPy:
\[
B_j^\dagger B_j=I_4,
\qquad
|(B_j^\dagger B_k)_{ab}|^2=\frac14
\quad(j\ne k).
\]
The actual verification script and raw output must still be committed before treating this repository alone as a reproducible verification package.

## 3. Equality example

Take
\[
\psi_* = \frac1{\sqrt2}(1,1,0,0)^T.
\]
For the matrices above, the reported outcome distributions are:
\[
\begin{array}{c|c|c}
\text{Basis}&\text{Probability vector}&H_j\\\hline
B_0&(1/2,1/2,0,0)&1\\
B_1&(1/2,0,1/2,0)&1\\
B_2&(1/4,1/4,1/4,1/4)&2\\
B_3&(1/2,1/2,0,0)&1\\
B_4&(1/4,1/4,1/4,1/4)&2
\end{array}
\]
Thus \(F(\psi_*)=7\). This establishes an equality example, not the universal lower bound.

The reported Pauli orbit consists of four rays:
\[
\frac1{\sqrt2}(1,1,0,0)^T,\quad
\frac1{\sqrt2}(1,-1,0,0)^T,\quad
\frac1{\sqrt2}(0,0,1,1)^T,\quad
\frac1{\sqrt2}(0,0,1,-1)^T.
\]
All four are reported to have entropy sum 7. This is not a complete classification of all minimizers.

## 4. Pauli commuting classes

Using two-qubit Pauli notation, the five classes are
\[
\mathcal C_0=\{ZI,IZ\},\quad
\mathcal C_1=\{XI,IX\},\quad
\mathcal C_2=\{YI,IY\},
\]
\[
\mathcal C_3=\{ZX,XY\},\quad
\mathcal C_4=\{ZY,XZ\}.
\]
Together these classes partition the 15 nonidentity two-qubit Pauli operators. Their common eigenbases define a complete set of five MUBs. The correspondence between these classes and the explicit matrices above should be included in the exact verification scripts.

The 16 two-qubit Pauli operators modulo global phase form a group isomorphic to \(\mathbb Z_2^4\). Pauli conjugation maps each Pauli operator to itself or its negative and therefore permutes the commuting classes. To obtain a full symmetry certificate for the explicit matrices, additionally verify that each transformed basis is a column permutation with phases of one of the five displayed bases.

## 5. Collision identity

For a complete set of five MUBs in dimension four, let
\[
C_j=\sum_{a=0}^3p_{j,a}^2.
\]
The complete-MUB second-moment identity is
\[
\sum_{j=0}^4C_j=1+\operatorname{Tr}(\rho^2).
\]
For pure \(\rho=|\psi\rangle\langle\psi|\), this gives
\[
\boxed{\sum_{j=0}^4C_j=2.}
\]

Since Shannon entropy dominates collision entropy,
\[
H(p)\ge-\log_2\sum_ap_a^2,
\]
and by AM-GM,
\[
F(\psi)\ge-\sum_{j=0}^4\log_2C_j
\ge5\log_2(5/2)\approx6.60964.
\]
This is a valid lower bound but is weaker than the target 7-bit bound.

## 6. Pure-state reconstruction

Let \(P_{j,a}=|b_{j,a}\rangle\langle b_{j,a}|\). For a complete set of MUBs,
\[
\rho=\frac{I_4}{4}+\sum_{j,a}(p_{j,a}-1/4)P_{j,a}.
\]
For pure states, with \(X=\rho-I_4/4\),
\[
\operatorname{Tr}(X^2)=\frac34,
\qquad
X^2=\frac12X+\frac{3}{16}I_4.
\]
These identities provide algebraic constraints on candidate probability tables. Any use in a certificate must retain the nonnegativity of all probabilities and the positive-semidefinite/rank-one condition on reconstructed \(\rho\).

## 7. Entropy-gap identity

For a probability vector \(p\), define
\[
C(p)=\sum_ap_a^2,\qquad
\Delta(p)=H(p)+\log_2C(p).
\]
Then \(\Delta(p)\ge0\), and
\[
F(\psi)=-\log_2\left(\prod_{j=0}^4C_j\right)
+\sum_{j=0}^4\Delta(p_j).
\]
Consequently, the desired inequality is equivalent to
\[
\sum_j\Delta(p_j)\ge
\log_2\left(128\prod_jC_j\right).
\]
If \(128\prod_jC_j\le1\), nonnegativity of each \(\Delta\) suffices. The difficult regime is where this product exceeds 1.

Also, if \(r_a=p_a^2/C(p)\), then
\[
\Delta(p)=D_{\rm KL}(p\|r)
\]
with base-2 relative entropy. Pinsker gives
\[
\Delta(p)\ge\frac{1}{2\ln2}\|p-r\|_1^2.
\]
A missing step is a sufficiently strong quantum-state constraint on the five deviations \(\|p_j-r_j\|_1\).

## 8. Third and higher moments

Define
\[
M_k=\sum_{j=0}^4\sum_{a=0}^3p_{j,a}^k.
\]
For the displayed equality example, the reported values are
\[
M_2=2,\quad M_3=\frac78,\quad
M_4=\frac{13}{32},\quad M_5=\frac{25}{128}.
\]
The conjectural inequality \(M_3\ge7/8\) has appeared in the exploration, but no proof has been established here. Even a third-moment inequality would need a valid bridge to Shannon entropy before it could prove the target.

## 9. Entropy polynomial lower approximation

For \(0\le x\le1\) and integer \(m\ge1\),
\[
P_m(x)=\frac{x}{\ln2}\sum_{k=1}^m\frac{(1-x)^k}{k}
\le -x\log_2x.
\]
The exact remainder is
\[
-x\log_2x-P_m(x)
=\frac{x}{\ln2}\sum_{k=m+1}^{\infty}\frac{(1-x)^k}{k}
\ge\frac{x(1-x)^{m+1}}{(m+1)\ln2}.
\]
This gives polynomial/moment lower bounds, but the bounds obtained so far have not reached 7 uniformly.