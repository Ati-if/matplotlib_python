print("Hello Everyone! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [8 , 10 , 12]
y2 = [9 , 11 , 13]











from matplotlib import pylab 

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.show()











pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'b+-')

pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 1 , 1)
pylab.plot(y , x , 'r+-')

pylab.show()











from matplotlib import pyplot as plt 

fig = pylab.figure()
axis = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis.plot(x , y , 'b--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Graph')

plt.show()












fig , axes = plt.subplots(nrows = 2 , ncols = 4)

for ax in axes.flat :
    ax.plot(x , y , 'b--')

plt.show()