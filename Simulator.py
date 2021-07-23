from Integrator import RK4
from Orbit import *
import Satellite


def s(progress):
    ''' Change this parameter to print the progress
    '''
    pass


def Simulate(number_of_orbits, state, status=s, timestep=1):
    tfinal: float = period * number_of_orbits
    time = np.arange(0.0, tfinal, timestep, dtype=float)

    view_state = []
    for i in range(len(time)):
        status(i/len(time))
        state = RK4(Satellite.Model, state, time[i], timestep)
        view_state.append(state[:, 0])
    return view_state, time
