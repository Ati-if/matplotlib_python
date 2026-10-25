print("This is Atif continuing to learn Python .")










from matplotlib import style

style.use ('ggplot')


x = [2 , 4 , 6]
y = [12 , 14 , 16]

x2 = [3 , 6 , 8]
y2 = [7 , 14 , 18]










from matplotlib import pylab 
pylab.plot(x , y , 'b' , 'y')
pylab.show()