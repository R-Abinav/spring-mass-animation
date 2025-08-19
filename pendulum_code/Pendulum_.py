import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the position of a simple pendulum given the angle and length
def simple_pendulum(theta, length):
    x = length * np.sin(theta)
    y = -length * np.cos(theta)
    return x, y

# Constants
length = 1.0  # Length of the pendulum (in meters)
omega = np.sqrt(9.81 / length)  # Angular frequency for SHM

# Time array
t = np.linspace(0, 10, 1000)

# Function to calculate angle as a function of time for SHM
def angle(t):
    return np.pi / 4 * np.cos(omega * t)

# Generate data
x, y = simple_pendulum(angle(t), length)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.scatter([x[0], x[-1]], [y[0], y[-1]], color='red')  # Mark start and end points
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trajectory of Simple Pendulum')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
