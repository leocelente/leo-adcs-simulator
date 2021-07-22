from random import random


def Model(B: list[float]):
    '''
    Modelo do Magnetometro. Aplica um bias e ruido
    no sinal original
    '''
    assert(B.shape == (3, 1))
