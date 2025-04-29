import numpy as np
import matplotlib.pyplot as plt

def Ra_cr(k,m):

    return (k**2 + (m*np.pi)**2)**3/k**2

k = np.linspace(1, 10, 500)

Ra_cr_1 = Ra_cr(k, 1)
Ra_cr_2 = Ra_cr(k, 2)   
Ra_cr_3 = Ra_cr(k, 3)

# Find minimum points
min_idx_1 = np.argmin(Ra_cr_1)
min_idx_2 = np.argmin(Ra_cr_2)
min_idx_3 = np.argmin(Ra_cr_3)

plt.figure(figsize=(10, 6))
plt.plot(k, Ra_cr_1, label='m=1', color='blue')
plt.plot(k, Ra_cr_2, label='m=2', color='red')
plt.plot(k, Ra_cr_3, label='m=3', color='green')

# Mark the minima with red circles
plt.plot(k[min_idx_1], Ra_cr_1[min_idx_1], color='black',marker='o')
plt.plot(k[min_idx_2], Ra_cr_2[min_idx_2], color='black',marker='o')
plt.plot(k[min_idx_3], Ra_cr_3[min_idx_3], color='black',marker='o')

plt.yscale('log')

plt.xlabel(r'$k$',fontsize=20)
plt.ylabel(r'$Ra_{cr}$',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.legend(fontsize=16)
plt.savefig('Ra_cr.png', dpi=600, bbox_inches='tight')
plt.show()
