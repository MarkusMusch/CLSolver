""" This file contains the analytical and numerical fluxes used in the
    finite volume method. The analytical fluxes are used to compute the
    exact solution of the Riemann problem. The numerical fluxes are used
    to compute the approximate solution of the Riemann problem.
"""

import numpy as np
from scipy import integrate

# Define the analytical fluxes here

def linearAdvection(u: np.array, capacity: float=1.) -> np.array:
    """ This function returns the value of the linear advection flux"""
    return capacity * u

def monotoneQuadratic(u: np.array, capacity: float=1.) -> np.array:
    """ This function returns the value of the monotone quadratic flux"""
    return np.where(u > 0, u*u/(2.*capacity), 0.)

def positiveBurgers(u: np.array, capacity: float=1.) -> np.array:
    """ This function returns the value of the positive Burgers flux"""
    return np.where(u > 0, u*u/(2.*capacity), 0.)

def trafficFlow(u: np.array, capacity: float=1.) -> np.array:
    """ This function returns the value of the traffic flow flux"""
    return np.where(u > 0, u*(1.-u/capacity), 0.)

def holdenRisebroFlow(u: np.array, capacity: float=1.) -> np.array:
    """ This function returns the value of the Holden-Risebro flow flux"""
    return np.where(u > 0, 4*u*(1.-u/capacity), 0.)

# Define the numerical fluxes here  

def upwindFlux(u: np.array, flux: callable, capacity: float=1.) -> np.array:
    """ This function returns the value of the upwind flux"""
    return flux(u, capacity)

def downwindFlux(u: float, flux: callable, capacity: float=1.) -> np.array:
    """ This function returns the value of the downwind flux"""
    return flux(u, capacity)

def concaveGodunov(u: np.array, flux: callable, capacity: float=1.) -> np.array:
    """ This function returns the value of the concave Godunov flux"""
    return np.minimum(flux(np.minimum(u, capacity/2.), capacity), flux(np.maximum(np.roll(u, -1), capacity/2.), capacity))

def laxFriedrichs(u: np.array, flux: callable, capacity: float=1., dx: float=1., dt: float=1.) -> np.array:
    """ This function returns the value of the Lax-Friedrichs flux"""
    return 0.5*(dx/dt)*(u - np.roll(u, -1)) + 0.5*(flux(u, capacity) + flux(np.roll(u, -1), capacity))
