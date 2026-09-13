import numpy as np
import matplotlib.pyplot as plt

# System parameters
m = 1.0        # mass (kg)
c = 0.2        # damping coefficient (Ns/m)
k = 2.0        # spring constant (N/m)
dt = 0.01      # time step (seconds)
T = 10.0       # total simulation time (seconds)

# time vector from 0 to T with step dt
t = np.arange(0, T + dt, dt)

# Initializing arrays
x = np.zeros(len(t))
v = np.zeros(len(t))

# Initial conditions
x[0] = 0.0     # initial displacement (meters)
v[0] = 0.0     # initial velocity (m/s)

# Solve the differential equation using the Euler method
for i in range(len(t) - 1):
    F = np.sin(2 * np.pi * t[i])

    x[i + 1] = x[i] + dt * v[i]
    v[i + 1] = v[i] + dt * (F - c * v[i] - k * x[i])

# Print the results every 100th iteration
print("{:>8} {:>15} {:>15}".format("Time", "Displacement", "Velocity"))
for i in range(0, len(t), 100):
    print("{:8.0f} {:15.4f} {:15.4f}".format(t[i], x[i], v[i]))

# Plot the displacement and velocity as functions of time
plt.figure(figsize=(10, 6))

# Plotting displacement x(t)
plt.subplot(2, 1, 1)
plt.plot(t, x, label="Displacement x(t)")
plt.xlabel("Time (seconds)")
plt.ylabel("Displacement (meters)")
plt.title("Dynamic Response of Mass-Spring-Damper System (Euler Method)")
plt.grid(True)
plt.legend()

# Plotting velocity v(t)
plt.subplot(2, 1, 2)
plt.plot(t, v, color='orange', label="Velocity v(t)")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
