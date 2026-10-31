print("Hello World! This is Atif continuing to learn python.")








from matplotlib import style

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [8 , 10 , 12]
y2 = [9 , 11 , 13]











from matplotlib import pylab

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'r')

pylab.show()