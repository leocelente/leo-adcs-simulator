from math import cos, sin
import numpy as np


def fromEulerAngle(euler):

    phi = euler[0]
    theta = euler[1]
    psi = euler[2]

    q0 = cos(phi/2)*cos(theta/2)*cos(psi/2) + \
        sin(phi/2)*sin(theta/2)*sin(psi/2)
    q1 = sin(phi/2)*cos(theta/2)*cos(psi/2) - \
        cos(phi/2)*sin(theta/2)*sin(psi/2)
    q2 = cos(phi/2)*sin(theta/2)*cos(psi/2) + \
        sin(phi/2)*cos(theta/2)*sin(psi/2)
    q3 = cos(phi/2)*cos(theta/2)*sin(psi/2) - \
        sin(phi/2)*sin(theta/2)*cos(psi/2)

    return np.matrix([q0, q1, q2, q3]).T

# % Copyright - Carlos Montalvo 2015
# % You may freely distribute this file but please keep my name in here
# % as the original owner
