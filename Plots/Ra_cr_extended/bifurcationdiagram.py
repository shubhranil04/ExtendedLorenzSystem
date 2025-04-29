import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
b = 8/3

# r and omega ranges
r_vals = np.linspace(0, 2, 300)
omega_vals = np.linspace(0, 2*np.pi, 100)

# Surface for r > 1
r_vals_surface = r_vals[r_vals > 1]
R, Omega = np.meshgrid(r_vals_surface, omega_vals)

sqrt_term = np.sqrt(b*(R-1))
X1 = sqrt_term * np.cos(Omega)
X2 = sqrt_term * np.sin(Omega)

# Line for all r: base state at (X1, X2) = (0, 0)
X1_line = np.zeros_like(r_vals)
X2_line = np.zeros_like(r_vals)
R_line = r_vals  # plot against r

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot wireframe surface
ax.plot_wireframe(X1, X2, R, color='black', linewidth=0.8)

# Plot line
ax.plot3D(X1_line, X2_line, R_line, color='black', linewidth=3, label='Base State (X1=X2=0)')

# Labels
ax.set_xlabel(r'$X_1$', fontsize=16)
ax.set_ylabel(r'$X_2$', fontsize=16)
ax.set_zlabel(r'$r$', fontsize=16)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 2])
plt.savefig('extendedbifurcationdiagram.png',dpi=600)
plt.tight_layout()
plt.show()

