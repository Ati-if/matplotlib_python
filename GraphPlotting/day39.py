print("Maybe I am the problem , Maybe I am the curse , Maybe every version of me only gets worse.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [5 , 7 , 9]
y2 = [10 , 12 , 14]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'y+-')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g--')

pylab.show()













import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0 , 10 , 100)

fig , axes = plt.subplots(dpi = 150)

linestyles = ['-' , '--' , '-.' , ':'] 

axes.plot(x , x + 1 , color = 'red' , lw = 2 , linestyle = linestyles[0])
axes.plot(x , x + 2 , color = 'blue' , lw = 2 , linestyle = linestyles[1])
axes.plot(x , x + 3 , color = 'orange' , lw = 2.5 , linestyle = linestyles[2])
axes.plot(x , x + 4 , color = 'black' , lw = 2 , linestyle = linestyles[3])

plt.show()