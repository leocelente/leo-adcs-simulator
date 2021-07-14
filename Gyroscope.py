from random import random


def Model(pqr):
    assert(pqr.shape == (3, 1))
    AngscaleBias: float = 0.01
    AngFieldBias: float = AngscaleBias*(2*random()-1)
    AngscaleNoise: float = 0.001
    AngFieldNoise: float = AngscaleNoise*(2*random()-1)
    return pqr + AngFieldBias + AngFieldNoise
