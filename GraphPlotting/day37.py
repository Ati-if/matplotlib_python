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










axes.legend(['label1' , 'label2' , 'label3'])

fig , axes = plt.subplots(dpi = 150) 

axes.set_xlabel('X-label')
axes.set_ylabel('Y-label')
axes.set_title('Graph')

axes.plot(x , x ** 2 , label = 'X-Squared')
axes.plot(x , x ** 3 , label = 'X-Cubed')
axes.legend()

plt.show()











fig , axes = plt.subplots(dpi = 150)

axes.plot(x , x ** 2 , color = 'blue' , alpha = 1 , linewidth = 2)
axes.plot(x , x ** 3 , color = 'red' , alpha = 1 , linewidth = 2)
axes.plot(x , x ** 1 , color = 'green' , alpha = 0.5 , linewidth = 2)
axes.plot(x , x ** 2.5 , color = 'yellow' , alpha = 0.7 , linewidth = 2)

plt.show()