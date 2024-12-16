# Task 2.1

import numpy as np
import matplotlib.pyplot as plt

# Set conditions
N0 = 10**9 # Number of cells
k = 0.006 # Growth rate of cells
M = 10**13 # Capacity
t = 1200 # Time in days
xplot, yplot = [[],[]] # Array for graphing values
xtimeplot, ytimeplot = [[],[]]

def simulate(N0, k, M, t):
    # Constant to represnt the capacility ratio against the inital cell size
    C = np.log(M/N0)

    # Simulate tumour growth upto day limit at differrent max capacities

    # Capcaity 10**13 (average)
    for i in range(t):
        N = (M * np.exp(-C * np.exp(-k * i))) # Intergation of Gompertz model for cell growth
        xplot.append(i)
        yplot.append(N)
        P = (N/M) * 100
        if(P > 97):
            break
        # Identifies if the model reaches a steady state

    # Plotting graph
    plt.plot(xplot, yplot, label='Tumor Growth', color='blue')
    plt.title("Simulation of Tumor Growth using Gompertz Model")
    plt.xlabel("Time (days)")
    plt.ylabel("Number of Tumor Cells (N)")
    plt.legend()
    plt.grid(True)
    plt.show()

def time_to_steady_state(N0, k, M, t):

    # Constant to represnt the capacility ratio against the inital cell size
    C = np.log(M/N0)

    for i in range(t):
        N = (M * np.exp(-C * np.exp(-k * i))) # Intergation of Gompertz model for cell growth
        # Identifies if the model reaches a steady state
        P = (N/M) * 100
        if(P > 98):
            ytimeplot.append(i)
            break


simulate(N0,k,M,t)

M = 10**11 # Lower Capacity
xplot.clear()
yplot.clear()
simulate(N0,k,M,t)


M = 10**18 # Higer Capacity
xplot.clear()
yplot.clear()
simulate(N0,k,M,t)

for i in range(11,21):
    M = 10**i
    xtimeplot.append(i)
    time_to_steady_state(N0, k, M, t)

plt.plot(xtimeplot, ytimeplot, color='blue')
plt.title("Time for Gompertz Model to Reach Steady State with Differing Maximum Carrying Capacities")
plt.xlabel("Maximum Carrying Capacity (10^)")
plt.ylabel("Time (days)")
plt.grid(True)
plt.show()



