print("A shadow in the light always alone.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [7 , 9 , 11]
y2 = [3 , 4 , 8]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()