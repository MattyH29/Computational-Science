import numpy as np
import matplotlib.pyplot as plt

sample_size = 10000

uni_rand = np.random.uniform(0,10,sample_size)


norm_rand = np.random.normal(0,1,sample_size)

# Plot histograms
plt.figure(figsize=(12, 6))

# Uniform distribution histogram
plt.subplot(1, 2, 1)
plt.hist(uni_rand, bins=20, color='lightblue', edgecolor='black')
plt.title('Uniform Random Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Normal distribution histogram
plt.subplot(1, 2, 2)
plt.hist(norm_rand, bins=20, color='lightblue', edgecolor='black')
plt.title('Normal Random Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the plot
plt.tight_layout()
plt.show()