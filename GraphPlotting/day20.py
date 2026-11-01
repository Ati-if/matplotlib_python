print("Hello World! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [8 , 10 , 12]
y2 = [9 , 11 , 13]









from matplotlib import pylab 

pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 3 , 2)
pylab.plot(y , x , 'r--')

pylab.show()













pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'y--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g--')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.subplot(2 , 2 , 4)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 3)
pylab.plot(y , x , 'y+-')

pylab.show()














pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'y--')


pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b+-')

pylab.subplot(2 , 2 , 3)
pylab.plot(y , x , 'g--')

pylab.subplot(2 , 2 , 4)
pylab.plot(x , y , 'r+-')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y--')

pylab.show()