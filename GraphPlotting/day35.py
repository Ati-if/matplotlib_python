print("It's survival of the fittest in this world filled with violence , deception and betrayel.")








from matplotlib import style

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [3 , 7 , 9]
y2 = [10 , 12 , 14]














from matplotlib import pyplot as plt 
from matplotlib import pylab 

fig = pylab.figure()
axis = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])

axis.plot(x , y , 'b--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')

pylab.show()











fig , axes = plt.subplots(nrows = 3 , ncols = 5)

for ax in axes.flat :
    ax.plot(x , y , 'r+-')

plt.show()










pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'b+-')

pylab.show()















pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()













fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'g--')
    ax.set_title('Graph')
    ax.set_xlabel('X-label')
    ax.set_ylabel('Ylabel')

plt.show()













fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis2 = fig.add_axes([0.4 , 0.5 , 0.1 , 0.2])

axis1.plot(x , y , 'g+-')
axis1.plot(y , x , 'r--')

pylab.show()













fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])
axis2 = fig.add_axes([0.2 , 0.3 , 0.4 , 0.5])

axis1.plot(x , y , 'b+-')
axis2.plot(y , x , 'g+-')

pylab.show()













pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()













#In matplotlib we can set other properties such as line colour, transparency and more.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)

fig ,  axes = plt.subplots(dpi = 150)
axes.plot(x , x + 1 , color = 'blue' , linewidth = 2)
axes.plot(x , x + 2 , color = 'green' , linewidth = 2)
axes.plot(x , x + 3 , color = 'red' , linewidth = 2)
axes.plot(x , x + 4 , color = 'orange' , linewidth = 2)


plt.show()