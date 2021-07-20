import Satellite
from Integrator import RK4
from Orbit import *
from matplotlib import pyplot as plt
from Earth import R

[q0, q1, q2, q3] = np.ravel(q0123_0.T).tolist()
BB = np.array([[0, 0, 0]], dtype=float).T
state = np.array([[x0, y0, z0, x_dot0, y_dot0, z_dot0,
                  q0, q1, q2, q3, p0, qq0, r0, BB[0, 0], BB[1, 0], BB[2, 0]]], dtype=float).T

number_of_orbits: float = 1
tfinal: float = period*number_of_orbits
timestep: float = 1.0
t_out = np.arange(0.0, tfinal, timestep, dtype=float)

view_state = []
print("Start of Simulation")
for i in range(len(t_out)):
    if i % 250 == 0:
        print("T=", i)

    state = RK4(Satellite.Model, state, t_out[i], timestep)
    view_state.append(state[0:16, 0])

print("End of Simulation")
view_state = np.array(view_state)

u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:20j]
x = R*1e-3*np.cos(u)*np.sin(v)
y = R*1e-3*np.sin(u)*np.sin(v)
z = R*1e-3*np.cos(v)
ax.plot_wireframe(x, y, z, color="lightblue", alpha=0.8)
# plt.plot(t_out, xs, color="red")
# plt.plot(t_out, ys, color="green")
# plt.plot(t_out, zs, color="blue")

plt.show()
