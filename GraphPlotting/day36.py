print("You miss the old me go find him , he is burried under everything you did.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [2 , 7 , 9]
y2 = [4 , 8 , 1]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')

pylab.show()











pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()