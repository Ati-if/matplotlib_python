print("Hello Everyone! This is Atif continuing to learn python.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [9 , 11 , 7]
y2 = [10 , 12 , 14]











from matplotlib import pyplot as plt 
from matplotlib import pylab 

fig = pylab.figure()

axis1 = fig.add_axes([0.1 , 0.2 , 0.3 , 0.4])
axis2 = fig.add_axes([0.5 , 0.6 , 0.7 , 0.8])

axis1.plot(x , y , 'b--')
axis2.plot(y , x , 'r+-')

pylab.show()










fig = pylab.figure()

fig.add_subplot()

plt.plot(x , y , 'b--')
plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.show()














fig = pylab.figure(figsize = (16 , 10) , dpi = 100)

fig.add_subplot()

plt.plot(x , y , 'g--')
pylab.show()













fig , axes = plt.subplots()

axes.plot(x , y , 'g--')

axes.set_xlabel('X-label')
axes.set_ylabel('Y-label')
axes.set_title('Graph')

plt.show()












fig , axes = plt.subplots()
axes.set_xlabel('X-Label')
axes.set_ylabel('Y-Label')
axes.set_title('Title')
axes.plot(x , [value ** 2 for value in x] , label = 'X-Squared')
axes.plot(x , [value ** 3 for value in x] , label = 'X-Cubed')
axes.legend()

plt.show()






















import matplotlib.pyplot as plt
import numpy as np

# 1. Define your data
x = np.linspace(0, 5, 100)

# 2. Create the figure and axes first
fig, axes = plt.subplots()

# 3. Set labels and title
axes.set_xlabel('X-Label')
axes.set_ylabel('Y-Label')
axes.set_title('Title')

# 4. Plot data with labels
axes.plot(x, x ** 2, label='X-Squared')
axes.plot(x, x ** 3, label='X-Cubed')

# 5. Call legend() with parentheses to render it
axes.legend()

plt.show()