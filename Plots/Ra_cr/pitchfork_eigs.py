import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variables
r_sym = sp.Symbol('r', real=True)
sigma, b = 10, 8/3

# Define the characteristic polynomial coefficients
a = 1
b_coeff = sigma + b + 1
c_coeff = sigma + b + sigma*b - r_sym*sigma 
d_coeff = -b * sigma * (r_sym - 1)  

# Display the characteristic equation
print("Characteristic equation:")
eq = sp.Eq(sp.Symbol('λ')**3 + b_coeff*sp.Symbol('λ')**2 + c_coeff*sp.Symbol('λ') + d_coeff, 0)
print(eq)

# Get symbolic solutions
print("\nSolving for the exact eigenvalues...")
roots_sym = sp.solve(sp.Poly([a, b_coeff, c_coeff, d_coeff], sp.Symbol('λ')), sp.Symbol('λ'))

# Using r from 0 to 2 with 500 steps
r_vals = np.linspace(0, 2, 500)
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
r_markers = [0, 0.5, 1, 1.5, 2]
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
# Plot eigenvalues vs r

colors = ['blue', 'red', 'green']
labels = [r'$\lambda_1$', r'$\lambda_2$', r'$\lambda_3$']

plt.figure(figsize=(10, 6))
for i in range(3):
    plt.plot(r_vals, roots_numeric[i, :].real, '-', 
             color=colors[i], linewidth=1.5, label=f'{labels[i]}')

# Add markers for specific r values
r_markers = [1]
for r_val in r_markers:
    idx = np.argmin(np.abs(r_vals - r_val))
    for i in [2]:
        plt.plot(r_val, roots_numeric[i, idx].real, 'o', 
                 markersize=8, markeredgecolor='black', markerfacecolor='black')
        plt.annotate(f'r={r_vals[idx]:.1f}', 
                    (r_val, roots_numeric[i, idx].real),
                    xytext=(5, 5), textcoords='offset points',fontsize=16)


plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)

plt.xlabel(r'$r$',fontsize=20)
plt.ylabel(r'$\lambda$',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.xticks([0, 0.5, 1, 1.5, 2], fontsize=16)
plt.ylim([-15,10])
plt.legend(fontsize=16)
plt.savefig('pitchfork_eigs.png', dpi=600, bbox_inches='tight')
plt.show()
