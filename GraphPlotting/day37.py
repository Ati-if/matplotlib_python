print("This is Atif continuing to learn python graph plotting")








import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0 , 10 , 100)

fig , axes = plt.subplots(dpi = 150)
axes.plot(x , x + 1 , color = 'blue' , linewidth = 2)
axes.plot(x , x + 2 , color = 'red' , linewidth = 2)
axes.plot(x , x + 3 , color = 'orange' , linewidth = 2)
axes.plot(x , x + 4 , color = 'yellow' , linewidth = 2)

plt.show()