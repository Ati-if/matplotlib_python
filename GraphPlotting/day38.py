print("I stopped expecting loyalty , I stopped asking to be understand.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [7 , 9 , 11]
y2 = [4 , 6 , 8]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y+-')

pylab.show()













import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0 , 10 , 100)

fig , axes = plt.subplots()

linestyles = ['-' , '--' , ':' , '-.'] 

axes.plot(x , x + 1 , color = 'red' , lw = 2 , linestyle = linestyles[0])
axes.plot(x , x + 2 , color = 'green' , lw = 2 , linestyle = linestyles[1])
axes.plot(x , x + 3 , color = 'yellow' , lw = 2 , linestyle = linestyles[2])
axes.plot(x , x + 4 , color = 'orange' , lw = 2 , linestyle = linestyles[3])

plt.show()














fig , ax = plt.subplot(dpi = 150)

ax.plot(x , x + 1 , color = 'red' , lw = 2 , linestyle = '-')
ax.plot(x , x + 2 , color = 'blue' , lw = 2 , linestyle = '--')
ax.plot(x , x + 3 , color = 'green' , lw = 2 , linestyle = '-.')

line, = ax.plot(x , x + 4 , color = 'orange' , lw = 2.5)
line.set_dashes([5 , 10 , 15 , 20]) 

plt.show()