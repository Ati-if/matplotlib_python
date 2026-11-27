print("People only care when they need something from you.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [7 , 9 , 11]
y2 = [11 , 13 , 15]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'g+-')

pylab.show()









pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'r')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'g--')

pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'r--')

pylab.show()