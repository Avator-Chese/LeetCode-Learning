import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def f(x, y):
    return - x * y ** 2


def rk4(h, x, y):
    k1 = f(x, y)
    k2 = f(x + h * x / 2, y + k1 * h / 2)
    k3 = f(x + h * x / 2, y + k2 * h / 2)
    k4 = f(x + h * x, y + k3 * h)
    return h * (k1 + 1 / 2 * k2 + 1 / 2 * k3 + k4) / 6


x = np.arange(0, 5, 0.25)
y = np.zeros(len(x))
y[0] = 2
h = 0.25

for i in range(len(x)):
    if i + 1 < len(x):
        y[i + 1] = y[i] + rk4(h, i, y[i])
    else:
        break


plt.plot(x, y)
plt.show()
