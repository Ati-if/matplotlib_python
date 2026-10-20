print("Hello Everyone! This is Atif Nawaz continuing to learn python .")






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













import matplotlib.pyplot as plt
import numpy as np

# 1. Define data for X, Y, and Z
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) ** 10 + np.cos(10 + Y * X) * np.cos(X)

# 2. Create a 1x2 subplot figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Left Plot: Labeled Contour Plot ---
CS = axes[0].contour(X, Y, Z, cmap="viridis")
axes[0].clabel(CS, inline=True, fontsize=10)
axes[0].set_title("Labeled Contour Plot")

# --- Right Plot: Filled Contour Plot ---
# Fixed 'virdis' typo to 'viridis'
cf = axes[1].contourf(X, Y, Z, cmap="viridis")
axes[1].set_title("Filled Contour Plot")

# Optional: Add a colorbar for the filled contour
fig.colorbar(cf, ax=axes[1])

plt.tight_layout()
plt.show()












import matplotlib.pyplot as plt
import numpy as np

# Create your data
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-2.0, 2.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# Create a single plot window
fig, ax = plt.subplots(figsize=(6, 5))

# Draw the filled contour graph
cf = ax.contourf(X, Y, Z, cmap="viridis")

# Add a colorbar to show the scale
fig.colorbar(cf)

ax.set_title("Contour Plot")
plt.show()















import numpy as np
import matplotlib.pyplot as plt


np.random.seed(10)
