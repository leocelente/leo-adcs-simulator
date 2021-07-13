import numpy as np


def RK4(model, state_prev, t_now: float, t_step: float):
    state_prev = np.ravel(state_prev)
    k1 = model(t_now, state_prev)
    k2 = model(t_now+t_step/2, state_prev + k1 * t_step/2)
    k3 = model(t_now+t_step/2, state_prev + k2 * t_step/2)
    k4 = model(t_now+t_step, state_prev + k3 * t_step)
    k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    delta_state = (k * t_step)
    state_next = state_prev + delta_state
    return state_next
