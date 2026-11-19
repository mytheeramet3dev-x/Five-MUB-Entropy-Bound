"""Exact data for the fixed five-MUB convention used in this project.
Matrices have basis vectors as columns. SymPy expressions are exact.
"""
import sympy as sp

I = sp.I
sqrt2 = sp.sqrt(2)
B0 = sp.eye(4)
B1 = sp.Matrix([[1,-1,-1,1],[1,1,-1,-1],[1,-1,1,-1],[1,1,1,1]]) / 2
B2 = sp.Matrix([[-1,1,1,-1],[-I,-I,I,I],[-I,I,-I,I],[1,1,1,1]]) / 2
B3 = sp.Matrix([[-I,I,-I,I],[-I,I,I,-I],[-1,-1,1,1],[1,1,1,1]]) / 2
B4 = sp.Matrix([[I,-I,-I,I],[-1,1,-1,1],[I,I,-I,-I],[1,1,1,1]]) / 2
BASES = (B0, B1, B2, B3, B4)
PSI_STAR = sp.Matrix([1,1,0,0]) / sqrt2

PAULI_I = sp.eye(2)
PAULI_X = sp.Matrix([[0,1],[1,0]])
PAULI_Z = sp.diag(1,-1)

def exact_probabilities(state, basis):
    """Four exact probabilities; columns of basis are its basis vectors."""
    amplitudes = basis.conjugate().T * state
    return tuple(sp.simplify(sp.expand_complex(a*sp.conjugate(a))) for a in amplitudes)

def shannon_entropy_bits(probabilities):
    """Exact symbolic entropy, with 0 log 0 interpreted as zero."""
    terms = []
    for p in probabilities:
        p = sp.simplify(p)
        if p != 0:
            terms.append(-p * sp.log(p, 2))
    return sp.simplify(sum(terms, sp.Integer(0)))

def pauli_operators():
    """Yield all 16 two-qubit Paulis modulo global phase."""
    for x1 in (0,1):
        for z1 in (0,1):
            for x2 in (0,1):
                for z2 in (0,1):
                    a = (PAULI_X if x1 else PAULI_I) * (PAULI_Z if z1 else PAULI_I)
                    b = (PAULI_X if x2 else PAULI_I) * (PAULI_Z if z2 else PAULI_I)
                    yield f"{x1}{z1}{x2}{z2}", sp.kronecker_product(a,b)
