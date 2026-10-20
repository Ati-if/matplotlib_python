
import numpy as np
import matplotlib.pyplot as plt

# Create X and Y coordinates
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate Z values
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# First plot: Contour plot with labels
CS = axes[0].contour(X, Y, Z)
axes[0].clabel(CS, inline=True, fontsize=10)
axes[0].set_title('Labeled Contour Plot')

# Second plot: Filled contour plot
axes[1].contourf(X, Y, Z, cmap='viridis')
axes[1].set_title('Filled Contour Plot')

plt.tight_layout()
plt.show()
