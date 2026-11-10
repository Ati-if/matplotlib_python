print("It's survival of the fittest in this world filled with violence , deception and betrayel.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [5 , 9 , 11]
y2 = [1 , 7 , 9]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g+-')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y--')

pylab.show()









pylab.subplot(2 , 4 , 3)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'b+-')

pylab.show()









pylab.subplot(2 , 2 , 4)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'g--')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y+-')

pylab.show()









from matplotlib import pyplot as plt 

fig = pylab.figure()

axis = fig.add_axes([0.2 , 0.2 , 0.4 , 0.4])

axis.plot(x , y , 'r--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')


pylab.show()











fig , axes = plt.subplots(nrows = 4 , ncols = 6)

for ax in axes.flat :
    ax.plot(x , y , 'b--')

plt.show()














fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'b--')
    ax.set_title('Graph')
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')

plt.show()













fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis2 = fig.add_axes([0.2 , 0.2 , 0.4 , 0.5])

axis1.plot(x , y , 'r--')
axis2.plot(y , x , 'b+-')

pylab.show()