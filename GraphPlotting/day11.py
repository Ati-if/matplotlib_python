print("Hello Everyone! This is Atif continuing to learn python .")











from matplotlib import style
style.use ('ggplot')

x = [2 , 4 , 6]
y = (12 , 14 , 16)



x2 = [3 , 5 , 7]
y2 = [7 , 14 , 18]











#Drawing a subgraph

from matplotlib import pylab

pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'b+-')

pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'o--')

pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y+-')

pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'b+-')


pylab.show()











pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'r--')


pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'o--')


pylab.show()