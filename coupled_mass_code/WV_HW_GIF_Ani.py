import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
R = 1  # Radius of the circle
num_masses = 4
k = 0.1  # Spring constant
m = 1  # Mass
omega = 1  # Angular frequency
amplitude = 0.2  # Amplitude of oscillation

# Initial positions of the masses on the circle
theta = np.linspace(0, 2 * np.pi, num_masses, endpoint=False)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)

# Initialize empty list to hold line objects for the masses
masses, = ax.plot([], [], 'bo', markersize=10)

# Function to update the animation
def update(frame):
    # Calculate the new positions of the masses
    x = R * np.cos(theta) + amplitude * np.cos(omega * frame) * np.sin(theta)
    y = R * np.sin(theta) + amplitude * np.sin(omega * frame) * np.cos(theta)

    # Update the positions of the masses
    masses.set_data(x, y)
    return masses,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100),
                    blit=True, interval=50)

# Save the animation as a GIF
ani.save('spring_mass_animation.gif', writer='pillow', fps=20)

plt.title('Spring-Mass System Animation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
