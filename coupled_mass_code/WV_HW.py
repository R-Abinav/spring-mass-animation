import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
R = 1  # Radius of the circle
num_masses = 4
k = 1  # Spring constant
m = 1  # Mass

# Initial conditions for the modes
mode1 = np.array([1, 1, -1, -1])
mode2 = np.array([1, 1, 1, 1])
mode3 = np.array([1, 1/np.sqrt(2), 1, np.sqrt(2)])

# Define the differential equations for the motion of the masses
def equations(t, y, mode):
    dydt = np.zeros_like(y)
    for i in range(num_masses):
        if i == 0:
            dydt[i] = (y[num_masses-1] - 2*y[i] + y[i+1]) * k / m
        elif i == num_masses-1:
            dydt[i] = (y[i-1] - 2*y[i] + y[0]) * k / m
        else:
            dydt[i] = (y[i-1] - 2*y[i] + y[i+1]) * k / m
    return dydt

# Simulate the motion for each mode
def simulate_motion(mode):
    initial_conditions = np.zeros(2 * num_masses)
    initial_conditions[::2] = mode * R  # Set initial positions based on mode
    initial_conditions[1::2] = np.zeros(num_masses)  # Initial velocities are zero

    # Solve the differential equations
    t_span = (0, 10)  # Simulation time span
    sol = solve_ivp(equations, t_span, initial_conditions, args=(mode,))

    # Convert cartesian coordinates to polar coordinates
    x = sol.y[::2]
    y = sol.y[1::2]
    theta = np.arctan2(y, x)

    # Plot the locus
    plt.figure()
    plt.plot(R * np.cos(theta), R * np.sin(theta))
    plt.title(f'Locus of masses with mode: {mode}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Simulate motion for each mode
simulate_motion(mode1)
simulate_motion(mode2)
simulate_motion(mode3)
