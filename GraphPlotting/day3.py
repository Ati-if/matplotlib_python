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









import numpy as np
import pylab

# Define x and y data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 1st Box (Top-Left)
pylab.subplot(2, 2, 1)
pylab.plot(x, y, "r--")
pylab.title("Plot 1")

# 2nd Box (Top-Right)
pylab.subplot(2, 2, 2)
pylab.plot(y, x, "b--")
pylab.title("Plot 2")

# 3rd Box (Bottom-Left)
pylab.subplot(2, 2, 3)
pylab.plot(x, y, "g--")
pylab.title("Plot 3")

# 4th Box (Bottom-Right)
pylab.subplot(2, 2, 4)
pylab.plot(y, x, "y--")
pylab.title("Plot 4")

# Adjust spacing so titles and labels don't overlap
pylab.tight_layout()

# Display the figure
pylab.show()












#Drawing a subgraph

pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 3 , 2)
pylab.plot(y , x , 'g--')

pylab.show()









#Drawing a subgraph

pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()









#Drawing a subgraph

pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'g+-')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y--')

pylab.show()











#(1 , 2 , 1) and (2 , 1 , 2) are significant if we want tiled subplots , without which both the graphs will be in the same plot

# For example

pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'y+-')

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b-+')

pylab.show()











pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')
pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g+-')

pylab.show()