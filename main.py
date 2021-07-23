import Visualization as Viz
from Simulator import Simulate
from Orbit import *
from matplotlib import pyplot as plt
from Earth import R

BB = np.array([[0, 0, 0]], dtype=float).T

state = np.vstack(
    [position_0, velocity_0, attitude_0, omega_0, BB])

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

data = np.array(data)


np.savetxt("state.csv", data, delimiter=",")

Viz.View(data, time)
