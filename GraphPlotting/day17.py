print("Hello Everyone! This is Atif continuing to practice matplot.")








from matplotlib import style

style.use('ggplot')

x = [2 , 4 , 6]
y = [11 , 13 , 17]

x2 = [3 , 5 , 7]
y2 = [3 , 8 , 10]









from matplotlib import pylab

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'b+-')

pylab.show()













pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'y')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'r--')

pylab.show()











pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'r--')


pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b+-')


pylab.show()













pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'r+-')


pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'y--')


pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()