print("Hello Everyone! This is Atif continuing to practice python.")








from matplotlib import style
style.use ('ggplot')

x = [2 , 4 , 6]
y = (12 , 14 , 16)



x2 = [3 , 5 , 7]
y2 = [7 , 14 , 18]








import matplotlib.pyplot as plt

plt.bar (x , y , label = 'Bar1' , color = 'orange')

plt.bar (x2 , y2 , label = 'Bar2' , color = 'red')

plt.xlabel ('Bar Number')

plt.ylabel ('Bar Height')

plt.title('Bar Chart')

plt.legend()
plt.show()










import numpy as np

s = np.array([2 , 4 , 6])

plt.pie(s , labels = ['A' , 'B' , 'C'])

plt.show()
print(s)










from matplotlib import pylab

print(pylab.__version__)













import numpy as np

x = np.linspace(0 , 10 , 25)

y = x * x + 2

print(x)
print(y)











print(np.array([x , y]) .  reshape(25 , 2))









pylab.plot(x , y , 'g' , 'r')
pylab.show()











#Drawing a subgraph

pylab.subplot(2 , 2 , 4)
pylab.plot(x , y , 'r')

pylab.subplot(2 , 3 , 4)
pylab.plot(y , x , 'g--')

pylab.subplot(2 , 4 , 6)
pylab.plot(x , y , 'b')

pylab.subplot(3 , 5 , 7)
pylab.plot(y , x , 'y--')

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












pylab.subplot(2 , 2 , 1)

pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 3)

pylab.plot(x , y , 'b--')

pylab.show()







import pylab

# Example data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]



pylab.subplot(2 , 2 , 1)

pylab.plot(x , y , 'y--')

pylab.subplots(2 , 1 , 2)

pylab.plot(y , x , 'b+-')

pylab.show()