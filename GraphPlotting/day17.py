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











pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')
pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g+-')


pylab.show()

















from matplotlib import pyplot as plt
fig = pylab.figure()
axis = fig.add_axes([0.1, 0.1, 0.8, 0.8])    #control left , right , width , height of canvas(from 0 to 1)
axis.plot(x , y , 'b')
axis.set_xlabel('X-Label')
axis.set_ylabel('Y-Label')
axis.set_title('Title')

plt.show()