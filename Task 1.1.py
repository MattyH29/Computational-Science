# Task 1.1

import numpy as np
import matplotlib.pyplot as plt

# Grid size
grid_size = 100
# Starting position at the center of the grid
position = [grid_size // 2, grid_size // 2]
# Number of steps for the random walk
steps = 100

# Counts each time a movement is made (check uniform behaviour)
UpCount = 0
DownCount = 0
LeftCount = 0
RightCount = 0

# Create lists to store the walk path
x_path, y_path = [position[0]], [position[1]]

# Random walk Algorithm
#np.random.seed(43)  # For reproducibility

for i in range(steps): #Loops for number of steps
    Xrand = np.random.uniform(0,1) # Random float between 0 and 1
    # Return 0 or 1
    if Xrand >= 0.5:
        Xrand = 1
    else: 
        Xrand = 0
    Yrand = np.random.uniform(0,1) # Random float between 0 and 1
    # Return 0 or 1
    if Yrand >= 0.5:
        Yrand = 1
    else:
        Yrand = 0

    # Binary code to determine direction of move
    if Xrand == 1 and Yrand == 1: # Move up
        UpCount += 1
        position[1] += 1 
    elif Xrand == 1 and Yrand == 0: # Move down
        DownCount += 1
        position[1] += -1
    elif Xrand == 0 and Yrand == 1: # Move left
        LeftCount += 1
        position[0] += -1
    elif Xrand == 0 and Yrand == 0: # Move right
        RightCount += 1
        position[0] += 1

    # Append to path
    x_path.append(position[0])
    y_path.append(position[1])

print(f"Up: {UpCount}, Down: {DownCount}, Left: {LeftCount}, Right: {RightCount}") # Output number of moves in each direction

# Plotting the grid and the walk path
plt.plot(x_path, y_path, marker="o", markersize=3, color="blue", label="Path") # Line path
plt.scatter(x_path[0], y_path[0], color="green", label="Start")   # Starting point
plt.scatter(x_path[-1], y_path[-1], color="red", label="End")     # Ending point

# Grid styling
plt.xlim(-1, grid_size)
plt.ylim(-1, grid_size)
plt.xticks([tick for tick in range(grid_size) if tick % 2 ==0])
plt.yticks([tick for tick in range(grid_size) if tick % 2 ==0])
plt.grid(True)
plt.legend()
plt.title("Random Walk on Grid")
plt.xlabel("X position")
plt.ylabel("Y position")

# Display grid
plt.show()
