import numpy as np


def Estimate(field, avel):
    s = 0.3
    if sum(Estimate.BfieldNavPrev) + sum(Estimate.pqrNavPrev) == 0:
        BfieldNav = field
        pqrNav = avel
    else:
        BiasEstimate = np.matrix([0, 0, 0]).T
        BfieldNav = Estimate.BfieldNavPrev*(1-s) + s*(field-BiasEstimate)
        pqrBiasEstimate = np.matrix([0, 0, 0]).T
        pqrNav = Estimate.pqrNavPrev*(1-s) + s*(avel-pqrBiasEstimate)
    Estimate.BfieldNavPrev = BfieldNav
    Estimate.pqrNavPrev = pqrNav
    return [BfieldNav, pqrNav]


Estimate.BfieldNavPrev = np.matrix([0, 0, 0]).T
Estimate.pqrNavPrev = np.matrix([0, 0, 0]).T
