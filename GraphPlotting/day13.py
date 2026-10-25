print("This is Atif continuing to learn Python .")










from matplotlib import style

style.use ('ggplot')


x = [2 , 4 , 6]
y = [12 , 14 , 16]

x2 = [3 , 6 , 8]
y2 = [7 , 14 , 18]










from matplotlib import pylab 
pylab.plot(x , y , 'b' , 'y')
pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')


pylab.show()











"""Drawing a subgraph"""
pylab.subplot(2 , 2 , 1) # The content of the brackets represent(rows , columns , indexes)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g--')
pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'b--')
pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y--')


pylab.show()












#Drawing a subgraph

pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')


pylab.show()











#Drawing a subgraph

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')


pylab.show()















pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r+-')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'b--')


pylab.show()
















pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'o--')


pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y+-')


pylab.show()















pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y--')


pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'b+-')

pylab.show()