print("Hello Everyone! This is day 7 of learning Python .")










from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)


fig , axes = plt.subplots(1 , 5 , figsize = (10 , 20))

ax = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8] , polar = True)

plt.show()













fig = plt.figure()

ax = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8] , polar = True)

plt.show()














fig = plt.figure()

ax = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8] , polar = True)

t = np.linspace(0 , 2 * np.pi , 100)

ax.plot(t , t * 5 , color = 'blue' , lw = 3)

plt.show()













import matplotlib.pyplot as plt
import numpy as np


#Draw a Histogram

hist_data = np.random.randn(1000)

fig , axes = plt.subplots(1 , 2 , figsize = (10 , 5))

axes[0].set_title('Histogram')

axes[0].hist(hist_data)

axes[1].set_title('Cummulative Detailed Histogram')

axes[1].hist(hist_data , cumulative = True , density = 1 , bins = 50)


plt.show()















hist_data = np.random.randn(1000)

fig , axes = plt.subplots(1 , 4 , figsize = (20 , 5))

axes[0].set_title('Histogram of n')
axes[0].hist(hist_data)


axes[1].set_title('Cummulative Detailed History of n')
axes[1].hist(hist_data , cumulative = True , density = 1 , bins = 50)

axes[2].set_title('Histogram of hist_data')
axes[2].hist(hist_data)


axes[3].set_title('Detailed Histogram of hist_data')
axes[3].hist(hist_data , cumulative = True , density = 2 , bins = 50)

plt.show()



















#Draw a contour image

import matplotlib  as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.025

x = np.arange(-3.0 , 3.0 , delta)

y = np.arange(-2.0 , 2.0 , delta)

X , Y = np.meshgrid(x , y)

Z1  = np.exp(-X ** 2 - Y ** 2)

Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)

Z = (Z1 - Z2) * 2














fig , axes = plt.subplots(1 , 2 , figsize = (10 , 5))

axes[0].set_title('Contour Plot')
axes[0].contour(X , Y , Z)


axes[1].set_title('Filled Contour Plot')
axes[1].contourf(X , Y , Z , cmap = 'viridis')

plt.show()
















fig , ax = plt.subplots()

CS = ax.contour(X , Y , Z)

ax.clabel(CS , inline = True , fontsize = 10)

ax.set_title('Labouled Contour Plot')

plt.show()