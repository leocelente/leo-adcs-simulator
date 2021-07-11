from random import random

def Model(BB):
    MagscaleBias = (4e-7)
    MagFieldBias = MagscaleBias*(2*random()-1)
    MagscaleNoise = (1e-5)
    MagFieldNoise = MagscaleNoise*(2*random()-1)
    return BB + MagFieldBias + MagFieldNoise
