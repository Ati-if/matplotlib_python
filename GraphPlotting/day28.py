print("Hello Everyone! This is Atif continuing to learn python plotting.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [4 , 6 , 8]
y2 = [12 , 10 , 9]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y+-')

pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 4 , 2)
pylab.plot(y , x , 'b--')

pylab.show()













from matplotlib import pyplot as plt 

fig = pylab.figure()

axis = fig.add_axes([0.1 , 0.2 , 0.4 , 0.6])

axis.plot(x , y , 'r--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')

pylab.show()










fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'b--')

plt.show()