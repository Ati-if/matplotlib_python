print("Hello Everyone! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [8 , 10 , 12]
y2 = [9 , 11 , 13]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.show()









pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()














pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')
pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g+-')

pylab.show()













pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()













from matplotlib import pyplot as plt

fig = plt.figure()

axis = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])
axis.plot(x , y , 'r--')
axis.set_xlabel('X-Axis')
axis.set_ylabel('Y-Axis')
axis.set_title('Graph Plotting')

plt.show()