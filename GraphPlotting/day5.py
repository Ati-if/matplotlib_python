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



