import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def decision_boundary():
    N = 500
    x = np.linspace(-10.0, 10.0, N)
    y = np.linspace(-10.0, 10.0, N)

    X, Y = np.meshgrid(x, y)

    # The discrimant function of each class of Generative Models
    z1 = -X + Y
    z2 = X + Y - 1
    z3 = -Y

    z = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if z1[i, j] > z2[i, j] and z1[i, j] > z3[i, j]:
                z[i, j] = 1
            elif z2[i, j] > z1[i, j] and z2[i, j] > z3[i, j]:
                z[i, j] = 0
            elif z3[i, j] > z1[i, j] and z3[i, j] > z2[i, j]:
                z[i, j] = -1
            else:
                z[i, j] = -2

    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
    plt.contourf(x, y, z, linewidth=5, cmap=custom_cmap)
    plt.text(-5, 5, r'$\omega_1$', fontsize=15)
    plt.text(5, 5, r'$\omega_2$', fontsize=15)
    plt.text(0, -5, r'$\omega_3$', fontsize=15)
    plt.savefig('example.pdf', format='pdf', dpi=1000)
    plt.show()


if __name__ == '__main__':
    decision_boundary()