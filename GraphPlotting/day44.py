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