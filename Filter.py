import numpy as np


def Estimate(field, avel):
    assert(field.shape == (3, 1))
    assert(avel.shape == (3, 1))
    s = 0.3
    if sum(Estimate.BfieldNavPrev) + sum(Estimate.pqrNavPrev) == 0:
        BfieldNav = field
        pqrNav = avel
    else:
        BiasEstimate = np.array([[0, 0, 0]], dtype=float).T
        BfieldNav = Estimate.BfieldNavPrev*(1-s) + s*(field-BiasEstimate)
        pqrBiasEstimate = np.array([[0, 0, 0]], dtype=float).T
        pqrNav = Estimate.pqrNavPrev*(1-s) + s*(avel-pqrBiasEstimate)
    Estimate.BfieldNavPrev = BfieldNav
    Estimate.pqrNavPrev = pqrNav

    assert(BfieldNav.shape == (3, 1))
    assert(pqrNav.shape == (3, 1))
    return [BfieldNav, pqrNav]


Estimate.BfieldNavPrev = np.array([[0, 0, 0]], dtype=float).T
Estimate.pqrNavPrev = np.array([[0, 0, 0]], dtype=float).T
