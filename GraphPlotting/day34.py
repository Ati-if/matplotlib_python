print("Every door you shut on me taught me how to feel nothing.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [4 , 7 , 9]
y2 = [1 , 8 , 10]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'g+-')

pylab.show()