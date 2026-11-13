print("It's survival of the fittest in this world filled with violence , deception and betrayel.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [2 , 7 , 9]
y2 = [5 , 8 , 10]













from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()

















pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()