import numpy as np
import matplotlib.pyplot as plt
# %matplotlib  # Uncomment in a Jupyter notebook environment

np.random.seed(10)

print(f"Using matplotlib backend: {plt.get_backend()}")












N = 30
x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))

area = (30 * np.random.rand(N)) ** 2

plt.scatter(x , y , s = area , c = colors , alpha = 0.05)

plt.show()













from matplotlib import style
style.use('ggplot')

x = [2 , 4 , 6]
y = [12 , 14 , 16]


x2 = [3 , 3 , 5]
y2 = [7 , 10 , 16]

plt.show()