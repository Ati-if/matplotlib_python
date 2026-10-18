print("Hello World!This is Atif , continuing to learn python.")










from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0 , 10 , 100)


fig , axes = plt.subplots(dpi = 100)


axes.plot(x , x + 3 , color = 'red' , marker = 'o' , markersize = '5' , markerfacecolor = 'blue')

plt.show()











fig , axes = plt.subplots(1 , 2  ,  figsize = (10 , 5))

axes[0].plot(x , x + 14 , color = 'red' , marker = 'o' , markersize = '5' ,  markerfacecolor = 'blue')

axes[1].plot(x , x + 15 , color = 'blue' , marker = 'o' , markersize = '6' , markerfacecolor = 'yellow')

axes[0].plot(x , x ** 2 , x ** 3 , lw = '2')
axes[0].set_title('Title')
axes[0].grid(True)

axes[1].plot(x , x ** 2 , x ** 3 , lw = '4')
axes[1].set_title('Title')
axes[1].grid(True)

plt.show()











import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)




fig , axes = plt.subplots(1 , 2 , figsize = (10 , 5))



axes[0].plot(x , x ** 3 , x ** 4 , lw = '3')
axes[0].set_ylim(0 , 50)
axes[0].set_xlim(0 , 50)
axes[0].grid(True)

axes[1].plot(x , x ** 2 , x ** 3 , lw = '4')
axes[1].set_ylim(0 , 60)
axes[1].set_xlim(0 , 60)
axes[1].grid(True)

plt.show()













import matplotlib.pyplot as plt
import numpy as np

# Example definition of x (if not already defined)
x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# First subplot: Plotting x^3 and x^4 as separate lines
axes[0].plot(x, x**3, label='x^3', lw=3)
axes[0].plot(x, x**4, label='x^4', lw=3)
axes[0].set_ylim(0, 50)
axes[0].set_xlim(0, 50)
axes[0].grid(True)  # Fixed: used parentheses instead of brackets
axes[0].legend()

# Second subplot: Plotting x^2 and x^3 as separate lines
axes[1].plot(x, x**2, label='x^2', lw=4)
axes[1].plot(x, x**3, label='x^3', lw=4)
axes[1].set_ylim(0, 60)
axes[1].set_xlim(0, 60)
axes[1].grid(True)  # Fixed: used parentheses instead of brackets
axes[1].legend()

plt.tight_layout()
plt.show()