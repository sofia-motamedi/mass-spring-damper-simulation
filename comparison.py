import numpy as np
import matplotlib.pyplot as plt

# System parameters
m = 1.0        # mass (kg)
c = 0.2        # damping coefficient (Ns/m)
k = 2.0        # spring constant (N/m)
dt = 0.01      # time step (seconds)
T = 10.0       # total simulation time (seconds)

# Time vector from 0 to T with step dt
t = np.arange(0, T + dt, dt)
N = len(t)

# Define the external force function
def F(time):
    return np.sin(2 * np.pi * time)

# arrays for displacement (x) and velocity (v) for each method

# Euler method
x_euler = np.zeros(N)
v_euler = np.zeros(N)

# Predictor-Corrector method
x_pc = np.zeros(N)
v_pc = np.zeros(N)

# Heun's method
x_heun = np.zeros(N)
v_heun = np.zeros(N)

# Runge-Kutta 4th Order method
x_rk4 = np.zeros(N)
v_rk4 = np.zeros(N)

# initial conditions
x_euler[0] = v_euler[0] = 0.0
x_pc[0] = v_pc[0] = 0.0
x_heun[0] = v_heun[0] = 0.0
x_rk4[0] = v_rk4[0] = 0.0

# Euler Method
for i in range(N - 1):
    x_euler[i+1] = x_euler[i] + dt * v_euler[i]
    v_euler[i+1] = v_euler[i] + dt * (F(t[i]) - c * v_euler[i] - k * x_euler[i])

# Predictor-Corrector Method
for i in range(N - 1):
    x_pred = x_pc[i] + dt * v_pc[i]
    v_pred = v_pc[i] + dt * (F(t[i]) - c * v_pc[i] - k * x_pc[i])
    x_pc[i+1] = x_pc[i] + 0.5 * dt * (v_pc[i] + v_pred)
    v_pc[i+1] = v_pc[i] + 0.5 * dt * ((F(t[i]) - c * v_pc[i] - k * x_pc[i]) + (F(t[i+1]) - c * v_pred - k * x_pred))

# Heun's Method
for i in range(N - 1):
    a_current = F(t[i]) - c * v_heun[i] - k * x_heun[i]
    x_predict = x_heun[i] + dt * v_heun[i]
    v_predict = v_heun[i] + dt * a_current
    a_predict = F(t[i+1]) - c * v_predict - k * x_predict
    x_heun[i+1] = x_heun[i] + 0.5 * dt * (v_heun[i] + v_predict)
    v_heun[i+1] = v_heun[i] + 0.5 * dt * (a_current + a_predict)

# Runge-Kutta 4th Order Method
for i in range(N - 1):
    current_t = t[i]
    current_x = x_rk4[i]
    current_v = v_rk4[i]
    
    s1_x = dt * current_v
    s1_v = dt * (F(current_t) - c * current_v - k * current_x)
    
    s2_x = dt * (current_v + 0.5 * s1_v)
    s2_v = dt * (F(current_t + 0.5 * dt) - c * (current_v + 0.5 * s1_v) - k * (current_x + 0.5 * s1_x))
    
    s3_x = dt * (current_v + 0.5 * s2_v)
    s3_v = dt * (F(current_t + 0.5 * dt) - c * (current_v + 0.5 * s2_v) - k * (current_x + 0.5 * s2_x))
    
    s4_x = dt * (current_v + s3_v)
    s4_v = dt * (F(current_t + dt) - c * (current_v + s3_v) - k * (current_x + s3_x))
    
    x_rk4[i+1] = current_x + (s1_x + 2*s2_x + 2*s3_x + s4_x) / 6
    v_rk4[i+1] = current_v + (s1_v + 2*s2_v + 2*s3_v + s4_v) / 6

# Plotting the Results: Comparison of Displacement x(t)
plt.figure(figsize=(12, 6))
plt.plot(t, x_euler, label="Euler", linestyle='-', color='blue')
plt.plot(t, x_pc, label="Predictor-Corrector", linestyle='--', color='red')
plt.plot(t, x_heun, label="Heun", linestyle='-.', color='green')
plt.plot(t, x_rk4, label="RK4", linestyle=':', color='black')
plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t) (m)")
plt.title("Displacement Comparison for Numerical Methods")
plt.legend()
plt.grid(True)
plt.show()

# Plotting the Results: Comparison of Velocity v(t)
plt.figure(figsize=(12, 6))
plt.plot(t, v_euler, label="Euler", linestyle='-', color='blue')
plt.plot(t, v_pc, label="Predictor-Corrector", linestyle='--', color='red')
plt.plot(t, v_heun, label="Heun", linestyle='-.', color='green')
plt.plot(t, v_rk4, label="RK4", linestyle=':', color='black')
plt.xlabel("Time (s)")
plt.ylabel("Velocity v(t) (m/s)")
plt.title("Velocity Comparison for Numerical Methods")
plt.legend()
plt.grid(True)
plt.show()
