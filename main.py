import Satellite
from Integrator import RK4
from Orbit import *
from matplotlib import pyplot as plt
from Earth import R

[q0, q1, q2, q3] = np.ravel(q0123_0.T).tolist()
state = np.array([[x0, y0, z0, x_dot0, y_dot0, z_dot0,
                  q0, q1, q2, q3, p0, q0, r0]], dtype=float).T

number_of_orbits: float = 1
tfinal: float = period*number_of_orbits
timestep: float = 1.0
t_out = np.arange(0.0, tfinal, timestep, dtype=float)

position: list[float] = [[], [], []]

print("Start of Simulation")
for i in range(len(t_out)):
    if i % 250 == 0:
        print("T=", i)

    state = RK4(Satellite.Model, state, t_out[i], timestep)
    position[0].append(state[0, 0]*1e-3)
    position[1].append(state[1, 0]*1e-3)
    position[2].append(state[2, 0]*1e-3)


print("End of Simulation")
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(position[0], position[1],
          position[2], 'red')

u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:20j]
x = R*1e-3*np.cos(u)*np.sin(v)
y = R*1e-3*np.sin(u)*np.sin(v)
z = R*1e-3*np.cos(v)
ax.plot_wireframe(x, y, z, color="lightblue", alpha=0.8)
# plt.plot(t_out, xs, color="red")
# plt.plot(t_out, ys, color="green")
# plt.plot(t_out, zs, color="blue")

plt.show()
