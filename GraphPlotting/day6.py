print("Hello World!This is Atif , continuing to learn python.")










from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0 , 10 , 100)


fig , axes = plt.subplots(dpi = 100)


axes.plot(x , x + 3 , color = 'red' , marker = 'o' , markersize = '5' , markerfacecolor = 'blue')

plt.show()











fig , axes = plt.subplots(1 , 2  ,  figsize = (10 , 5))

axes[0].plot(x , x + 14 , color = 'red' , marker = 'o' , markersize = '5' ,  markerfacecolor = 'blue')

axes[1].plot(x , x + 15 , color = 'blue' , marker = 'o' , markersize = '6' , markerfacecolor = 'yellow')

axes[0].plot(x , x ** 2 , x ** 3 , lw = '2')
axes[0].set_title('Title')
axes[0].grid(True)

axes[1].plot(x , x ** 2 , x ** 3 , lw = '4')
axes[1].set_title('Title')
axes[1].grid(True)

plt.show()