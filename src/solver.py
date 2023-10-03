"""Contains the solver function for 1D hyperbolic conservation laws."""

import numpy as np

# Use vectorize to make sure that the function works on numpy arrays
# even if the return value doesn't depend on the input
def solve(u: np.ndarray, x: np.ndarray, endTime: float, dt: float, dx: float,
          numCells: int, exactSolution: callable, analytical_flux: callable,
          numerical_flux: callable) -> np.ndarray:
    u_new = np.zeros(numCells+1)
    l1_error = []

    for i in range(int(endTime/dt)):
        flux = numerical_flux(u, analytical_flux)
        u_new = u - (dt/dx)*(flux - np.roll(flux, 1))
        u_new[0] = u_new[-1]

        u = u_new
        l1_error.append(np.sum(np.abs(u - exactSolution(x, (i+1)*dt)))*dx)

    return l1_error, u
