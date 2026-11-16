print("Put me down gave me the runaround now just look at what you've done.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [1 , 3 , 7]
y2 = [10 , 12 , 14]











from matplotlib import pylab 
from matplotlib import pyplot as plt

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()












pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'b--')

pylab.show()