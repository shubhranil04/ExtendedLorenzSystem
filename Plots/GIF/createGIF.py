import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


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
IC = np.array([1e-9, 1e-9, 1e-9])  # Initial condition
t = np.linspace(0, 100, 1000)  # Time points

# Integrate the Lorenz system
from scipy.integrate import solve_ivp
sol = solve_ivp(lorenz_system, [t[0], t[-1]], IC, method='DOP853', t_eval=t, args=(rho,), rtol=1e-10, atol=1e-10)

# Define grid
x = np.linspace(-np.sqrt(2), np.sqrt(2), 1000)  # covers two wavelengths in x
z = np.linspace(0, 1, 500)             # z from 0 to 1
X, Z = np.meshgrid(x, z)

Psi = sol.y[0]

# Define stream function psi = sin(kx) * sin(pi z)
k = np.pi / np.sqrt(2)
psi = np.sin(k * X) * np.sin(np.pi * Z)

# Compute velocity field from stream function
dpsi_dz, dpsi_dx = np.gradient(psi, z, x)  # note: order is (z, x)
u = dpsi_dz        # u = ∂ψ/∂z
w = -dpsi_dx       # w = -∂ψ/∂x

print("Creating GIF...")
# Create figure
fig, ax = plt.subplots(figsize=(6, 5))
q = ax.quiver(X, Z, Psi[100]*u, Psi[100]*w,pivot='mid', scale=10)
ax.set_title('Velocity field')
ax.set_xlabel('x')
ax.set_ylabel('z')

plt.show()
'''
def update(frame):
    U = Psi[frame]*u
    W = Psi[frame]*w
    q.set_UVC(U, W) 
    ax.set_title(f"Time step: {frame}")
    return q,

ani = FuncAnimation(fig, update, frames=range(0, len(t), 2), blit=False)
ani.save("velocity_field.gif", writer=PillowWriter(fps=100))
plt.close()
'''