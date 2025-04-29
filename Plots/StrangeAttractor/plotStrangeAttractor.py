import numpy as np
import matplotlib.pyplot as plt

def lorenz_system(t, state, rho = 28.0):
    """
    Lorenz system of equations.
    """
    x = state[0]
    y = state[1]
    z = state[2]
    # Lorenz parameters
    sigma = 10.0
    beta = 8.0 / 3.0
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt]) 

rho = 28.0  # Lorenz parameter
IC = np.array([1e-9, 0, 10])  # Initial condition
t = np.linspace(0, 100, 10000)  # Time points

# Integrate the Lorenz system
from scipy.integrate import solve_ivp
sol = solve_ivp(lorenz_system, [t[0], t[-1]], IC, method='DOP853', t_eval=t, args=(rho,), rtol=1e-10, atol=1e-10)

# Plotting the Lorenz attractor
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.75, color='blue')
ax.set_xlim([-25, 25])
ax.set_ylim([-25, 25])
ax.set_zlim([0, 50])
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)
ax.set_zlabel('Z', fontsize=14)
plt.grid()

plt.savefig(f'attractor_{rho:.2f}.png', dpi=600)
plt.show()

# Plot time series
fig, ax = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
ax[0].plot(t, sol.y[0], lw=1.5, color='blue')
ax[0].set_ylabel('X', fontsize=16)
ax[0].set_xlim([t[0], t[-1]])
ax[0].set_ylim([-25, 25])
ax[0].tick_params(axis='both', which='major', labelsize=14)
ax[1].plot(t, sol.y[1], lw=1.5, color='blue')
ax[1].set_ylabel('Y', fontsize=16)
ax[1].set_xlim([t[0], t[-1]])
ax[1].set_ylim([-25, 25])
ax[1].tick_params(axis='both', which='major', labelsize=14)
ax[2].plot(t, sol.y[2], lw=1.5, color='blue')
ax[2].set_ylabel('Z', fontsize=16)
ax[2].set_xlabel('Time', fontsize=16)
ax[2].set_xlim([t[0], t[-1]])
ax[2].set_ylim([0, 50])
ax[2].tick_params(axis='both', which='major', labelsize=14)
plt.savefig(f'time_series_{rho:.2f}.png', dpi=600,bbox_inches='tight')
plt.show()

