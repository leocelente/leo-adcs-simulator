from math import acos, atan2, pi
from Earth import M
from Universe import G
import numpy as np
from igrf import igrf as MagneticFieldModel
import DCM
from datetime import date
import Magnetometer
import Gyroscope
import Filter

m: float = 2.6
I = np.diag([0.9, 0.9, 0.3])
invI = np.linalg.inv(I)


def rotationModel(w, torques):
    H = I @ w
    c = np.cross(w, H, axis=0)
    w_dot = invI @ (torques - c)
    return w_dot


def attitudeModel(quaternion, w):
    p, q, r = w
    assert(quaternion.shape == (4, 1))
    PQRMAT = np.array([[0, -p, -q, -r], [p, 0, r, -q],
                       [q, -r, 0, p], [r, q, -p, 0]],  dtype=float)
    quaternion_dot = 0.5*PQRMAT @ quaternion
    assert(quaternion_dot.shape == (4, 1))
    quaternion_dot = np.reshape(quaternion_dot, (4, 1))
    return quaternion_dot


def accelerationModel(xyz):
    rho: float = np.linalg.norm(xyz)
    rhat: float = xyz/rho
    Fgrav: list[float] = -(G*M*m/rho**2)*rhat
    accel: list[float] = Fgrav/m
    return accel


def velocityModel(vel):
    return vel


def magneticModel(xyz, posAngle):
    phiE, thetaE, psiE = posAngle.flat
    rho: float = np.linalg.norm(xyz)
    latitude: float = 90 - thetaE * (180/pi)
    longitude: float = psiE * (180/pi)
    rho_km: float = (rho) / 1000
    today = date.fromisoformat('2020-01-01')
    BNED = MagneticFieldModel(
        today, glat=latitude, glon=longitude, alt_km=rho_km, itype=0)
    BNED = np.array([BNED.north, BNED.east, BNED.down], dtype=float)
    BNED = BNED*1e-9
    return BNED


def polar(xyz):
    x, y, z = xyz
    rho: float = np.linalg.norm(xyz)
    phiE: float = 0.
    thetaE: float = acos(z/rho)
    psiE: float = atan2(y, x)
    return np.array([[phiE, thetaE, psiE]]).T


def propagateVector(v, pos_angles, q0123):
    assert(v.shape == (3, 1))
    assert(pos_angles.shape == (3, 1))
    BI = DCM.fromEulerAngle(pos_angles) @ v
    assert(BI.shape == (3, 1))
    vv = DCM.fromQuaternion(q0123).T @ BI
    return vv


def Magnetorquer(state):
    return np.array([[0, 0, 0]], dtype=float).T


def Model(t: float, state: list[float]):
    """
        Returns the change, d state/dt
    """
    assert(state.shape == (13, 1))
    position_cartesian = state[0:3]
    angular_speed = state[10:13]

    quaternion = state[6:10]
    quaternion_dot = attitudeModel(quaternion, angular_speed)

    acceleration = accelerationModel(position_cartesian)

    if t % 20 == 0:
        position_polar = polar(position_cartesian)
        BNED = magneticModel(position_cartesian, position_polar)
        Model.BB = propagateVector(BNED, position_polar, quaternion)

    BfieldMeasured = Magnetometer.Model(Model.BB)
    pqrMeasured = Gyroscope.Model(angular_speed)
    [BfieldNav, pqrNav] = Filter.Estimate(BfieldMeasured, pqrMeasured)

    net_torques = Magnetorquer(state)
    angular_acceleration = rotationModel(angular_speed, net_torques)

    velocity = state[3:6]

    dstate = np.vstack(
        [velocity, acceleration, quaternion_dot, angular_acceleration])

    assert(dstate.shape == (13, 1))
    return dstate


Model.BB = np.array([[0, 0, 0]], dtype=float).T
