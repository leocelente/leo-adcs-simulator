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
I: np.matrix = np.diag([0.9, 0.9, 0.3])
invI = np.linalg.inv(I)


def Model(t: float, state):
    state = np.ravel(state.T).tolist()
    [x, y, z] = state[0:3]
    vel = np.matrix(state[3:6]).T
    q0123 = np.matrix(state[6:10]).T
    [p, q, r] = state[10:13]
    pqr = np.matrix(state[10:13]).T

    PQRMAT = np.matrix([[0, -p, -q, -r], [p, 0, r, -q],
                       [q, -r, 0, p], [r, q, -p, 0]])
    q0123_dot = 0.5*PQRMAT*q0123
    q0123_dot = np.ravel(q0123_dot).T
    kk = np.matrix([1, 2, 3]).T
    rv = state[0:3]
    rho: float = np.linalg.norm(rv)
    rhat = rv/rho
    Fgrav = -(G*M*m/rho**2)*rhat
    if t % 5 == 0:
        # Convert Cartesian x,y,z into Lat, Lon, Alt
        phiE = 0.
        thetaE = acos(z/rho)
        psiE = atan2(y, x)

        latitude = 90 - thetaE * (180/pi)
        longitude = psiE * (180/pi)
        rho_km = (rho) / 1000
        today = date.fromisoformat('2020-01-01')
        BNED = MagneticFieldModel(
            today, glat=latitude, glon=longitude, alt_km=rho_km, itype=0)
        # Convert NED (North East Down to X,Y,Z in ECI frame)
        # First we need to create a rotation matrix from the NED frame to the
        # inertial frame
        BNED = np.matrix([BNED.north, BNED.east, BNED.down])  # ECI
        BI = DCM.fromEulerAngle(euler=np.matrix(
            [phiE, thetaE+pi, psiE]).T) * BNED  # Satellite Orbit
        Model.BB = DCM.fromQuaternion(q0123).T * BI  # Satellite Body
        # Convert to Tesla
        Model.BB = Model.BB*1e-9

    BfieldMeasured = Magnetometer.Model(Model.BB)
    pqrMeasured = Gyroscope.Model(pqr)
    [BfieldNav, pqrNav] = Filter.Estimate(BfieldMeasured, pqrMeasured)
    accel = Fgrav/m
    LMN_magtorquers = np.matrix([0., 0., 0.]).T
    H = np.matmul(I, pqr)
    # A bunch of numpy conversion to flatten states
    pqr = pqr.T.tolist()[0]
    H = H.T.tolist()[0]
    c = np.matrix(np.cross(pqr, H)).T
    pqr_dot = np.matmul(invI, (LMN_magtorquers - c))
    _v = np.ravel(vel.T).tolist()
    _a = np.ravel(accel).tolist()
    _q = np.ravel(np.ravel(q0123_dot.T).tolist()).tolist()
    _p = np.ravel(pqr_dot).tolist()
    _s = np.concatenate((_v, _a, _q, _p))
    dstate = _s.T
    return dstate


Model.BB = np.matrix([0, 0, 0]).T
