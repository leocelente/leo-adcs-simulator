import numpy as np
from math import cos, sin


def fromQuaternion(quaternion):
    # % compute R such that v(inertial) = TIB v(body)

    [q0, q1, q2, q3] = quaternion.T.squeeze().tolist()[0]

    DCM = np.matrix([
        [(q0 ** 2+q1 ** 2-q2 ** 2-q3 ** 2), 2*(q1*q2-q0*q3), 2*(q0*q2+q1*q3)],
        [2*(q1*q2+q0*q3), (q0 ** 2-q1 ** 2+q2 ** 2-q3 ** 2), 2*(q2*q3-q0*q1)],
        [2*(q1*q3-q0*q2), 2*(q0*q1+q2*q3), (q0 ** 2-q1 ** 2-q2 ** 2+q3 ** 2)]
    ])
    return DCM

# % Matrix originally adopted from Boom 2010 - Mark Costello
# % Copyright - Carlos Montalvo 2015
# % You may freely distribute this file but please keep my name in here
# % as the original owner


def fromEulerAngle(euler):
    [phi, theta, psi] = euler
    ct = cos(theta)
    st = sin(theta)
    sp = sin(phi)
    cp = cos(phi)
    ss = sin(psi)
    cs = cos(psi)

    out = np.matrix([
        [ct*cs,  sp*st*cs-cp*ss, cp*st*cs+sp*ss],
        [ct*ss,  sp*st*ss+cp*cs, cp*st*ss-sp*cs],
        [-st,    sp*ct,          cp*ct]
    ])
    return out
