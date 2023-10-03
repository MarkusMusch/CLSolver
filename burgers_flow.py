"""Burgers' equation with periodic boundary conditions."""

import matplotlib.pyplot as plt
import numpy as np

from src.flux_collection import positiveBurgers, upwindFlux
from src.solver import solve

numCells=1000
leftBoundary = 0.0
rightBoundary = 1.0
dx = (rightBoundary-leftBoundary)/numCells

dt = 1e-4
endTime = 0.1

# Define the initial data for your equation here
def initial_data(x: np.array) -> np.array:
    return np.where(x < 0.2, 2.0, 1.0)

def exact_solution(x: float, t: float) -> float:
    return np.where(x<t, 1.0,
                    np.where((t <= x) & (x < 2*t), x/t,
                    np.where(x-(3./2.)*t < 0.2, 2.0, 1.0)))

x = np.linspace(leftBoundary, rightBoundary, numCells+1)

u = np.vectorize(initial_data)(x)
#u[0] = u[-1]
plt.plot(x, u , label="Initial")
plt.savefig("./images/initial_data_burgers.png")
plt.show()

l1_error, u = solve(u, x, endTime, dt, dx, numCells, exact_solution, positiveBurgers, upwindFlux)

plt.plot(l1_error)
plt.savefig("./images/l1_error_burgers.png")
plt.show()

plt.plot(x, u, label="Numerical")
plt.plot(x, exact_solution(x, endTime), label="Exact")
plt.savefig("./images/final_time_burgers_flow.png")
plt.show()
