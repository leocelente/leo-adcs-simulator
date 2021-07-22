from math import cos, sin
import numpy as np


def fromEulerAngle(euler: list[float]):
    '''
    Converte da representação de angulos de Euler321,\n
    `Yaw (1), Pitch (2), Roll (3)`
    Para Quaternions\n
    `[w, xi, yj, zk]`\n
    Usada apenas para inicializar a atitude com angulos de euler
    '''

    assert(euler.shape == (3, 1))
    phi: float = euler[0]
    theta: float = euler[1]
    psi: float = euler[2]

    q0 = cos(phi/2)*cos(theta/2)*cos(psi/2) + \
        sin(phi/2)*sin(theta/2)*sin(psi/2)
    q1 = sin(phi/2)*cos(theta/2)*cos(psi/2) - \
        cos(phi/2)*sin(theta/2)*sin(psi/2)
    q2 = cos(phi/2)*sin(theta/2)*cos(psi/2) + \
        sin(phi/2)*cos(theta/2)*sin(psi/2)
    q3 = cos(phi/2)*cos(theta/2)*sin(psi/2) - \
        sin(phi/2)*sin(theta/2)*cos(psi/2)
    out = np.array([[q0, q1, q2, q3]], dtype=float).T
    assert(out.shape == (4, 1))
    return out
# Original MATLAB code copyright comment
# % Copyright - Carlos Montalvo 2015
# % You may freely distribute this file but please keep my name in here
# % as the original owner
