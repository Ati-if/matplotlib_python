print("Hello Everyone,This is the third day of plotting graphs using python. ") 






#Drawing a subgraph
import numpy as np
import pylab

x = np.linspace(0 , 10  , 100)
y = np.sin(x)

pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 2 , 3)
pylab.plot(y , x , 'b--')
pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'g--')
pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y--')

pylab.show()









