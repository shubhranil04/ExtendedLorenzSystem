import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_1 = sl('per1')
data_2 = sl('per2')

print([item['PAR(1)'] for item in data_1])
print([item['PAR(1)'] for item in data_2])

lw = 1.5
indices = [3, 6, 12]

for index in indices:
    rho = data_1[index]['PAR(1)']
    x1 = [data_1[index]['data'][k]['u'][0] for k in range(len(data_1[index]['data']))]
    y1 = [data_1[index]['data'][k]['u'][1] for k in range(len(data_1[index]['data']))]
    z1 = [data_1[index]['data'][k]['u'][2] for k in range(len(data_1[index]['data']))]

    x2 = [data_2[index]['data'][k]['u'][0] for k in range(len(data_2[index]['data']))]
    y2 = [data_2[index]['data'][k]['u'][1] for k in range(len(data_2[index]['data']))]
    z2 = [data_2[index]['data'][k]['u'][2] for k in range(len(data_2[index]['data']))]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x1, y1, z1, 'b', linewidth=lw)
    ax.plot(x2, y2, z2, 'b', linewidth=lw)
    ax.set_xlim([-15, 15])
    ax.set_ylim([-15, 15])
    ax.set_zlim([0, 30])
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)

    # Save each figure

    #plt.savefig(f'orbit_r_{rho:.2f}.png', dpi=600)
    plt.close(fig)  # Close to save memory
