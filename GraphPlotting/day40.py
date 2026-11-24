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













pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'g+-')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'y+-')

pylab.show()











from matplotlib import pyplot as plt
from matplotlib import pylab 

fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis2 = fig.add_axes([0.4 , 0.2 , 0.1 , 0.5])

axis1.plot(x , y , 'g--')
axis2.plot(y , x , 'r+-')

pylab.show()














fig , axes = plt.subplots()

axes.plot(x , y , 'g--')
axes.set_xlabel('X-label')
axes.set_ylabel('Y-label')
axes.set_title('Graph')


plt.show()