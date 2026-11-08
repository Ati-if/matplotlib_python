print("Hello World! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [7 , 9 , 11]
y2 = [11 , 13 , 15]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')

pylab.show()













pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y--')

pylab.show()











pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'b--')

pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g--')

pylab.show()













pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 3 , 2)
pylab.plot(y , x , 'y--')

pylab.show()












from matplotlib import pyplot as plt
fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.set_title('Graph')
    ax.plot(x , y , 'b--')

plt.show()















fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.1 , 0.2 , 0.4])
axis2 = fig.add_axes([0.3 , 0.5 , 0.6 , 0.7])

axis1.plot(x , y , 'g--')
axis2.plot(y , x , 'r--')

pylab.show()