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