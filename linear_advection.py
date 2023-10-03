"""Linear advection equation example with periodic boundary conditions."""

import matplotlib.pyplot as plt
import numpy as np

from src.flux_collection import linearAdvection, upwindFlux
from src.solver import solve

numCells=1000
leftBoundary = 0.0
rightBoundary = 1.0
dx = (rightBoundary-leftBoundary)/numCells

dt = 1e-4
endTime = 1.

# Define the initial data for your equation here
def initial_data(x: float) -> float:
    return np.cos(x*2*np.pi) + 1.1

def exact_solution(x: float, t: float) -> float:
    return initial_data(x-t)

x = np.linspace(leftBoundary, rightBoundary, numCells+1)

u = np.vectorize(initial_data)(x)
u[0] = u[-1]
plt.plot(x, u , label="Initial")
plt.savefig("./images/initial_data_linear_advection.png")
plt.show()

l1_error, u = solve(u, x, endTime, dt, dx, numCells, exact_solution, linearAdvection, upwindFlux)

plt.plot(l1_error)
plt.savefig("./images/l1_error_linear_advection.png")
plt.show()

plt.plot(x, u, label="Numerical")
plt.plot(x, exact_solution(x, endTime), label="Exact")
plt.savefig("./images/final_time_linear_advection.png")
plt.show()
