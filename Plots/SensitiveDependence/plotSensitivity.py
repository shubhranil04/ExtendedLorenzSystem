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
IC_1 = np.array([1, 5, 10])  # Initial condition

dir = [0,0,1] #np.random.randn(3) 
dir /= np.linalg.norm(dir)  # Normalize the direction
IC_2 = IC_1 + 1e-9*dir # Perturbed initial condition

t = np.linspace(0, 100, 10000)  # Time points

# Integrate the Lorenz system
from scipy.integrate import solve_ivp
sol_1 = solve_ivp(lorenz_system, [t[0], t[-1]], IC_1, method='DOP853', t_eval=t, args=(rho,), rtol=1e-10, atol=1e-10)
sol_2 = solve_ivp(lorenz_system, [t[0], t[-1]], IC_2, method='DOP853', t_eval=t, args=(rho,), rtol=1e-10, atol=1e-10)

# Plot time series
# Plot time series
fig, ax = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
ax[0].plot(t, sol_1.y[0], lw=1.5, color='blue')
ax[0].plot(t, sol_2.y[0], lw=1.5, color='red')
ax[0].set_ylabel('X', fontsize=16)
ax[0].set_xlim([t[0], t[-1]])
ax[0].set_ylim([-25, 25])
ax[0].tick_params(axis='both', which='major', labelsize=14)
ax[1].plot(t, sol_1.y[1], lw=1.5, color='blue')
ax[1].plot(t, sol_2.y[1], lw=1.5, color='red')
ax[1].set_ylabel('Y', fontsize=16)
ax[1].set_xlim([t[0], t[-1]])
ax[1].set_ylim([-25, 25])
ax[1].tick_params(axis='both', which='major', labelsize=14)
ax[2].plot(t, sol_1.y[2], lw=1.5, color='blue')
ax[2].plot(t, sol_2.y[2], lw=1.5, color='red')
ax[2].set_ylabel('Z', fontsize=16)
ax[2].set_xlabel('Time', fontsize=16)
ax[2].set_xlim([t[0], t[-1]])
ax[2].set_ylim([0, 50])
ax[2].tick_params(axis='both', which='major', labelsize=14)
plt.savefig(f'sensitivity_{rho:.2f}.png', dpi=600,bbox_inches='tight')
plt.show()

# Plot separation

delta = np.linalg.norm(sol_1.y - sol_2.y, axis=0)

from scipy.stats import linregress
mask = (t < 25) & (t > 5)
t_fit = t[mask]
delta_fit = delta[mask]
slope, intercept, r_value, p_value, std_err = linregress(t_fit, np.log(delta_fit))

print(f'Slope: {slope}, Intercept: {intercept}, R-squared: {r_value**2}')

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(t, delta, lw=1.5, color='blue')
ax.plot(t, np.exp(intercept + slope * t), color='black', linewidth=1.5, linestyle='--', label=fr'$\delta(t) \sim e^{{{slope:.2f}t}}$')
ax.tick_params(axis='both', which='major', labelsize=14)
ax.set_ylabel(r'Separation ($\delta$)', fontsize=16)
ax.set_xlabel('Time', fontsize=16)
ax.set_xlim([t[0], 40])
ax.set_ylim([1e-10, 1e3])
ax.set_yscale('log')
ax.legend(fontsize=14)

plt.savefig(f'separation_{rho:.2f}.png', dpi=600,bbox_inches='tight')
plt.show()
