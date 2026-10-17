print("Hello , Everyone!This is Atif Nawaz.Continuing to enhance python skills.")










import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0 , 10 , 100)

fig , axes = plt.subplots(dpi = 100)

axes.plot(x , x + 1 , color = 'blue' , linewidth = 2)

axes.plot(x , x + 2 , color = 'red' , linewidth = 2)

axes.plot(x , x + 3 , color = 'blue' , linewidth = 2)

axes.plot(x , x + 4 , color = 'orange' , linewidth = 2)


plt.show()










fig , axes = plt.subplots(dpi = 100)

axes.plot(x , x ** 2 , color = 'blue' , alpha = 1 , linewidth = 2)

axes.plot(x , x **  3 , color = 'red' , alpha = 1 , linewidth = 2)

axes.plot(x , x ** 1.5 , color = 'green' , alpha = 0.5 , linewidth = 3)

axes.plot(x , x ** 2  , color = 'orange' , alpha = 0.5 , linewidth = 2)

plt.show()













import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)
fig , axes = plt.subplots(dpi = 100)

#define linestyle for blue lines

linestyles = ['-' , '--' , '-.' , ':']


axes.plot(x , x + 1 , color = 'blue' , lw = 2 , linestyle = linestyles[0])

axes.plot(x , x + 2 , color = 'red' , lw = 3  , linestyle = linestyles[1])

axes.plot(x , x + 3 , color = 'orange' , lw = 1 , linestyle = linestyles[2])


line, = axes.plot(x , x + 4 , color = 'black' , lw = 2)

line.set_dashes([2 , 2 , 10 , 2])

plt.show()















#%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)

fig , ax = plt.subplots()


ax.plot(x , x + 1 , color = 'blue' , lw = 2 , linestyle = '-')

ax.plot(x , x + 2 , color = 'red' , lw = 2 , linestyle = '-')

ax.plot(x , x + 3 , color = 'orange' , lw = 2 , linestyle = ':')


line, = ax.plot(x , x + 4 , color = 'black' , lw = 2)
line.set_dashes([5 , 10 , 20 , 15])


plt.show()














fig , ax = plt.subplots(dpi = 100)

ax.plot(x , x + 1 , color = 'blue' , marker = 'o')

ax.plot(x , x + 2 , color = 'red' , marker = 's')

ax.plot(x , x + 3 , color = 'blue' , marker = '+')

ax.plot(x , x + 4 , color = 'red' , marker = 'x')

plt.show()













fig , ax = plt.subplots(dpi = 100)

ax.plot(x , x + 5 , color = 'blue' , marker = 'o' , markersize = '5' , markerfacecolor = "red")

ax.plot(x , x + 6 , color = 'yellow' , marker = 's' , markersize = '4' , markerfacecolor = 'blue')

ax.plot(x , x + 7 , color = 'red' , marker = '+' , markersize = '6' , markerfacecolor = 'violet')

ax.plot(x , x + 8 , color = 'green' , marker = 's' , markersize = '7' , markerfacecolor = 'black')


plt.show()
