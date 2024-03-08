import matplotlib.pyplot as plt
import numpy as np

def thom_attractor(b, start_position, num_steps, dt):
    """
    Generate points for Thom's attractor.

    Parameters:
        b (float): The parameter controlling the behavior of the attractor.
        start_position (numpy.ndarray): The initial position of the attractor in 3D space.
        num_steps (int): The number of steps to compute.
        dt (float): The time step for each iteration.

    Returns:
        numpy.ndarray: Array of 3D points representing Thom's attractor trajectory.
    """
    # Initialize array to store positions
    positions = np.zeros((num_steps, 3))
    positions[0] = start_position  # Set the initial position

    # Iterate to generate positions
    for step in range(1, num_steps):
        current_state = positions[step - 1]  # Get the current state
        # Compute the next state using the Thom attractor equations
        dx = -b * current_state[0] + np.sin(current_state[1])
        dy = -b * current_state[1] + np.sin(current_state[2])
        dz = -b * current_state[2] + np.sin(current_state[0])

        positions[step] = current_state + np.array([dx, dy, dz]) * dt  # Update the position

    return positions  # Return the computed positions


# Set parameters for Thom's attractor
b = 0.2
start_position = np.array([0.1, 0.0, 0.0])  # Initial position
num_steps = 100000  # Number of steps to compute
dt = 0.01  # Time step for each iteration

# Set the view parameters (elevation, azimuth, roll)
elevation = 0  # Set your desired elevation angle
azimuth = -90  # Set your desired azimuth angle
roll = 0  # Set your desired roll angle

# Generate Thom's attractor points
thom_points = thom_attractor(b, start_position, num_steps, dt)

# Visualization
ax = plt.figure().add_subplot(111, projection='3d')  # Create a 3D subplot
ax.set_axis_off()  # Turn off the axes

# Plot the Thom attractor trajectory
ax.plot(thom_points[:, 0], thom_points[:, 1], thom_points[:, 2], color='black', lw=0.08)

# Set the viewing angle
ax.view_init(elev=elevation, azim=azimuth)
ax.dist = 8  # Set the distance from the plot

# Optionally, save the plot as an image file
# plt.savefig("thom_attractor.png", dpi=1200)  # Save the plot as a PNG file with high resolution

# Display the plot
plt.show()
