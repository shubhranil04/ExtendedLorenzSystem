import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the extended Lorenz system of equations
def extended_lorenz(t, state, sigma, r, b):
    X1, X2, Y1, Y2, Z = state
    dX1 = -sigma * X1 + sigma * Y1
    dX2 = -sigma * X2 - sigma * Y2
    dY1 = -X1 * Z + r * X1 - Y1
    dY2 = X2 * Z - r * X2 - Y2
    dZ = X1 * Y1 - X2 * Y2 - b * Z
    return [dX1, dX2, dY1, dY2, dZ]

# Parameters for the system
sigma = 10.0
r = 28.0
b = 8/3

# Initial conditions: [X1, X2, Y1, Y2, Z]
seed = 50
np.random.seed(seed) 
initial_conditions = 100 * np.random.rand(5)

# Time span for the simulation
t_span = (0, 500)
t_eval = np.linspace(t_span[0], t_span[1], 50000)

# Solve the system of equations
solution = solve_ivp(extended_lorenz, t_span, initial_conditions, args=(sigma, r, b), t_eval=t_eval)

# Extract the solution
X1, X2, Y1, Y2, Z = solution.y
t = solution.t

# Get the time points corresponding to the latter half of the time interval
half_time_index = len(solution.t) // 2

# Slice the solution to get only the latter half
X1_half = X1[half_time_index:]
X2_half = X2[half_time_index:]
Z_half = Z[half_time_index:]

# ------------------------------
# Plot 1: Trajectory in X1-X2-Z space (latter half of the time interval)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlim([-25, 25])
ax.set_ylim([-25, 25])
ax.set_zlim([0, 50])
ax.plot(X1_half, X2_half, Z_half, lw=0.75, color='blue')
ax.set_xlabel('X1', fontsize=14)
ax.set_ylabel('X2', fontsize=14)
ax.set_zlabel('Z', fontsize=14)
plt.savefig(f'extendedattractor_seed_{seed:.0f}.png', dpi=600, bbox_inches='tight', pad_inches=0.5)
plt.show()

# ------------------------------
# Combined Plot: X1/X2 and -Y1/Y2 vs Time (excluding X1, X2, Y1, Y2 = 0)

# Compute valid indices where none of the denominators are zero
valid_indices = (X1 != 0) & (X2 != 0) & (Y1 != 0) & (Y2 != 0)

# Compute ratios
X1_X2 = X1[valid_indices] / X2[valid_indices]
Y1_Y2 = -Y1[valid_indices] / Y2[valid_indices]
t_valid = t[valid_indices]

# Plot both ratios on the same plot
plt.figure(figsize=(8, 6))
plt.plot(t_valid, X1_X2, lw=1.5, color='blue', label='X1 / X2')
plt.plot(t_valid, Y1_Y2, lw=1.5, color='red', label='- Y1 / Y2')
plt.tick_params(axis='both', which='major', labelsize=12)
plt.xlim([0, 5])
plt.ylim([-10, 10])
plt.xlabel('Time', fontsize=14)
plt.ylabel('Ratio', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)

# Save the combined figure
plt.savefig(f'X1_X2_Y1_Y2_vs_time_seed_{seed:.0f}.png', dpi=600, bbox_inches='tight')
plt.show()

print(initial_conditions)

