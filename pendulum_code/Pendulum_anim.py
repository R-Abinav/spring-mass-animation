import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 0.5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Simple Pendulum SHM Animation')

# Initialize the line representing the pendulum
line, = ax.plot([], [], lw=2)
bob, = ax.plot([], [], 'o', color='red')  # Pendulum bob

# Function to update the animation
def update(frame):
    # Calculate the angle and position of the pendulum at the current frame
    theta = angle(frame)
    x, y = simple_pendulum(theta, length)
    
    # Update the position of the pendulum line
    line.set_data([0, x], [0, y])
    
    # Update the position of the pendulum bob
    bob.set_data([x], [y])
    
    return line, bob

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=t, blit=True)

# Show the animation
plt.show()
