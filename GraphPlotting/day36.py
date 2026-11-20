print("You miss the old me go find him , he is burried under everything you did.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [2 , 7 , 9]
y2 = [4 , 8 , 1]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')

pylab.show()











pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()













import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)

fig ,  axes = plt.subplots(dpi = 150)
axes.plot(x , x + 1 , color = 'blue' , linewidth = 2)
axes.plot(x , x + 2 , color = 'green' , linewidth = 2)
axes.plot(x , x + 3 , color = 'red' , linewidth = 2)
axes.plot(x , x + 4 , color = 'orange' , linewidth = 2)


plt.show()













fig , axes = plt.subplots(dpi = 150)

axes.plot(x , x ** 2 , color = 'blue' , alpha = 1 , linewidth = 2)
axes.plot(x , x ** 3 , color = 'red' , alpha = 0.5 , linewidth = 2)
axes.plot(x , x ** 1 , color = 'orange' , alpha = 0.7 , linewidth = 2)
axes.plot(x , x ** 2.5 , color = 'green' , alpha = 1 , linewidth = 2)


plt.show()













fig , axes = plt.subplots(dpi = 150)

linestyles = ['-' , '--' , '-.']

axes.plot(x , x + 1 , color = 'red' , lw = 2 , linestyle = linestyles[0])
axes.plot(x , x + 2 , color = 'blue' , lw = 2 , linestyle = linestyles[1])
axes.plot(x , x + 3 , color = 'orange' , lw = 2 , linestyle = linestyles[2])

plt.show()