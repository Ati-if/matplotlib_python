print("Hello World! This is Atif continuing to learn python.")





from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [8 , 10 , 12]
y2 = [9 , 11 , 13]










from matplotlib import pyplot as plt

fig = plt.figure()
axis = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])
axis.plot(x , y , 'b--')
axis.plot(x2 , y2 , 'r--')

axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')

plt.show()














fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'b--')

plt.show()













from matplotlib import pylab
fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])
axis2 = fig.add_axes([0.2 , 0.4 , 0.3 , 0.5])

axis1.plot(x , y , 'b--')
axis2.plot(y , x , 'r--')

pylab.show()













pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 3)
pylab.plot(y , x , 'r--')

pylab.show()












fig = pylab.figure()

fig.add_subplot(2 , 1 , 2)

plt.plot(x , y , 'b--')
plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.title('Title')

plt.show()













fig = pylab.figure(figsize = (8 , 4) , dpi = 100)

fig.add_subplot(2 , 1 , 2)

plt.plot(x , y , 'y--')

pylab.show()