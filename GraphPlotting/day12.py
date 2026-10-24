print("Hello Everyone! This is Atif continuing to learn python .")








from matplotlib import style
style.use ('ggplot')

x = [2 , 4 , 6]
y = (12 , 14 , 16)



x2 = [3 , 5 , 7]
y2 = [7 , 14 , 18]










from matplotlib import pylab

pylab.plot(x , y , 'g' , 'r')

pylab.show()













import pylab

# Dummy data for x and y to make it runnable
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# 1. Bottom plot of a 2x1 grid (Row 2, Col 1, Index 2)
pylab.subplot(2, 1, 2)
pylab.plot(x, y, "r")

# 2. Top-left plot of a 2x2 grid (Row 1, Col 1, Index 1)
pylab.subplot(2, 2, 1)
pylab.plot(y, x, "b--")

# 3. FIXED: Changed to (2, 2, 3) so it fits a 2x2 grid (Bottom-Left)
pylab.subplot(2, 2, 3)
pylab.plot(x, y, "b")

# 4. Bottom-right plot of a 2x2 grid (Row 2, Col 2, Index 4)
pylab.subplot(2, 2, 4)
pylab.plot(y, x, "r--")

pylab.show()













pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'r--')


pylab.show()











pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'r--')


pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'b--')


pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(1 , 2 , 2)
pylab.plot(y , x , 'b+-')

pylab.show()











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'y+-')

pylab.show()