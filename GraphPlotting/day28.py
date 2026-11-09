print("Hello Everyone! This is Atif continuing to learn python plotting.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [4 , 6 , 8]
y2 = [12 , 10 , 9]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y+-')

pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 4 , 2)
pylab.plot(y , x , 'b--')

pylab.show()