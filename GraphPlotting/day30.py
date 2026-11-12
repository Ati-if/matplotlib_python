print("Hello World! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [3 , 6 , 9]
y2 = [5 , 8 , 3]











from matplotlib import pyplot as plt 
from matplotlib import pylab 

fig = pylab.figure()

axis1 = fig.add_axes([0.2 , 0.3 , 0.4 , 0.5])
axis2 = fig.add_axes([0.6 , 0.1 , 0.6 , 0.8])

axis1.plot(x , y , 'b--')
axis2.plot(y , x , 'g+-')

pylab.show()














fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.8 , 0.8])
axis2 = fig.add_axes([0.2 , 0.4 , 0.3 , 0.5])

axis1.plot(x , y , 'y--')
axis2.plot(y , x , 'r+-')

pylab.show()