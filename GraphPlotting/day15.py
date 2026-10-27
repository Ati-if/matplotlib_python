print("Hello Everyone! This is Atif continuing to learn python .")










from matplotlib import style

style.use ('ggplot')

x = [2 , 4 , 6]
y = [12 , 14 , 16]


x2 = [2 , 3 , 5]
y2 = [8 , 9 , 7]










import matplotlib.pyplot as plt

plt.bar (x , y , label = 'Bar1' , color = 'g')
plt.bar (x2 , y2 , label = 'Bar2' , color = 'b')


plt.xlabel ('Bar Number')
plt.ylabel ('Bar Height')
plt.title ('Bar Chart')

plt.legend()
plt.show()










import numpy as np

s = np.array([2 , 4 , 6])

plt.pie(s , labels = ['A' , 'B' , 'C'])

plt.show()
print(s)












from matplotlib import pylab

pylab.plot(x , y , 'b--' , 'r')
pylab.show()












pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'r')

pylab.show()













pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'o--')

pylab.show()













pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'o--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'b')

pylab.show()












"""Drawing a subgraph"""
pylab.subplot(2 , 2 , 1) # The content of the brackets represent(rows , columns , indexes)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g--')
pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'b--')
pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y--')

pylab.show()