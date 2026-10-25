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











pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')


pylab.show()











"""Drawing a subgraph"""
pylab.subplot(2 , 2 , 1) # The content of the brackets represent(rows , columns , indexes)
pylab.plot(x , y , 'r--')
pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g--')
pylab.subplot(2 , 2 , 3)
pylab.plot(x , y , 'b--')
pylab.subplot(2 , 2 , 4)
pylab.plot(y , x , 'y--')


pylab.show()












#Drawing a subgraph

pylab.subplot(2 , 2 , 1)
pylab.plot(x , y , 'b')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r--')


pylab.show()











#Drawing a subgraph

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'b--')


pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'r+-')


pylab.show()















pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r+-')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'b--')


pylab.show()
















pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'o--')


pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y+-')


pylab.show()















pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'y--')


pylab.subplot(1 , 2 , 1)
pylab.plot(x , y , 'b+-')

pylab.show()











import pylab

# Create your data (example)
# x = ...
# y = ...

# Set up a figure with 1 row and 2 columns
pylab.figure(figsize=(10, 4))

# --- First Subplot (Left side) ---
pylab.subplot(1, 2, 1)
pylab.plot(x, y, "r--", label="y vs x (dashed)")
pylab.plot(x, y, "b+-", label="y vs x (blue +)")  # Overlays on the first subplot
pylab.legend()

# --- Second Subplot (Right side) ---
pylab.subplot(1, 2, 2)
pylab.plot(y, x, "g--", label="x vs y")  # or 'y--' depending on your color choice
pylab.legend()

pylab.show()