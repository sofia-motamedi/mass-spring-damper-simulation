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

# Solve the system using the Predictor-Corrector method
for i in range(len(t) - 1):
    # Predictor step: use Euler method to compute a preliminary (predicted) state
    F = np.sin(2 * np.pi * t[i])
    x_predicted = x[i] + dt * v[i]
    v_predicted = v[i] + dt * (F - c * v[i] - k * x[i])

    # Compute acceleration at current step (a_current) and at predicted step (a_predicted)
    a_current = F - c * v[i] - k * x[i]
    F_next = np.sin(2 * np.pi * t[i+1])
    a_predicted = F_next - c * v_predicted - k * x_predicted

    x[i+1] = x[i] + (dt/2) * (v[i] + v_predicted)
    v[i+1] = v[i] + (dt/2) * (a_current + a_predicted)

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
plt.title("Dynamic Response of the Mass-Spring-Damper System (Predictor-Corrector)")
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
