print("Hello Everyone! This is Atif continuing to learn python plotting.")










from matplotlib import style

style.use ('ggplot')

x = [2 , 4 , 6]
y = [12 , 13 , 14]

x2 = [3 , 5 , 7]
y2 = [4 , 7 , 9]











from matplotlib import pylab

pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'r--')

pylab.show()













pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'r')

pylab.show()