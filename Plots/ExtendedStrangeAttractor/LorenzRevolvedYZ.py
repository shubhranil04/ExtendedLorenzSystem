import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

# Define the Lorenz system
def lorenz_rhs(t, state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Integrate the Lorenz system
def integrate_lorenz(initial_state=[1.0, 1.0, 1.0], t_span=(0, 500), num_points=50000):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    sol = solve_ivp(
        lorenz_rhs,
        t_span,
        initial_state,
        t_eval=t_eval,
        method='DOP853'
    )
    return sol.t, sol.y[0], sol.y[1], sol.y[2]

# Generate surface of revolution around Z-axis from Y-Z projection
def generate_surface_of_revolution(y, z, num_angles=1000):
    theta = np.linspace(0, 2 * np.pi, num_angles)
    y_rot = np.outer(np.abs(y), np.cos(theta))  # abs(y) to maintain radial symmetry
    x_rot = np.outer(np.abs(y), np.sin(theta))
    z_mesh = np.tile(z, (num_angles, 1)).T
    return x_rot, y_rot, z_mesh

# Main routine
def main():
    # Step 1: Integrate Lorenz system
    t, x, y, z = integrate_lorenz()

    # Step 2: Use second half of data to avoid transients
    midpoint = len(t) // 2
    y, z = y[midpoint:], z[midpoint:]

    # Step 3: Plot Y-Z projection
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(y, z, color='blue', lw=0.6)
    ax.tick_params(axis='both', which='major', labelsize=14)
    plt.xlabel(r'Y', fontsize=18)
    plt.ylabel(r'Z', fontsize=18)
    plt.grid(True, alpha=0.3)
    plt.savefig('lorenz_yz_projection.png', dpi=600, bbox_inches='tight')
    plt.close()
    '''
    # Step 4: Generate and plot solid of revolution
    Xr, Yr, Zr = generate_surface_of_revolution(y, z, num_angles=1000)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(
        Xr, Yr, Zr,
        rstride=5,
        cstride=5,
        color='white',
        edgecolor='black',
        linewidth=0.2,
        alpha=1.0
    )

    ax.set_xlabel(r'Y$_1$', fontsize=18)
    ax.set_ylabel(r'Y$_2$', fontsize=18)
    ax.set_zlabel(r'Z', fontsize=18)
    ax.view_init(elev=30, azim=135)
    ax.tick_params(axis='both', which='major', labelsize=14)
    plt.savefig('lorenz_y_surface_of_revolution.png', dpi=600, bbox_inches='tight', pad_inches=0.5)
    plt.close()
    '''
    
if __name__ == "__main__":
    main()

