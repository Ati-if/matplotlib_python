print("I am the monster you created , the nightmare you made.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [7 , 9 , 11]
y2 = [11 , 13 , 15]











from matplotlib import pylab 

pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()













pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'y--')

pylab.subplot(2 , 1 , 1)
pylab.plot(y , x , 'g+-')

pylab.show()













import matplotlib.pyplot as plt 

plt.bar(x , y , label = 'Bar1' , color = 'Grey')
plt.bar(x2 , y2 , label = 'Bar2' , color = 'black')

plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Bar Chart')

plt.legend()
plt.show()













import numpy as np 

s = np.array([2 , 3 , 4])

plt.pie(s , labels = ['A' , 'B' , 'C'])

plt.show()
print(s)














import matplotlib.pyplot as plt
import numpy as np

s = np.array([2, 3, 4])

custom_colors = ["#ff6b6b", "#4ecdc4", "#ffe66d"]

plt.pie(s, labels=["A", "B", "C"], colors=custom_colors)
plt.show()
print(s)












pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'y+-')

pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'b--')

pylab.show()












pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')

pylab.show()