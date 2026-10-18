print("Hello World!This is Atif , continuing to learn python.")










from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0 , 10 , 100)


fig , axes = plt.subplots(dpi = 100)


axes.plot(x , x + 3 , color = 'red' , marker = 'o' , markersize = '5' , markerfacecolor = 'blue')

plt.show()