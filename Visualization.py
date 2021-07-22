import numpy as np
from matplotlib import figure, pyplot as plt
from Earth import R


def Earth(state):
    fig = figure.Figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot3D(state[:, 0]*1e-3,
              state[:, 1]*1e-3,
              state[:, 2]*1e-3, 'red')

    u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:20j]
    x = R*1e-3*np.cos(u)*np.sin(v)
    y = R*1e-3*np.sin(u)*np.sin(v)
    z = R*1e-3*np.cos(v)
    ax.plot_wireframe(x, y, z, color="lightblue", alpha=0.8)
    fig.legend(['Orbit'])
    # ax.xlim()
    # fig.title.set_text("LEO Orbit")
    # Skipping a lot of other complexity her
    f, ax = plt.subplots()
    ax.plot(x, y)
    # further stuff
    return ax

    return ax


def Attitude(state, time):
    plt.subplot(2, 2, 2)
    plt.plot(time, state[:, 6:10])
    plt.legend(["q0", "q1", "q2", "q3"])
    plt.title("Attitudes")
    plt.grid()


def Omega(state, time):
    plt.subplot(2, 2, 3)
    plt.plot(time, state[:, 10:13])
    plt.legend(["p", "q", "r"])
    plt.title("Angular Velocities")
    plt.grid()


def MagneticField(state, time):
    plt.subplot(2, 2, 4)
    plt.plot(time, state[:, 13:16])
    plt.legend(["B_x", "B_y", "B_z"])
    plt.title("Magnetic Field")
    plt.grid()


def View(plots):
    cols = len(plots)/2
    rows = len(plots) - cols
    fig, axs = plt.subplots(rows, cols)
