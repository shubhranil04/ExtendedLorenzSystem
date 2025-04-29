import sympy as sp

# Define symbolic variables
sigma, r, b = sp.symbols('sigma r b')

# Define the matrix (example: Lorenz system Jacobian you gave)
J = sp.Matrix([
    [-sigma, 0, sigma, 0, 0],
    [0, -sigma, 0, -sigma, 0],
    [r, 0, -1, 0, 0],
    [0, -r, 0, -1, 0],
    [0, 0, 0, 0, -b]
])

print(J)

# Find eigenvalues analytically
eigenvals = J.eigenvals()

# Print eigenvalues
for eigenval, multiplicity in eigenvals.items():
    print(f"Eigenvalue: {eigenval}, Multiplicity: {multiplicity}")

