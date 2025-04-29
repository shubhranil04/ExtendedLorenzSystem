import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
r_sym = sp.Symbol('r', real=True)
sigma, b = 10, 8/3

# Define the characteristic polynomial coefficients
a = 1
b_coeff = sigma + b + 1
c_coeff = (sigma + r_sym) * b  
d_coeff = 2 * b * sigma * (r_sym - 1)  

# Display the characteristic equation
print("Characteristic equation:")
eq = sp.Eq(sp.Symbol('λ')**3 + b_coeff*sp.Symbol('λ')**2 + c_coeff*sp.Symbol('λ') + d_coeff, 0)
print(eq)

# Get symbolic solutions
print("\nSolving for the exact eigenvalues...")
roots_sym = sp.solve(sp.Poly([a, b_coeff, c_coeff, d_coeff], sp.Symbol('λ')), sp.Symbol('λ'))

# Using r from 1 to 30 with 500 steps
r_vals = np.linspace(1+1e-3, 40, 1000)
roots_numeric = np.zeros((3, len(r_vals)), dtype=complex)

# Function to convert sympy expression to numpy function
def sympy_to_numpy(expr):
    return sp.lambdify(r_sym, expr, "numpy")

# Convert symbolic roots to numeric functions
root_funcs = [sympy_to_numpy(root) for root in roots_sym]

# Evaluate roots for each value of r
for i, func in enumerate(root_funcs):
    try:
        roots_numeric[i, :] = func(r_vals)
    except Exception as e:
        print(f"Error evaluating root {i+1}: {e}")
        # Fallback to numerical approach for this root
        for j, r_val in enumerate(r_vals):
            poly_coeffs = [1, sigma + b + 1, (sigma + r_val) * b, 2 * b * sigma * (r_val - 1)]
            roots_numeric[i, j] = np.roots(poly_coeffs)[i]

'''
# Plotting in complex plane
plt.figure(figsize=(14, 10))
colors = ['blue', 'red', 'green']
labels = ['First eigenvalue', 'Second eigenvalue', 'Third eigenvalue']

for i in range(3):
    plt.plot(roots_numeric[i, :].real, roots_numeric[i, :].imag, '-', 
             color=colors[i], linewidth=1.5, label=labels[i])

plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='black', linestyle='--', alpha=0.3)

# Add markers for specific r values
r_markers = [1, 5, 10, 15, 20, 25, 30]
for r_val in r_markers:
    idx = np.argmin(np.abs(r_vals - r_val))
    for i in range(3):
        plt.plot(roots_numeric[i, idx].real, roots_numeric[i, idx].imag, 'o', 
                 markersize=8, markeredgecolor='black', markerfacecolor=colors[i])
        plt.annotate(f'r={r_vals[idx]:.1f}', 
                    (roots_numeric[i, idx].real, roots_numeric[i, idx].imag),
                    xytext=(5, 5), textcoords='offset points')

plt.xlabel('Real Part', fontsize=14)
plt.ylabel('Imaginary Part', fontsize=14)
plt.title('Corrected Eigenvalue Branches of the Lorenz System in Complex Plane (r=1-30)', fontsize=16)
plt.grid(True, alpha=0.3)
plt.legend(loc='best')
plt.tight_layout()
plt.show()
'''
colors = ['blue', 'red', 'green']
labels = ['First eigenvalue', 'Second eigenvalue', 'Third eigenvalue']

# Plot showing evolution of real parts with r
plt.figure(figsize=(8, 6))
plt.plot(r_vals, roots_numeric[0, :].real, '-', color=colors[0], linewidth=1.5, label=r'Re($\lambda_{1}$)')
plt.plot(r_vals, roots_numeric[1, :].real, '-', color=colors[1], linewidth=1.5, label=r'Re($\lambda_{2/3}$)')

# Add markers for specific r values
r_markers = [24.74]
for r_val in r_markers:
    idx = np.argmin(np.abs(r_vals - r_val))
    for i in [2]:
        plt.plot(r_val, roots_numeric[i, idx].real, 'o', 
                 markersize=8, markeredgecolor='black', markerfacecolor='black')
        plt.annotate(f'r={r_vals[idx]:.2f}', 
                    (r_val, roots_numeric[i, idx].real),
                    xytext=(5, 5), textcoords='offset points',fontsize=16)
        
plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)
plt.xlabel(r'$r$',fontsize=20)
plt.ylabel(r'Re($\lambda$)',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend(fontsize=16)
plt.ylim([-20,10])
plt.savefig('hopf_eigs_real.png', dpi=600, bbox_inches='tight')
plt.show()

# Plot showing evolution of imaginary parts with r
plt.figure(figsize=(8, 6))
plt.plot(r_vals, roots_numeric[0, :].imag, '-', color=colors[0], linewidth=1.5, label=r'Im($\lambda_{1}$)')
plt.plot(r_vals, roots_numeric[1, :].imag, '-', color=colors[1], linewidth=1.5, label=r'Im($\lambda_{2}$)')
plt.plot(r_vals, roots_numeric[2, :].imag, '-', color=colors[2], linewidth=1.5, label=r'Im($\lambda_{3}$)')

'''
# Add markers for specific r values
r_markers = [24.74]
for r_val in r_markers:
    idx = np.argmin(np.abs(r_vals - r_val))
    for i in [2]:
        plt.plot(r_val, roots_numeric[i, idx].real, 'o', 
                 markersize=8, markeredgecolor='black', markerfacecolor='black')
        plt.annotate(f'r={r_vals[idx]:.2f}', 
                    (r_val, roots_numeric[i, idx].real),
                    xytext=(5, 5), textcoords='offset points',fontsize=16)
'''

plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)
plt.xlabel(r'$r$',fontsize=20)
plt.ylabel(r'Im($\lambda$)',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend(fontsize=16)
plt.ylim([-15,15])
plt.savefig('hopf_eigs_imag.png', dpi=600, bbox_inches='tight')
plt.show()
'''
# Plot showing evolution of imaginary parts with r
plt.figure(figsize=(14, 7))
for i in range(3):
    plt.plot(r_vals, roots_numeric[i, :].imag, '-', color=colors[i], linewidth=1.5, label=labels[i])

plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)
plt.xlabel('Parameter r', fontsize=14)
plt.ylabel('Imaginary Part of Eigenvalues', fontsize=14)
plt.title('Evolution of Corrected Eigenvalue Imaginary Parts with Parameter r (r=1-30)', fontsize=16)
plt.grid(True, alpha=0.3)
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Create a 3D plot to visualize the eigenvalues as a function of r
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

for i in range(3):
    ax.plot(r_vals, roots_numeric[i, :].real, roots_numeric[i, :].imag, 
            color=colors[i], linewidth=1.5, label=labels[i])
    
    # Add markers for specific r values
    for r_val in r_markers:
        idx = np.argmin(np.abs(r_vals - r_val))
        ax.scatter([r_vals[idx]], [roots_numeric[i, idx].real], [roots_numeric[i, idx].imag], 
                   color=colors[i], edgecolor='black', s=50)
        ax.text(r_vals[idx], roots_numeric[i, idx].real, roots_numeric[i, idx].imag, 
                f'r={r_vals[idx]:.1f}', size=8)

ax.set_xlabel('Parameter r', fontsize=12)
ax.set_ylabel('Real Part', fontsize=12)
ax.set_zlabel('Imaginary Part', fontsize=12)
ax.set_title('3D Visualization of Corrected Eigenvalue Evolution with Parameter r', fontsize=16)
ax.legend(loc='best')
plt.tight_layout()
plt.show()

# Find critical values where real parts of eigenvalues cross zero
print("\nAnalyzing bifurcation points:")

# Function to calculate eigenvalues for a specific r value
def get_eigenvalues(r_value):
    return np.roots([1, sigma + b + 1, (sigma + r_value) * b, 2 * b * sigma * (r_value - 1)])

# Check near r=1 (first bifurcation)
r_critical1 = np.linspace(0.95, 1.05, 100)
eig_real_parts = np.zeros((3, len(r_critical1)))

for i, r_val in enumerate(r_critical1):
    eigs = get_eigenvalues(r_val)
    eig_real_parts[:, i] = eigs.real

# Find where real part crosses zero
for i in range(3):
    for j in range(len(r_critical1) - 1):
        if eig_real_parts[i, j] * eig_real_parts[i, j+1] <= 0:
            crossing_r = (r_critical1[j] + r_critical1[j+1]) / 2
            print(f"Eigenvalue {i+1} crosses zero at approximately r = {crossing_r:.6f}")

# Print eigenvalues at r = 28 (chaotic regime)
r_chaotic = 28
eigs_chaotic = get_eigenvalues(r_chaotic)
print(f"\nEigenvalues at r = {r_chaotic} (chaotic regime):")
for i, eig in enumerate(eigs_chaotic):
    print(f"λ_{i+1} = {eig}")
'''