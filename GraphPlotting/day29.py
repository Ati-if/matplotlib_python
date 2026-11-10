print("It's survival of the fittest in this world filled with violence , deception and betrayel.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [5 , 9 , 11]
y2 = [1 , 7 , 9]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g+-')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y--')

pylab.show()