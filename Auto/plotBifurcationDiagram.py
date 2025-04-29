import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def parseB(filename):
    ips = None
    rho = []
    x = []
    stability = []
    max_x = []
    min_x = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert the line into a list of strings by splitting on whitespace
                words = line.split()
                for i in range(len(words) - 1):
                    if words[i] == 'IPS' and words[i+1] == '=':
                    # Check the next word for the value of IPS
                        try:
                            ips = int(words[i+2])  # The value is the second word after 'IPS'
                            break  # Exit loop once we find the value
                        except IndexError:
                            print("Error: IPS value is missing after '='.")
                            return
                        except ValueError:
                            print(f"Error: Unable to convert the value '{words[i+2]}' to an integer.")
                            return

                if ips == 1 and words[0] != '0':
                    PT = int(words[1])
                    rho_ = float(words[4])
                    x_ = float(words[6])
                    
                    rho.append(rho_)
                    x.append(x_)
                    stability.append(-np.sign(PT))
                
                if ips == 2 and words[0] != '0':
                    PT = int(words[1])
                    rho_ = float(words[4])
                    max_x_ = float(words[6])
                    min_x_ = float(words[10])
                    
                    rho.append(rho_)
                    max_x.append(max_x_)
                    min_x.append(min_x_)
                    stability.append(-np.sign(PT))
                    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        
    # Convert lists to numpy arrays
    rho = np.array(rho)
    x = np.array(x)
    stability = np.array(stability)
    max_x = np.array(max_x)
    min_x = np.array(min_x)
    
    
    # Get sorted indices based on rho
    sorted_indices = np.argsort(rho)

    # Reorder all arrays based on sorted indices
    rho = rho[sorted_indices]
    
    if ips == 1:
        x = x[sorted_indices]
  
    elif ips == 2:
        max_x = max_x[sorted_indices]
        min_x = min_x[sorted_indices]
        
    stability = stability[sorted_indices]
    
    return {'ips':ips, 'rho':rho, 'x':x, 'max_x':max_x, 'min_x':min_x, 'stability':stability}

filename = "b.eq"

dict=parseB(filename)
ips=dict['ips']
rho=dict['rho']
x=dict['x']
stability=dict['stability']

rho_b1_stable = rho[(np.abs(x)<1e-6) & (stability==1)]
x_b1_stable = x[(np.abs(x)<1e-6) & (stability==1)]
rho_b1_unstable = rho[(np.abs(x)<1e-6) & (stability==-1)]
x_b1_unstable = x[(np.abs(x)<1e-6) & (stability==-1)]
rho_b1_unstable = np.insert(rho_b1_unstable, 0, rho_b1_stable[-1])
x_b1_unstable = np.insert(x_b1_unstable, 0, x_b1_stable[-1])

rho_b2_stable = rho[(x>1e-6) & (stability==1)]
x_b2_stable = x[(x>1e-6) & (stability==1)]

rho_b2_unstable = rho[(x>1e-6) & (stability==-1)]
x_b2_unstable = x[(x>1e-6) & (stability==-1)]
rho_b2_unstable = np.insert(rho_b2_unstable, 0, rho_b2_stable[-1])
x_b2_unstable = np.insert(x_b2_unstable, 0, x_b2_stable[-1])

rho_b3_stable = rho[(x<-1e-6) & (stability==1)]
x_b3_stable = x[(x<-1e-6) & (stability==1)]

rho_b3_unstable = rho[(x<-1e-6) & (stability==-1)]
x_b3_unstable = x[(x<-1e-6) & (stability==-1)]
rho_b3_unstable = np.insert(rho_b3_unstable, 0, rho_b3_stable[-1])
x_b3_unstable = np.insert(x_b3_unstable, 0, x_b3_stable[-1])

filename="b.per1"

dict=parseB(filename)
ips=dict['ips']
rho=dict['rho']
max_x=dict['max_x']
min_x=dict['min_x']

rho_b4 = rho[(min_x>1e-6)]
max_b4 = max_x[(min_x>1e-6)]
min_b4 = min_x[(min_x>1e-6)]

filename="b.per2"
dict=parseB(filename)
ips=dict['ips']
rho=dict['rho']
max_x=dict['max_x']
min_x=dict['min_x']

rho_b5 = rho[(min_x<-1e-6)]
max_b5 = max_x[(min_x<-1e-6)]
min_b5 = min_x[(min_x<-1e-6)]

rho_homo = np.min(rho_b5)
rho_hopf = np.max(rho_b5)
max_hopf = max_b5[rho_b5==rho_hopf][0]

# Plotting the bifurcation diagram
plt.figure(figsize=(12, 6))
plt.plot(rho_b1_stable, x_b1_stable,color='blue',linewidth=1.5)
plt.plot(rho_b1_unstable, x_b1_unstable,color='blue',linestyle='--',linewidth=1.5)
plt.plot(rho_b2_stable, x_b2_stable, color='green',linewidth=1.5)
plt.plot(rho_b2_unstable, x_b2_unstable, color='green',linestyle='--',linewidth=1.5)
plt.plot(rho_b3_stable, x_b3_stable, color='red',linewidth=1.5)
plt.plot(rho_b3_unstable, x_b3_unstable, color='red',linestyle='--',linewidth=1.5)
plt.plot(rho_b4, max_b4, color='purple',linestyle='--',linewidth=1.5)
plt.plot(rho_b4, min_b4, color='purple',linestyle='--',linewidth=1.5)
plt.plot(rho_b5, max_b5, color='orange',linestyle='--',linewidth=1.5)
plt.plot(rho_b5, min_b5, color='orange',linestyle='--',linewidth=1.5)

plt.plot(rho_homo, 0, color='black', marker='o')
plt.text(rho_homo, 0, f'  r = {rho_homo:.3f}', fontsize=12, ha='left', va='bottom')

plt.plot(rho_hopf, max_hopf, color='black', marker='o')
plt.text(rho_hopf, max_hopf, f'  r = {rho_hopf:.3f}', fontsize=12, ha='left', va='bottom')
plt.text(rho_hopf-10, max_hopf-3.5, 'Unstable Limit Cycle', fontsize=12, ha='left', va='bottom')

plt.plot(rho_hopf, -max_hopf, color='black', marker='o')
plt.text(rho_hopf, -max_hopf, f'  r = {rho_hopf:.3f}', fontsize=12, ha='left', va='top')
plt.text(rho_hopf-10, -max_hopf+2.5, 'Unstable Limit Cycle', fontsize=12, ha='left', va='bottom')
 
plt.xlim([0,30])
plt.xlabel(r'r',fontsize=14)
plt.ylabel(r'X',fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.savefig('bifurcation_diagram.png', dpi=600, bbox_inches='tight')
plt.show()
