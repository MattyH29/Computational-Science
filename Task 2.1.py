# Task 2.1

import numpy as np
import matplotlib.pyplot as plt

# Set conditions
N0 = 10**9 # Number of cells
k = 0.006 # Growth rate of cells
M = 10**13 # Capacity
t = 1200 # Time in days
xplot, yplot = [[],[]] # Array for graphing values

# Constant to represnt the capacility ratio against the inital cell size
C = np.log(M/N0)

# Simulate tumour growth upto day limit at differrent max capacities

# Capcaity 10**13 (average)
for i in range(t):
    N = (M * np.exp(-C * np.exp(-k * i))) # Intergation of Gompertz model for cell growth
    xplot.append(i)
    yplot.append(N)

# Capcacity 10**11 (lower)
M = 10**11
C = np.log(M/N0)
zplot = []
for i in range(t):
    N = (M * np.exp(-C * np.exp(-k * i))) # Intergation of Gompertz model for cell growth
    zplot.append(N)

# Capcaity 10**20 (higher)
M = 10**20
C = np.log(M/N0)
lplot = []
for i in range(t):
    N = (M * np.exp(-C * np.exp(-k * i))) # Intergation of Gompertz model for cell growth
    lplot.append(N)

# Plotting graph
plt.plot(xplot, yplot, label='Tumor Growth', color='blue')
#plt.plot(xplot, zplot, label='Tumor Growth',color='red')
#plt.plot(xplot, lplot, label='Tumor Growth',color='green')
#plt.axhline(M, linestyle='--', color='red', label='Carrying Capacity (M)')
plt.title("Simulation of Tumor Growth using Gompertz Model")
plt.xlabel("Time (days)")
plt.ylabel("Number of Tumor Cells (N)")
plt.legend()
plt.grid(True)
plt.show()