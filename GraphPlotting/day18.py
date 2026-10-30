print("Hello World!This is Atif continuing to learn python.")








from matplotlib import style

style.use ('ggplot')

x = [2 , 3 , 5]
y = [6 , 8 , 4]

x2 = [5 , 7 , 9]
y2 = [12 , 14 , 16]











from matplotlib import pylab

pylab.subplot(1 , 1 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 1 , 1)
pylab.plot(y , x , 'b+-')

pylab.show()











pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'b--')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'o--')

pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y--')

pylab.show()