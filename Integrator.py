#!/usr/bin/python3

def RK4(model, state_prev, t_now: float, t_step: float):
    k1 = model(t_now, state_prev)
    k2 = model(t_now+t_step/2, state_prev + k1 * t_step/2)
    k3 = model(t_now+t_step/2, state_prev + k2 * t_step/2)
    k4 = model(t_now+t_step, state_prev + k3 * t_step)
    k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    state_next = state_prev + (k * t_step)
    return state_next
