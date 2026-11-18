print("It's survival of the fittest in this world filled with violence , deception and betrayel.")








from matplotlib import style

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [3 , 7 , 9]
y2 = [10 , 12 , 14]














from matplotlib import pyplot as plt 
from matplotlib import pylab 

fig = pylab.figure()
axis = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])

axis.plot(x , y , 'b--')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')

pylab.show()











fig , axes = plt.subplots(nrows = 3 , ncols = 5)

for ax in axes.flat :
    ax.plot(x , y , 'r+-')

plt.show()










pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'g--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'b+-')

pylab.show()