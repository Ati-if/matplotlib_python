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