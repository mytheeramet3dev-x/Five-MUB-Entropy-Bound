# Pauli Symmetry and Entropy Invariance

## Scope

This document proves a conditional symmetry theorem for the entropy functional. The theorem is purely mathematical; applying it to the repository's concrete Pauli operators requires the exact basis-action certificate to be verified.

## Setup

Let \(B_j\in\mathbb C^{4\times4}\) be unitary basis matrices, with columns the basis vectors, for \(j=0,\ldots,4\). For a unit state \(\psi\), define
\[
p_j(\psi)=\bigl(|(B_j^\dagger\psi)_a|^2\bigr)_{a=0}^3,
\quad H_j(\psi)=-\sum_a p_{j,a}(\psi)\log_2p_{j,a}(\psi),
\]
using \(0\log_2 0=0\), and \(F(\psi)=\sum_jH_j(\psi)\).

Suppose a unitary \(U\) permutes the five bases in the following matrix-level sense: there is a permutation \(\pi\) of \(\{0,\ldots,4\}\) and, for every \(j\), a monomial unitary \(M_j\) (a permutation matrix times diagonal phases) such that
\[
UB_j=B_{\pi(j)}M_j.
\tag{PS}
\]

## Theorem — entropy invariance under monomial basis action

Under (PS), for every unit vector \(\psi\),
\[
F(U\psi)=F(\psi).
\]

### Proof

From (PS), left-multiply by \(B_{\pi(j)}^\dagger\):
\[
B_{\pi(j)}^\dagger U\psi=M_jB_j^\dagger\psi.
\]
A monomial unitary has exactly one unit-modulus entry in each row and column. Thus applying \(M_j\) only permutes the four coordinates and multiplies them by phases. Taking coordinatewise squared moduli removes phases and permutes the probability vector. Therefore
\[
p_{\pi(j)}(U\psi)=\sigma_j(p_j(\psi))
\]
for a coordinate permutation \(\sigma_j\). Shannon entropy is invariant under coordinate permutations, hence
\[
H_{\pi(j)}(U\psi)=H_j(\psi).
\]
Since \(\pi\) permutes all five basis labels, summing over \(j\) proves \(F(U\psi)=F(\psi)\). \(\square\)

## Consequences and limits

1. If (PS) is verified for a group \(G\) of unitaries, then \(F\) is constant on every orbit \(G\cdot\psi\). A state and all its orbit members have identical entropy objective values.
2. This does **not**, by itself, prove that a search may be restricted to a chosen fundamental domain. Such restriction additionally requires a rigorous construction showing the domain meets every orbit (or a covering argument).
3. This theorem does not prove \(F\ge7\), nor does it classify equality states.
4. A Pauli operator preserving the set of commuting classes is not yet enough for (PS). The explicit matrices must yield monomial overlap matrices \(B_{\pi(j)}^\dagger U B_j\), checked exactly.
5. Until the certificate generator and checker are executed and the records archived, this theorem is **PROVED CONDITIONALLY**, while its concrete application to the repository's Pauli set is **NOT YET VERIFIED**.

## Proof obligation for each concrete \(U\)

For every input basis \(j\), provide:
- target index \(\pi(j)\), with the five targets forming a permutation;
- exact overlap \(R_j=B_{\pi(j)}^\dagger U B_j\);
- exactly one nonzero entry per row and column;
- exact modulus one for every nonzero entry.

These conditions establish \(R_j=M_j\) and hence (PS).
