# Task 2.2

import numpy as np
import matplotlib.pyplot as plt

# Set conditions
N0 = 10**9 # Inital number of cells
k = 0.006 # Growth rate of cells
M = 10**13 # Capacity
t = 1200 # Time in days


# Grid size
grid_size = 100
# Starting position at the center of the grid
position = [grid_size // 2, grid_size // 2]

# Number of moves the simulation can make
moves = 1000
# Array to store positions of tumor on grid
x_path, y_path = [position[0]], [position[1]]

# Binary uniform random 
def getRand():
    Xrand = np.random.uniform(0,1)
    if Xrand >= 0.5:
        return 1
    else: 
        return 0

# Random movement
def move(Xrand, Yrand, Zrand):

    # Binary direction selector 
    if Xrand == 1 and Yrand == 1 and Zrand == 0: # Up
        position[1] += 1 
    elif Xrand == 1 and Yrand == 0 and Zrand == 0: # Down
        position[1] += -1
    elif Xrand == 0 and Yrand == 1 and Zrand == 0: # Left
        position[0] += -1
    elif Xrand == 0 and Yrand == 0 and Zrand == 0: # Right
        position[0] += 1
    elif Xrand == 1 and Yrand == 1 and Zrand == 1: # Up Left
        position[0] += -1
        position[1] += 1
    elif Xrand == 1 and Yrand == 0 and Zrand == 1: # Down Left
        position[0] += -1
        position[1] += -1
    elif Xrand == 0 and Yrand == 1 and Zrand == 1: # Up Right
        position[0] += 1
        position[1] += 1
    elif Xrand == 0 and Yrand == 0 and Zrand == 1: # Down Right
        position[0] += 1
        position[1] += -1

    # Checks the new position is within the boundaries of the grid
    position[0] = max(0, min(grid_size - 1, position[0]))
    position[1] = max(0, min(grid_size - 1, position[1]))

    # Add movement to list
    x_path.append(position[0])
    y_path.append(position[1])
    
# Tumor growth simulator 
def GompertzModel(k, M, t):
    # Runs for a limited number of days
    for i in range(t):
        N = (M * np.exp(-C * np.exp(-k * i))) # Interagted Gompertz model for cell growth
        
        # Identifies if the model reaches a steady state
        P = (N/M) * 100
        if(P > 99.99):
            break


# Constant to represnt the capacility ratio against the inital cell size
C = np.log(M/N0)

# Simulate tumour growth upto a limited numbre of growth steps
for q in range(moves):
    # Runs simulation
    GompertzModel(k,M,t)

    # Gets uniform random binary results
    Xrand = getRand()
    Yrand = getRand()
    Zrand = getRand()

    # Choses a direction of movement for the cell
    move(Xrand,Yrand,Zrand)

# Plotting the grid and the walk path
plt.scatter(x_path, y_path, marker="o", color="blue", label="Tumor")

# Grid styling
plt.xlim(-1, grid_size)
plt.ylim(-1, grid_size)
plt.xticks([tick for tick in range(grid_size) if tick % 2 ==0])
plt.yticks([tick for tick in range(grid_size) if tick % 2 ==0])
plt.grid(True)
plt.legend()
plt.title("Simulated Tumor Growth on a Grid using the Gompertz Model")
plt.xlabel("X position")
plt.ylabel("Y position")

plt.show()

        
        

