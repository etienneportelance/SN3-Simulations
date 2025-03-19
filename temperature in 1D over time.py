import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0          # Length of the wall (meters)
T_left = 100.0   # Temperature at the left boundary (°C)
T_right = 0.0    # Temperature at the right boundary (°C)
alpha = 1e-4     # Thermal diffusivity (m^2/s)
nx = 100         # Number of spatial grid points
nt = 3000        # Number of time steps
dx = L / (nx - 1)  # Spatial step size
dt = 0.5 * dx**2 / alpha  # Time step size (chosen for stability)
G_steps = 100   # A line in the graph is produced once every G_steps

# Initialize temperature array
T = np.zeros(nx)
T[0] = T_left    # Left boundary condition
T[-1] = T_right  # Right boundary condition


# Create a grid for visualization
x = np.linspace(0, L, nx)

# Set up the plot
plt.figure(figsize=(10, 6))
plt.xlabel('Position (m)')
plt.ylabel('Temperature (°C)')
plt.title('1D Temperature Distribution in a Wall Over Time')

# Time-stepping loop
for t in range(nt):
    # Create a copy of the temperature array to avoid overwriting
    T_new = T.copy()
    
    
    # Update temperature using the finite difference method
    for i in range(1, nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i+1] - 2*T[i] + T[i-1])
    
    # Update the temperature array
    T = T_new
    
    # Plot every 100 time steps
    if t % 100 == 0:
        plt.plot(x, T, label=f'Time = {t * dt:.2f} s')


# Add legend and show the plot
plt.legend()
plt.grid()
plt.show()