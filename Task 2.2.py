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
grid = np.zeros((grid_size, grid_size))

# Number of moves the simulation can make
steps = 100
# Array to store positions of tumor on grid
x_path, y_path = [position[0]], [position[1]]

active_cells =[position]

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
        direction = [0,1]
    elif Xrand == 1 and Yrand == 0 and Zrand == 0: # Down
        direction = [0,-1]
    elif Xrand == 0 and Yrand == 1 and Zrand == 0: # Left
        direction = [-1,0]
    elif Xrand == 0 and Yrand == 0 and Zrand == 0: # Right
        direction = [1,0]
    elif Xrand == 1 and Yrand == 1 and Zrand == 1: # Up Left
        direction = [-1,1]
    elif Xrand == 1 and Yrand == 0 and Zrand == 1: # Down Left
        direction = [-1,-1]
    elif Xrand == 0 and Yrand == 1 and Zrand == 1: # Up Right
        direction = [1,1]
    elif Xrand == 0 and Yrand == 0 and Zrand == 1: # Down Right
        direction = [1,-1]

    return direction
    
# Tumor growth simulator 
def GompertzModel(k, M, t):
    # Runs for a limited number of days
    for i in range(t):
        N = (M * np.exp(-C * np.exp(-k * i))) # Interagted Gompertz model for cell growth
        
        # Identifies if the model reaches a steady state
        P = (N/M) * 100
        if(P > 97):
            break


# Constant to represnt the capacility ratio against the inital cell size
C = np.log(M/N0)

# Simulate tumour growth upto a limited numbre of growth steps
for step in range(steps+1):
    new_cells = []
    # Runs simulation
    GompertzModel(k,M,t)

    # Loop through all cells
    for cell in active_cells:
        x_current, y_current = cell

        # Random choice if the cell should multiply
        random_move = getRand()
        if random_move < 0.5:

            # Randomly choose direction to grow
            Xrand = getRand()
            Yrand = getRand()
            Zrand = getRand()
            x_direction, y_direction = move(Xrand,Yrand,Zrand)
            # Check the values are in grid range
            new_x, new_y = x_current + x_direction, y_current + y_direction
            if new_x == grid_size or new_x == 0 or new_y == grid_size or new_y == 0:
                continue
            else:
                # Grow if the plot has not already been infected
                if grid[new_x, new_y] == 0:
                    new_cells.append((new_x,new_y))
                    grid[new_x,new_y] = 1
    active_cells.extend(new_cells)

    # Display tumor at different stages of growth 
    if step % 20 == 0 or step == steps:
        plt.imshow(grid, cmap='Blues')
        plt.xlim(-1, grid_size)
        plt.ylim(-1, grid_size)
        plt.xticks([tick for tick in range(grid_size) if tick % 3 ==0])
        plt.yticks([tick for tick in range(grid_size) if tick % 3 ==0])
        plt.grid(True)
        plt.title(f"Simulated Tumor Growth on a Grid using the Gompertz Model Steps: {step}")
        plt.xlabel("X position")
        plt.ylabel("Y position")
        plt.show()

        
        

