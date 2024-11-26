# Task 1.2

import numpy as np
import matplotlib.pyplot as plt

# Grid size
grid_size = 100
# Starting position at the center of the grid
position = [grid_size // 2, grid_size // 2]
# Number of steps for the random walk
steps = 10000

# Varibables to count the number of times a direction is used
UpCount = 0
DownCount = 0
LeftCount = 0
RightCount = 0
LeftUpCount = 0
LeftDownCount = 0
RightUpCount = 0
RightDownCount = 0

# Create lists to store the walk path
x_path, y_path = [position[0]], [position[1]]

# Random walk
#np.random.seed(42)  # For reproducibility
for i in range(steps):
    # Uniform random binary selector
    Xrand = np.random.uniform(0,1) # Random float between 0 and 1
    if Xrand >= 0.5:
        Xrand = 1
    else: 
        Xrand = 0
    Yrand = np.random.uniform(0,1) # Random float between 0 and 1
    if Yrand >= 0.5:
        Yrand = 1
    else:
        Yrand = 0
    Zrand = np.random.uniform(0,1) # Random flaot between 0 and 1
    if Zrand >= 0.5:
        Zrand = 1
    else:
        Zrand = 0

    # Binary direction selector
    if Xrand == 1 and Yrand == 1 and Zrand == 0: # Up
        UpCount += 1
        position[1] += 1 
    elif Xrand == 1 and Yrand == 0 and Zrand == 0: # Down
        DownCount += 1
        position[1] += -1
    elif Xrand == 0 and Yrand == 1 and Zrand == 0: # Left
        LeftCount += 1
        position[0] += -1
    elif Xrand == 0 and Yrand == 0 and Zrand == 0: # Right
        RightCount += 1
        position[0] += 1
    elif Xrand == 1 and Yrand == 1 and Zrand == 1: # Up Left
        LeftUpCount += 1
        position[0] += -1
        position[1] += 1
    elif Xrand == 1 and Yrand == 0 and Zrand == 1: # Down Left
        LeftDownCount += 1
        position[0] += -1
        position[1] += -1
    elif Xrand == 0 and Yrand == 1 and Zrand == 1: # Up Right
        RightUpCount += 1
        position[0] += 1
        position[1] += 1
    elif Xrand == 0 and Yrand == 0 and Zrand == 1: # Down Right
        RightDownCount += 1
        position[0] += 1
        position[1] += -1

    # Keep within grid bounds
    position[0] = max(0, min(grid_size - 1, position[0]))
    position[1] = max(0, min(grid_size - 1, position[1]))
    # Append to path
    x_path.append(position[0])
    y_path.append(position[1])

print(f"Up: {UpCount}, Down: {DownCount}, Left: {LeftCount}, Right: {RightCount}, Up Left: {LeftUpCount}, Up Right: {RightUpCount}, Down Left: {LeftDownCount}, Down Right: {RightDownCount}")

# Plotting the grid and the walk path
plt.plot(x_path, y_path, marker="o", markersize=3, color="blue", label="Path") # Path
plt.scatter(x_path[0], y_path[0], color="green", label="Start")   # Starting point
plt.scatter(x_path[-1], y_path[-1], color="red", label="End")     # Ending point

# Grid styling
plt.xlim(-1, grid_size)
plt.ylim(-1, grid_size)
plt.xticks([tick for tick in range(grid_size) if tick % 2 ==0])
plt.yticks([tick for tick in range(grid_size) if tick % 2 ==0])
plt.grid(True)
plt.legend()
plt.title("Random Walk on a Grid")
plt.xlabel("X position")
plt.ylabel("Y position")

plt.show()
