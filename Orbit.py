import Quaternion
import numpy as np
from Earth import R, mu
from math import pi, sqrt, sin, cos

altitude = 600e3
x0 = R + altitude
y0 = 0.0
z0 = 0.0

orbit_inclination = 54.24 * (pi/180)
semi_major = np.linalg.norm([x0, y0, z0])
circular_vel = sqrt(mu/semi_major)

x_dot0 = 0
y_dot0 = circular_vel * cos(orbit_inclination)
z_dot0 = circular_vel * sin(orbit_inclination)

phi0 = 0
theta0 = 0
psi0 = 0
ptp0 = np.matrix([phi0, theta0, psi0]).T
q0123_0 = Quaternion.fromEulerAngle(ptp0)
p0 = 0.08
q0 = -0.02
r0 = 0.03


period = 2*pi/sqrt(mu)*semi_major**(3/2)
