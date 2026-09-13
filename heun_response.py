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

# initial conditions
x[0] = 0.0     # initial displacement (meters)
v[0] = 0.0     # initial velocity (m/s)

# Solve the differential equations using the Heun method:
for i in range(len(t) - 1):
    # Compute s1 for both x and v
    s1_x = dt * v[i]
    s1_v = dt * (np.sin(2 * np.pi * t[i]) - c * v[i] - k * x[i])

    # Compute s2 using s1
    s2_x = dt * (v[i] + s1_v)
    s2_v = dt * (np.sin(2 * np.pi * (t[i] + dt)) - c * (v[i] + s1_v) - k * (x[i] + s1_x))

    # Update the state using the s1 and s2 values
    x[i+1] = x[i] + 0.5 * (s1_x + s2_x)
    v[i+1] = v[i] + 0.5 * (s1_v + s2_v)

# Print the results every 100th iteration
print("{:>8} {:>15} {:>15}".format("Time", "Displacement", "Velocity"))
for i in range(0, len(t), 100):
    print("{:8.0f} {:15.4f} {:15.4f}".format(t[i], x[i], v[i]))

# Plot the displacement and velocity as functions of time
plt.figure(figsize=(10, 6))

# Plotting displacement x(t)
plt.subplot(2, 1, 1)
plt.plot(t, x, label="Displacement x(t)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Mass-Spring-Damper System Response (Heun Method)")
plt.grid(True)
plt.legend()

# Plotting velocity v(t)
plt.subplot(2, 1, 2)
plt.plot(t, v, color='orange', label="Velocity v(t)")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
