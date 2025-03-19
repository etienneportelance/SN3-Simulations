import numpy as np
import matplotlib.pyplot as plt

# Configure matplotlib to use a non-interactive backend
plt.switch_backend('TkAgg')  # or 'Qt5Agg' if you have PyQt5 installed

# Parameters
L = 1.0          # Length of the wall (meters)
T_left = 100.0   # Temperature at the left boundary (°C)
T_right = 0.0    # Temperature at the right boundary (°C)
alpha = 1e-4     # Thermal diffusivity (m^2/s)
k = 50.0         # Thermal conductivity (W/m·K)
A = 1.0          # Cross-sectional area (m²)
nx = 100         # Number of spatial grid points
nt = 3000        # Number of time steps
dx = L / (nx - 1)  # Spatial step size
dt = 0.5 * dx**2 / alpha  # Time step size (chosen for stability)

# Initialize temperature array
T = np.zeros(nx)
T[0] = T_left    # Left boundary condition
T[-1] = T_right  # Right boundary condition

# Initialize arrays for power and time
P_left = np.zeros(nt)
P_right = np.zeros(nt)
Times = np.zeros(nt)

# Time-stepping loop
for t in range(nt):
    # Create a copy of the temperature array to avoid overwriting
    T_new = T.copy()
    
    # Update temperature using the finite difference method
    for i in range(1, nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i+1] - 2*T[i] + T[i-1])
    
    # Update the temperature array
    T = T_new
    
    # Calculate and store power at every time step
    P_left[t] = -k * A * (T[1] - T[0]) / dx
    P_right[t] = -k * A * (T[-1] - T[-2]) / dx
    Times[t] = t * dt

# Set up the plot
plt.figure(figsize=(10, 6))
plt.plot(Times, P_left, label='Left Boundary Power')
plt.plot(Times, P_right, label='Right Boundary Power')
plt.xlabel('Time (s)')
plt.ylabel('Power (W)')
plt.title('Power at Boundaries Over Time')
plt.legend()
plt.grid()
plt.show()