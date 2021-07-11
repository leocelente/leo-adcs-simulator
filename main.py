import Satellite
from Integrator import RK4
from Orbit import *
[q0, q1, q2, q3] = np.ravel(q0123_0.T).tolist()
state = np.matrix([x0, y0, z0, x_dot0, y_dot0, z_dot0, q0,q1,q2,q3, p0, q0, r0]).T
number_of_orbits = 1.
tfinal = period*number_of_orbits
timestep = 1.0
t_out = np.linspace(0.0, tfinal, num=int(tfinal))

print("Start of Simulation")
for i in range(len(t_out)):
    if i % 250 == 0:
        print("T=", i) 
    state = RK4(Satellite.Model, state, t_out[i], timestep)

print("End of Simulation")
