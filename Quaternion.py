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

    [yaw, pitch, roll] = euler.flat

    cy = cos(yaw/2)
    cp = cos(pitch/2)
    cr = cos(roll/2)
    sy = sin(yaw/2)
    sp = sin(pitch/2)
    sr = sin(roll/2)

    q0 = cy * cp * cr + sy * sp * sr
    q1 = sy * cp * cr - cy * sp * sr
    q2 = cy * sp * cr + sy * cp * sr
    q3 = cy * cp * sr - sy * sp * cr

    out = np.array([[q0, q1, q2, q3]], dtype=float).T
    assert(out.shape == (4, 1))

    return out
