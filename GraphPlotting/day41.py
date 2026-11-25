print("I push away the people I love the most .")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [5 , 7 , 9]
y2 = [9 , 11 , 13]











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













fig , axes = plt.subplots(dpi = 150)

axes.plot(x , x + 1 , color = 'red' , lw = 2 , marker = 'o')
axes.plot(x , x + 2 , color = 'blue' , lw = 2 , marker = '+')
axes.plot(x , x + 3 , color = 'yellow' , lw = 2 , marker = 's')
axes.plot(x , x + 4 , color = 'orange' , lw = 2 , marker = 'x')

plt.show()














fig , axes = plt.subplots(dpi = 150)

axes.plot(x , x + 1 , color = 'red' , linewidth = 2)
axes.plot(x , x + 2 , color = 'blue' , linewidth = 2.5)
axes.plot(x , x + 3 , color = 'green' , linewidth = 2) 
axes.plot(x , x + 4 , color = 'orange' , linewidth = 2)


plt.show()













fig , axes = plt.subplots(dpi = 150) 

axes.plot(x , x ** 2 , color = 'blue' , alpha = 0.8 , linewidth = 2)
axes.plot(x , x ** 1 , color = 'red' , alpha = 1 , linewidth = 2.5)
axes.plot(x , x ** 3 , color = 'orange' , alpha = 0.5 , linewidth = 2)
axes.plot(x , x ** 4 , color = 'green' , alpha = 0.7 , linewidth = 2)


plt.show()