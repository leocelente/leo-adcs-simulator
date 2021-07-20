import Quaternion
import numpy as np
from Earth import R, mu
from math import pi, sqrt, sin, cos

altitude: float = 600e3
x0: float = R + altitude
y0: float = 0.0
z0: float = 0.0

orbit_inclination: float = 54.24 * (pi/180)
semi_major: float = np.linalg.norm([x0, y0, z0])
circular_vel: float = sqrt(mu/semi_major)

x_dot0: float = 0
y_dot0: float = circular_vel * cos(orbit_inclination)
z_dot0: float = circular_vel * sin(orbit_inclination)

phi0: float = 0
theta0: float = 0
psi0: float = 0
ptp0 = np.array([[phi0, theta0, psi0]], dtype=float).T
q0123_0 = Quaternion.fromEulerAngle(ptp0)
p0: float = 0.08
qq0: float = -0.02
r0: float = 0.03


period: float = 2*pi/sqrt(mu)*semi_major**(3/2)
