from random import random



def Model(pqr):
    AngscaleBias = 0.01
    AngFieldBias = AngscaleBias*(2*random()-1)
    AngscaleNoise = 0.001
    AngFieldNoise = AngscaleNoise*(2*random()-1)
    return pqr + AngFieldBias + AngFieldNoise
