import numpy as np
import matplotlib.pyplot as plt

def simple_pendulum(theta, length):
    """
    Function to calculate the position of a simple pendulum given the angle and length.
    
    Parameters:
        theta (float or array-like): Angle(s) in radians.
        length (float): Length of the pendulum.
        
    Returns:
        tuple: Tuple containing the x and y coordinates of the pendulum bob.
    """
    x = length * np.sin(theta)
    y = -length * np.cos(theta)
    return x, y

# Constants
length = 1.0  # Length of the pendulum (in meters)
theta = np.linspace(-2*np.pi, 2*np.pi, 1000)  # Range of angles from -2*pi to 2*pi

# Calculate the pendulum position for each angle
x, y = simple_pendulum(theta, length)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Locus of Simple Pendulum')
plt.title('Locus of a Simple Pendulum')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
