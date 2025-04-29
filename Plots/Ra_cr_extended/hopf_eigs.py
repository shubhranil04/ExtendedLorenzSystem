import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbolic variables
r, sigma, b, omega, lam = sp.symbols('r sigma b omega lambda', real=True)
cos = sp.cos
sin = sp.sin
sqrt = sp.sqrt

# Define the Jacobian matrix J
J = sp.Matrix([
    [-sigma, 0, sigma, 0, 0],
    [0, -sigma, 0, -sigma, 0],
    [1, 0, -1, 0, -sqrt(b * (r - 1)) * cos(omega)],
    [0, -1, 0, -1, sqrt(b * (r - 1)) * sin(omega)],
    [sqrt(b * (r - 1)) * cos(omega), sqrt(b * (r - 1)) * sin(omega),
     sqrt(b * (r - 1)) * cos(omega), -sqrt(b * (r - 1)) * sin(omega), -b]
])

# Characteristic polynomial: det(J - lambda*I)
char_poly = (J - lam * sp.eye(5)).det()
char_poly = sp.simplify(char_poly)

# Factor out lambda (known root)
char_poly_factored = sp.simplify(char_poly / lam)

# Substitute numerical values
sigma_val = 10
b_val = 8/3
omega_val = 0

# Define function to get numerical coefficients
def get_coeffs_at_r(r_val):
    expr = char_poly_factored.subs({sigma: sigma_val, b: b_val, omega: omega_val, r: r_val})
    poly = sp.Poly(expr, lam)
    coeffs = np.array([float(c) for c in poly.all_coeffs()])
    return coeffs

# r range
r_values = np.linspace(1, 30, 300)

# Storage for eigenvalues (branches tracked)
eigenvalues_tracked = []

# First step: compute initial eigenvalues
coeffs_initial = get_coeffs_at_r(r_values[0])
roots_previous = np.roots(coeffs_initial)
roots_previous = sorted(roots_previous, key=lambda z: (np.real(z), np.imag(z)))
eigenvalues_tracked.append(roots_previous)

# Now loop
for r_val in r_values[1:]:
    coeffs = get_coeffs_at_r(r_val)
    roots_current = np.roots(coeffs)
    
    # Match roots: closest to previous roots
    roots_remaining = list(roots_current)
    matched_roots = []
    
    for prev_root in roots_previous:
        distances = [abs(root - prev_root) for root in roots_remaining]
        idx_min = np.argmin(distances)
        matched_roots.append(roots_remaining.pop(idx_min))
    
    eigenvalues_tracked.append(matched_roots)
    roots_previous = matched_roots  # Update for next iteration

# Convert to arrays
eigenvalues_tracked = np.array(eigenvalues_tracked)

# Separate real and imaginary parts
eigen_real_parts = np.real(eigenvalues_tracked)
eigen_imag_parts = np.imag(eigenvalues_tracked)

# Now plot real parts (first plot)
fig1, ax1 = plt.subplots(figsize=(8, 6))

# Define r_marker
r_marker = 24.74

# Find the index of r_marker
r_index = np.argmin(np.abs(r_values - r_marker))

for i in range(4):
    ax1.plot(r_values, eigen_real_parts[:, i], label=fr"Re($λ_{i+1}$)", linewidth=2)

# Plot the zero eigenvalue as a horizontal line
ax1.axhline(0, color='purple', linestyle='--', label=r"Re($λ_5$)", linewidth=2)

# Plot the marker for the specific r_marker
ax1.plot(r_marker, eigen_real_parts[r_index, 3], 'ko', markersize=8)
plt.annotate(f'r={r_marker:.2f}', 
                    (r_marker, eigen_real_parts[r_index, 3]	),
                    xytext=(5, 5), textcoords='offset points',fontsize=16)

ax1.set_xlabel(r'$r$', fontsize=18)
ax1.set_ylabel(r'Re($\lambda$)', fontsize=18)
ax1.tick_params(axis='both', which='major', labelsize=14)
ax1.legend(fontsize=14,loc='upper left')
ax1.set_ylim([-20, 10])
plt.savefig('extendedhopf_eigs_real.png', dpi=600, bbox_inches='tight')
fig1.tight_layout()
plt.show()

# Now plot imag parts (second plot)
fig2, ax2 = plt.subplots(figsize=(8, 6))

for i in range(4):
    ax2.plot(r_values, eigen_imag_parts[:, i], label=fr"Im($λ_{i+1}$)", linewidth=2)

# Plot the zero eigenvalue as a horizontal line
ax2.axhline(0, color='purple', linestyle='--', label=r"Im($λ_5$)", linewidth=2)

ax2.set_xlabel(r'$r$', fontsize=18)
ax2.set_ylabel(r'Im($\lambda$)', fontsize=18)
ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.legend(fontsize=14,loc='upper left')
ax2.set_ylim([-15, 15])
plt.savefig('extendedhopf_eigs_imag.png', dpi=600, bbox_inches='tight')
fig2.tight_layout()
plt.show()

