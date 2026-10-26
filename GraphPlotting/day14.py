print("Hello Everyone! This is Atif continuing to learn python.")








from matplotlib import style

style.use('ggplot')


x = [2 , 4 , 6]
y = [12 , 14 , 16]


x2 = [3 , 6 , 8]
y2 = [7 , 14 , 16]









from matplotlib import pylab

pylab.plot(x , y , 'b--' , 'R')
pylab.show()








pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'y--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'o--')


pylab.show()
