from random import random

gyro_bias = 1e-2
gyro_noise = 1e-3


def Model(omega):
    '''
    Modelo do Giroscópio, aplica um bias e ruido caracteristico
    de sensores no sinal de simulação (original)
    '''
    assert(omega.shape == (3, 1))
    bias: float = gyro_bias * random()
    noise: float = gyro_noise * random()
    return omega + bias + noise
