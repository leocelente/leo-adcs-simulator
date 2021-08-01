from typing import Callable
import numpy as np


def RK4(model: Callable[[float, list[float]], list[float]], state_prev: list[float], t_now: float, t_step: float):
    '''
    Range-Kutta 4\nIntegra o estado `state_prev` pelo modelo `model`
    no passo `t_now` até o passo `t_now + t_step`
    '''
    assert(state_prev.shape == (13, 1))
    state_prev = np.ravel(state_prev)
    state_prev = np.reshape(state_prev, (13, 1))

    k1: list[float] = model(t_now, state_prev)
    k2: list[float] = model(t_now+t_step/2., state_prev + (k1 * t_step/2.))
    k3: list[float] = model(t_now+t_step/2., state_prev + (k2 * t_step/2.))
    k4: list[float] = model(t_now+t_step, state_prev + k3 * t_step)
    k: list[float] = (1/6)*(k1 + 2*k2 + 2*k3 + k4)

    delta_state: list[float] = (k * t_step)
    state_next:  list[float] = state_prev + delta_state

    return state_next
