# Numerical Simulation and Comparative Analysis of a Mass-Spring-Damper System

## Overview
This project investigates the dynamic response of a single-degree-of-freedom mass-spring-damper system subjected to an external harmonic force. The physical system is modeled using a second-order ordinary differential equation (ODE), which is then converted into a system of first-order ODEs and solved using both analytical and numerical techniques in Python.

<img src="figures/system_diagram.png" width="600">
---

## Mathematical Modeling

The equation of motion for the system is given by[span_4](start_span)[span_4](end_span):

$$m \frac{d^2x}{dt^2} + c \frac{dx}{dt} + k x(t) = F(t)$$

Where:
* $m = 1.0 \text{ kg}$ is the mass[span_5](start_span)[span_5](end_span).
* $c = 0.2 \text{ Ns/m}$ is the damping coefficient[span_6](start_span)[span_6](end_span).
* $k = 2.0 \text{ N/m}$ is the spring constant[span_7](start_span)[span_7](end_span).
* $F(t) = \sin(2\pi t)$ is the external harmonic excitation force[span_8](start_span)[span_8](end_span).
* $x(t)$ is the displacement of the mass relative to its equilibrium position[span_9](start_span)[span_9](end_span).

To solve this numerically, the second-order equation is reduced to a system of two first-order differential equations by defining velocity $v(t) = \frac{dx}{dt}$[span_10](start_span)[span_10](end_span):

$$\begin{cases}
\frac{dx}{dt} = v(t) \\
\frac{dv}{dt} = \frac{1}{m} \left[ F(t) - c v(t) - k x(t) \right] = \sin(2\pi t) - 0.2 v(t) - 2 x(t)
\end{cases}$$

Initial conditions are set to $x(0) = 0 \text{ m}$ and $v(0) = 0 \text{ m/s}$ over a time span of $T = 10 \text{ s}$ with a time step of $\Delta t = 0.01 \text{ s}$[span_11](start_span)[span_11](end_span).

---

## Analytical Solution
The analytical solution combines the homogeneous solution ($x_h(t)$) of the damped oscillator and the particular solution ($x_p(t)$) driven by the harmonic forcing function using the method of undetermined coefficients[span_12](start_span)[span_12](end_span):

$$x(t) = e^{-0.1t} \left[ 0.0008928 \cos(1.411t) + 0.11896 \sin(1.411t) \right] - 0.02664 \sin(2\pi t) - 0.0008928 \cos(2\pi t)$$

---

## Numerical Methods Implemented
Four distinct numerical integration schemes were implemented in Python using NumPy and Matplotlib:

1. Euler Method: A first-order explicit method that uses current slopes to advance the solution[span_13](start_span)[span_13](end_span). Simple to implement but prone to cumulative error and instability in oscillatory systems[span_14](start_span)[span_14](end_span).
2. Predictor-Corrector Method: Improves accuracy by predicting a tentative next state using the Euler step and then correcting it using averaged derivatives[span_15](start_span)[span_15](end_span).
3. Heun's Method (Modified Euler): A second-order Runge-Kutta method that averages the initial and predicted slopes to achieve higher stability and accuracy[span_16](start_span)[span_16](end_span).
4. 4th Order Runge-Kutta (RK4): Evaluates four increment stages per time step to provide high-order accuracy ($\mathcal{O}(\Delta t^4)$), making it ideal for sensitive or highly oscillatory dynamical systems[span_17](start_span)[span_17](end_span).

---

## Results and Visualizations

### 1. Euler Method Response
![Euler Method Response](images/euler_response.png)
*Dynamic response of displacement $x(t)$ and velocity $v(t)$ using the Euler method[span_18](start_span)[span_18](end_span).*

### 2. Predictor-Corrector Method Response
![Predictor-Corrector Response](images/predictor_corrector_response.png)
*Simulation results using the Predictor-Corrector algorithm[span_19](start_span)[span_19](end_span).*

### 3. Heun's Method Response
![Heun Method Response](images/heun_response.png)
*System response calculated via Heun's second-order method[span_20](start_span)[span_20](end_span).*

### 4. 4th Order Runge-Kutta (RK4) Response
![RK4 Method Response](images/rk4_response.png)
*High-precision dynamic response obtained using the RK4 method[span_21](start_span)[span_21](end_span).*
### 5. Comparative Analysis of All Numerical Methods
![Methods Comparison](images/comparison.png)
*Overlay comparison of displacement trajectories across all four numerical solvers[span_22](start_span)[span_22](end_span).*

---

## Conclusion & Key Takeaways
* Simplicity vs. Accuracy: While the Euler method is computationally straightforward, its first-order truncation error accumulates rapidly in oscillatory mechanical systems[span_23](start_span)[span_23](end_span).
* Stability: Heun's and Predictor-Corrector methods offer second-order improvements by incorporating slope corrections, yielding stable trajectories[span_24](start_span)[span_24](end_span).
* High-Precision Engineering: The RK4 method delivers superior accuracy and stability, making it the preferred standard for simulating complex physical dynamics despite its increased computational overhead per step[span_25](start_span)[span_25](end_span).

---

## Requirements
* Python 3.x
* NumPy
* Matplotlib

To run the simulation, execute:
`bash
python main.py
