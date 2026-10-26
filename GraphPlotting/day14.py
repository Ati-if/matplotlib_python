print("Hello Everyone! This is Atif continuing to learn python.")








from matplotlib import style

style.use('ggplot')


x = [2 , 4 , 6]
y = [12 , 14 , 16]


x2 = [3 , 6 , 8]
y2 = [7 , 14 , 16]









from matplotlib import pylab

pylab.plot(x , y , 'b--' , 'R')
pylab.show()








pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'y--')

pylab.subplot(2 , 2 , 1)
pylab.plot(y , x , 'o--')


pylab.show()












pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'b--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'o--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y--')

pylab.show()

















pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'b--')

pylab.show()













pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y--')


pylab.show()














pylab.subplot(2 , 2 , 2)
pylab.plot(x , y , 'r--')


pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'b+-')

pylab.show()










pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'r-+')

pylab.show()















pylab.subplot(1 , 2 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'b+-')



pylab.show()

















 #(1 , 2 , 1) and (2 , 1 , 2) are significant if we want tiled subplots , without which both the graphs will be in the same plot

# For example

pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')
pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'g+-')
pylab.subplot(1 , 2 , 1)
pylab.plot(y , x , 'g+-')


















from matplotlib import pyplot as plt
fig = pylab.figure()
axis = fig.add_axes([0.1, 0.1, 0.8, 0.8])    #control left , right , width , height of canvas(from 0 to 1)
axis.plot(x , y , 'b')
axis.set_xlabel('X-Label')
axis.set_ylabel('Y-Label')
axis.set_title('Title')