print("Put me down gave me the runaround now just look at what you've done.")








from matplotlib import style 

style.use ('ggplot')

x = [2 , 4 , 6]
y = [3 , 5 , 7]

x2 = [1 , 3 , 7]
y2 = [10 , 12 , 14]











from matplotlib import pylab 
from matplotlib import pyplot as plt

pylab.subplot(2 , 1 , 2)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 2 , 2)
pylab.plot(y , x , 'g+-')

pylab.show()












pylab.subplot(2 , 1 , 1)
pylab.plot(x , y , 'r--')

pylab.subplot(2 , 1 , 2)
pylab.plot(y , x , 'b--')

pylab.show()









fig , axes = plt.subplots()

axes.plot(x , y , 'g--')
axes.set_xlabel('X-label')
axes.set_ylabel('Y-label')
axes.set_title('Title')

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















#In matplotlib we can set other properties such as line colour, transparency and more.
fig ,  axes = plt.subplots(dpi = 200)
axes.plot(x , x + 1 , color = 'blue' , linewidth = 2)
axes.plot(x , x + 2 , color = 'green' , linewidth = 2)
axes.plot(x , x + 3 , color = 'red' , linewidth = 2)
axes.plot(x , x + 4 , color = 'orange' , linewidth = 2)


plt.show()