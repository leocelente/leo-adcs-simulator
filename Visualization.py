import numpy as np
from matplotlib import figure, pyplot as plt
from Earth import R

import sys


def Earth(ax, state):
    ax.plot3D(state[:, 0]*1e-3,
              state[:, 1]*1e-3,
              state[:, 2]*1e-3, 'red', label="Orbit")

    u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:20j]
    x = R*1e-3*np.cos(u)*np.sin(v)
    y = R*1e-3*np.sin(u)*np.sin(v)
    z = R*1e-3*np.cos(v)
    ax.plot_wireframe(x, y, z, color="lightblue", alpha=0.8)
    ax.legend()
    ax.title.set_text("LEO Orbit")
    


def Attitude(ax, state, time):
    ax.plot(time, state[:, 6:10], label=["$q_w$", "$q_x$", "$q_y$", "$q_z$"])
    ax.legend()
    ax.title.set_text("Attitudes")
    ax.grid()


def Omega(ax, state, time):
    ax.plot(time, state[:, 10:13], label=["$\omega_x$", "$\omega_y$", "$\omega_z$"])
    ax.set_ylabel("rad/s")
    ax.legend()
    ax.title.set_text("Angular Velocities")
    ax.grid()


def MagneticField(ax, state, time):
    ax.plot(time, 1e3*state[:, 13:16], label=["$B_x$", "$B_y$", "$B_z$"])
    ax.legend()
    ax.title.set_text("Magnetic Field")
    ax.set_ylabel("mT")
    ax.grid()


def View(state, time):
    fig = plt.figure()
    grid = plt.GridSpec(3,2)
    ax_earth = fig.add_subplot(grid[0:, 0], projection="3d")
    Earth(ax_earth, state)
    ax_att = fig.add_subplot(grid[0, 1])
    Attitude(ax_att, state, time)
    ax_mag = fig.add_subplot(grid[1, 1])
    MagneticField(ax_mag, state, time)
    ax_gyr = fig.add_subplot(grid[2, 1])
    Omega(ax_gyr, state, time)
    plt.show()
    

def status(percent):
    percent = percent*100.0
    sys.stdout.write('Progress: \033[K' + ('%.2f' %  percent) + '%\r')
