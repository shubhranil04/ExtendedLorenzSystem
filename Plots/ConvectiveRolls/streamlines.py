import numpy as np
import matplotlib.pyplot as plt

# Define grid
x = np.linspace(-np.sqrt(2), np.sqrt(2), 1000)  # covers two wavelengths in x
z = np.linspace(0, 1, 500)             # z from 0 to 1
X, Z = np.meshgrid(x, z)

# Define stream function psi = sin(kx) * sin(pi z)
k = np.pi / np.sqrt(2)
psi = np.sin(k * X) * np.sin(np.pi * Z)
psi_2 = 2*np.sin(k * X) * np.sin(np.pi * Z)

# Compute velocity field from stream function
dpsi_dz, dpsi_dx = np.gradient(psi, z, x)  # note: order is (z, x)
u = dpsi_dz        # u = ∂ψ/∂z
w = -dpsi_dx       # w = -∂ψ/∂x

# Compute velocity field from stream function
dpsi_dz_2, dpsi_dx_2 = np.gradient(psi_2, z, x)  # note: order is (z, x)
u_2 = dpsi_dz_2        # u = ∂ψ/∂z
w_2 = -dpsi_dx_2       # w = -∂ψ/∂x

# Plot
plt.figure(figsize=(8, 4))
plt.streamplot(x, z, u, w, density=1, linewidth=1.5, arrowsize=1.5, color='b')
plt.streamplot(x, z, u_2, w_2, density=1, linewidth=1.5, arrowsize=1.5, color='g')
#plt.contour(X, Z, psi, levels=20, colors='k', linewidths=0.5)
plt.xlim([-np.sqrt(2), np.sqrt(2)])
plt.ylim([0, 1])
plt.xlabel('x',fontsize=12)
plt.ylabel('z',fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)
#plt.title(r'Streamlines of $\psi(x, z) = \sin(kx)\sin(\pi z)$')
#plt.axis('equal')
plt.tight_layout()
#plt.savefig('streamlines.png',dpi=600,bbox_inches='tight')
plt.show()

