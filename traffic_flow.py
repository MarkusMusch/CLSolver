"""Traffic flow equation with periodic boundary conditions."""

import matplotlib.pyplot as plt
import numpy as np

from src.flux_collection import laxFriedrichs, trafficFlow
from src.solver import solve

numCells=1000
leftBoundary = 0.0
rightBoundary = 1.0
dx = (rightBoundary-leftBoundary)/numCells

dt = 1e-4
endTime = 1.

# Define the initial data for your equation here
def initial_data(x: np.array) -> np.array:
    return np.where((0 <= x) & (x <= 1), 1*(1-x), 0.)

def exact_solution(x: float, t: float) -> float:
    return initial_data(x-t)

x = np.linspace(leftBoundary, rightBoundary, numCells+1)

u = np.vectorize(initial_data)(x)
u[0] = u[-1]
l1_error, u = solve(u, x, endTime, dt, dx, numCells, exact_solution, trafficFlow, laxFriedrichs)

plt.plot(l1_error)
plt.show()

plt.plot(x, u, label="Numerical")
plt.plot(x, exact_solution(x, endTime), label="Exact")
plt.show()
