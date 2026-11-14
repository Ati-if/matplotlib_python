print("Hello Everyone! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [9 , 11 , 7]
y2 = [10 , 12 , 14]











from matplotlib import pyplot as plt 
from matplotlib import pylab 

fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis2 = fig.add_axes([0.5 , 0.6 , 0.7 , 0.8])

axis1.plot(x , y , 'b--')
axis2.plot(y , x , 'r+-')

pylab.show()