print("You fix one broken thing and find five more to take its place.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [7 , 9 , 10]
y2 = [11 , 13 , 15]













from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')

pylab.show()













pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()













pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'y+-')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'g--')

pylab.show()

















pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'r+-')

pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'y--')

pylab.show()














from matplotlib import pyplot as plt 

fig = pylab.figure()

axis = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis.plot(x , y , 'r--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Graph')

plt.show()



















fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'g--')
    ax.set_xlabel('X-label')
    ax.set_ylabel('Y-label')


plt.show()