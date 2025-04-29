import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_1 = sl('per1')
data_2 = sl('per2')

print([item['PAR(1)'] for item in data_1])
print([item['PAR(1)'] for item in data_2])

lw = 1.5
indices = [5]

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
    
for index in indices:
    rho = data_1[index]['PAR(1)']
    seed = 100
    np.random.seed(seed) 
    IC =  15*np.random.rand(3) #np.array([1e-9, 0, 10])  # Initial condition
    print(IC)
    t = np.linspace(0, 100, 10000)  # Time points

    # Integrate the Lorenz system
    from scipy.integrate import solve_ivp
    sol = solve_ivp(lorenz_system, [t[0], t[-1]], IC, method='DOP853', t_eval=t, args=(rho,), rtol=1e-10, atol=1e-10)

    x1 = [data_1[index]['data'][k]['u'][0] for k in range(len(data_1[index]['data']))]
    y1 = [data_1[index]['data'][k]['u'][1] for k in range(len(data_1[index]['data']))]
    z1 = [data_1[index]['data'][k]['u'][2] for k in range(len(data_1[index]['data']))]

    x2 = [data_2[index]['data'][k]['u'][0] for k in range(len(data_2[index]['data']))]
    y2 = [data_2[index]['data'][k]['u'][1] for k in range(len(data_2[index]['data']))]
    z2 = [data_2[index]['data'][k]['u'][2] for k in range(len(data_2[index]['data']))]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(sol.y[0], sol.y[1], sol.y[2], lw=0.5, color='red')
    ax.plot(x1, y1, z1, 'b', linewidth=lw)
    ax.plot(x2, y2, z2, 'b', linewidth=lw)
    ax.set_xlim([-25, 25])
    ax.set_ylim([-25, 25])
    ax.set_zlim([0, 30])
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)
    # Save each figure
    plt.savefig(f'attractor_with_orbit_r_{rho:.2f}_seed_{seed:.0f}.png', dpi=600)
    plt.show()
    
    plt.close(fig)  # Close to save memory
