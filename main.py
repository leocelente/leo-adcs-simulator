import numpy as np
import Visualization as Viz
from Simulator import Simulate
from Orbit import *

print("Start of Simulation")

state = np.vstack(
    [position_0, velocity_0, attitude_0, omega_0])
number_of_orbits: float = .3
data, time = Simulate(number_of_orbits, state, status=Viz.status, timestep=1)

print("End of Simulation")

data = np.array(data)


np.savetxt("state.csv", data, delimiter=",")

Viz.View(data, time)
