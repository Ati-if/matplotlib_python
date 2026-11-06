print("Hello World! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [8 , 10 , 12]
y2 = [9 , 11 , 13]









from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()










from matplotlib import pyplot as plt 

fig = plt.figure()

axis = fig.add_axes([0.1 , 0.1 , 0.4 , 0.4])
axis.plot(x , y , 'r--')

axis.set_xlabel('X-Axis')
axis.set_ylabel('Y-Axis')
axis.set_title('Graph Plotting')
plt.show()












fig , axes = plt.subplots(nrows = 2 , ncols = 2)

for ax in axes.flat :
    ax.plot(x , y , 'r--')
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_title('Graph Plotting')

plt.show()













fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'r--')
    ax.set_xlabel('X-Axis')
    ax.set_ylabel('Y-Axis')
    ax.set_title('Graph')

plt.tight_layout()
plt.show()











from matplotlib import pylab 

fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.4 , 0.4])
axis2 = fig.add_axes([0.5 , 0.4 , 0.3 , 0.2])

axis1.plot(x , y , 'r--')
axis1.set_xlabel('X-Axis')
axis1.set_ylabel('Y-Axis')
axis1.set_title('Plotting')

axis2.plot(x2 , y2 , 'b--')
axis2.set_xlabel('X-Axis')
axis2.set_ylabel('Y-Axis')
axis2.set_title('Plotting')

pylab.show()