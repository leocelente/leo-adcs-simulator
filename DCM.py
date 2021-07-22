import numpy as np
from math import cos, sin


def fromQuaternion(quaternion: list[float]):
    '''
    Converte representação em Quaternion `[w, xi, yj, zk]`
    para a matriz de cossenos (DCM)
    '''
    assert(quaternion.shape == (4, 1))
    [q0, q1, q2, q3] = quaternion.flat

    DCM = np.array([
        [(q0 ** 2+q1 ** 2-q2 ** 2-q3 ** 2), 2*(q1*q2-q0*q3), 2*(q0*q2+q1*q3)],
        [2*(q1*q2+q0*q3), (q0 ** 2-q1 ** 2+q2 ** 2-q3 ** 2), 2*(q2*q3-q0*q1)],
        [2*(q1*q3-q0*q2), 2*(q0*q1+q2*q3), (q0 ** 2-q1 ** 2-q2 ** 2+q3 ** 2)]
    ], dtype=float)
    assert(DCM.shape == (3, 3))
    return DCM


def fromEulerAngle(euler: list[float]):
    '''
    Converte representação em angulos de Euler321\n
    `Yaw (1), Pitch (2), Roll (3)` 
    para a matriz de cossenos (DCM)
    '''
    assert(euler.shape == (3, 1))

    [yaw, pitch, roll] = euler.flat
    cp: float = cos(pitch)
    sp: float = sin(pitch)
    sy: float = sin(yaw)
    cy: float = cos(yaw)
    sr: float = sin(roll)
    cr: float = cos(roll)

    DCM = np.array([
        [cp*cr,  sy*sp*cr-cy*sr, cy*sp*cr+sy*sr],
        [cp*sr,  sy*sp*sr+cy*cr, cy*sp*sr-sy*cr],
        [-sp,    sy*cp,          cy*cp]
    ], dtype=float)

    assert(DCM.shape == (3, 3))
    return DCM
