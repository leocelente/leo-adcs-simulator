from random import random


def Model(BB: list[float]):
    assert(BB.shape == (3, 1))
    MagscaleBias: float = (4e-7)
    MagFieldBias: float = MagscaleBias*(2*random()-1)
    MagscaleNoise: float = (1e-5)
    MagFieldNoise: float = MagscaleNoise*(2*random()-1)
    return BB + MagFieldBias + MagFieldNoise
