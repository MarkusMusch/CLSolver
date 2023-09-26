"""Main entry point for the application."""

import matplotlib.pyplot as plt
import numpy as np

numCells=1000
leftBoundary = 0.0
rightBoundary = 1.0
dx = (rightBoundary-leftBoundary)/numCells

dt = 1e-4
endTime = 1.0

# Define the fluxes on the edges and nodes here
def linearAdvection(x: float) -> float:
    return x

# Define the numerical flux here
def upwindFlux(leftCellAverage: float, flux: callable) -> float:
    return flux(leftCellAverage)

# Define the initial data for your equation here
def initialData(x: float) -> float:
    return np.cos(x*2*np.pi)

def exactSolution(x: float, t: float) -> float:
    return initialData(x-t)

x = np.linspace(leftBoundary, rightBoundary, numCells+1)
# Use vectorize to make sure that the function works on numpy arrays
# even if the return value doesn't depend on the input
u = np.vectorize(initialData)(x)
u[0] = u[-1]
u_new = np.zeros(numCells+1)
l1_error = []

for i in range(int(endTime/dt)):
    flux = upwindFlux(u, linearAdvection)
    u_new = u - (dt/dx)*(flux - np.roll(flux, 1))
    u_new[0] = u_new[-1]

    u = u_new
    l1_error.append(np.sum(np.abs(u - exactSolution(x, (i+1)*dt)))*dx)

plt.plot(l1_error)
plt.show()

plt.plot(x, u, label="Numerical")
plt.plot(x, exactSolution(x, endTime), label="Exact")
plt.show()
