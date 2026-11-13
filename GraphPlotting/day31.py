print("It's survival of the fittest in this world filled with violence , deception and betrayel.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [2 , 7 , 9]
y2 = [5 , 8 , 10]













from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()

















pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()













from matplotlib import pyplot as plt 
from matplotlib import pylab 

fig = pylab.figure()
axis = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])

axis.plot(x , y , 'g--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Graph')

pylab.show()












fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'y--')

plt.show()














fig , axes = plt.subplots(nrows = 3 , ncols = 6)

for ax in axes.flat :
    ax.set_title('Set')
    ax.plot(x , y , 'r--')

plt.show()

















#Draw a picture or graph inside another graph
fig = pylab.figure()
axis1 = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])  #big axis
axis2 = fig.add_axes([0.2 , 0.5 , 0.3 , 0.4])  #small canvas
axis1.plot(x , y , 'b')
axis2.plot(y , x , 'r')

pylab.show()