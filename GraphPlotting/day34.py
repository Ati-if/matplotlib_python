print("Every door you shut on me taught me how to feel nothing.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [4 , 7 , 9]
y2 = [1 , 8 , 10]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'g+-')

pylab.show()













pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'y--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g--')

pylab.show()













pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'g+-')


pylab.show()















from matplotlib import pyplot as plt 

fig = pylab.figure()

axis = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])

axis.plot(x , y , 'g--')
axis.plot(y , x , 'r--')

axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Graph')
pylab.show()

















fig , axes = plt.subplots(nrows = 3 , ncols = 6)

for ax in axes.flat :
    ax.plot(x , y , 'g--')
    ax.plot(y , x , 'r--')

plt.show()