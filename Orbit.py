import numpy as np
from Earth import R, mu
from math import pi

altitude: float = 600e3
position_0 = np.array([[R + altitude, 0, 0]], dtype=float).T

orbit_inclination: float = 54.24 * (pi/180)
semi_major: float = np.linalg.norm(position_0)
circular_vel: float = np.sqrt(mu/semi_major)
period: float = 2*pi/np.sqrt(mu)*semi_major**(3/2)

vel_y_0: float = circular_vel * np.cos(orbit_inclination)
vel_z_0: float = circular_vel * np.sin(orbit_inclination)
velocity_0 = np.array([[0, vel_y_0, vel_z_0]], dtype=float).T

attitude_0 = np.array([[1, 0, 0, 0]], dtype=float).T
omega_0 = np.array([[0.08, -0.02, 0.03]], dtype=float).T

BB = np.array([[0, 0, 0]], dtype=float).T
