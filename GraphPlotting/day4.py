print("Hello Everyone! This is the 4th day of plotting graphs using matplotlib")








from matplotlib import pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

fig = plt.figure()

axis = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])

axis.plot(x , y , 'b')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')

plt.show()









fig , axes = plt.subplots(nrows = 3 , ncols = 4)

for ax  in axes.flat :
    ax.plot(x , y , 'b')


plt.show()









fig , axes = plt.subplots(nrows = 4 , ncols = 4)


for ax in axes.flat :
    ax.set_title('Title')

    ax.plot(x , y , 'r')

plt.show()









#Draw a picture or graph inside a graph

import numpy as np 
import pylab

x = np.linspace(0 , 10 , 100)
y = np.sin(x)

fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])
axis2 = fig.add_axes([0.2 , 0.4 , 0.3 , 0.5])

axis1.plot(x , y , 'b')
axis2.plot(y , x , 'r')

pylab.show()











fig = pylab.figure()

fig.add_subplot()

plt.plot(x , y , 'b')

plt.xlabel('X-label')

plt.ylabel('Y-label')

plt.title('Title')

plt.show()











fig = pylab.figure(figsize = (16 , 9) , dpi = 140)

fig.add_subplot()

plt.plot(x , y , 'b')

pylab.show()











fig = pylab.figure(figsize = (18 , 8) , dpi = 150)

plt.plot(x , y , 'b')

pylab.show()












fig , axes = plt.subplots()

axes.plot(x , y , 'b')

axes.set_xlabel('X-label')
axes.set_ylabel('Y-label')

axes.set_title('Title')

plt.show()













ax.legend(["label1" , "label2" , "label3"])

fig , axes = plt.subplots()

axes.set_xlabel('Xlabel')
axes.set_ylabel('Ylabel')

axes.set_title('Title')


axes.plot(x , x ** 2 , label = 'X-squared')
axes.plot(x , x ** 3 , label = 'Y-squared')

axes.legend()

plt.show()