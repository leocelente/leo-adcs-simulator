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

# % Matrix originally adopted from Boom 2010 - Mark Costello
# % Copyright - Carlos Montalvo 2015
# % You may freely distribute this file but please keep my name in here
# % as the original owner


def fromEulerAngle(euler: list[float]):
    '''
    Converte representação em angulos de Euler321\n
    `Yaw (1), Pitch (2), Roll (3)` 
    para a matriz de cossenos (DCM)
    '''
    assert(euler.shape == (3, 1))

    [phi, theta, psi] = euler.flat
    ct: float = cos(theta)
    st: float = sin(theta)
    sp: float = sin(phi)
    cp: float = cos(phi)
    ss: float = sin(psi)
    cs: float = cos(psi)

    out = np.array([
        [ct*cs,  sp*st*cs-cp*ss, cp*st*cs+sp*ss],
        [ct*ss,  sp*st*ss+cp*cs, cp*st*ss-sp*cs],
        [-st,    sp*ct,          cp*ct]
    ], dtype=float)
    assert(out.shape == (3, 3))
    return out
