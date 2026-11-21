print("This is Atif continuing to learn python graph plotting")








import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0 , 10 , 100)

fig , axes = plt.subplots(dpi = 150)
axes.plot(x , x + 1 , color = 'blue' , linewidth = 2)
axes.plot(x , x + 2 , color = 'red' , linewidth = 2)
axes.plot(x , x + 3 , color = 'orange' , linewidth = 2)
axes.plot(x , x + 4 , color = 'yellow' , linewidth = 2)

plt.show()










axes.legend(['label1' , 'label2' , 'label3'])

fig , axes = plt.subplots(dpi = 150) 

axes.set_xlabel('X-label')
axes.set_ylabel('Y-label')
axes.set_title('Graph')

axes.plot(x , x ** 2 , label = 'X-Squared')
axes.plot(x , x ** 3 , label = 'X-Cubed')
axes.legend()

plt.show()











fig , axes = plt.subplots(dpi = 150)

axes.plot(x , x ** 2 , color = 'blue' , alpha = 1 , linewidth = 2)
axes.plot(x , x ** 3 , color = 'red' , alpha = 1 , linewidth = 2)
axes.plot(x , x ** 1 , color = 'green' , alpha = 0.5 , linewidth = 2)
axes.plot(x , x ** 2.5 , color = 'yellow' , alpha = 0.7 , linewidth = 2)

plt.show()












fig , axes = plt.subplots(dpi = 150)

linestyles = ['-' , '--' , '-.' , ':']

axes.plot(x , x + 1 , color = 'blue' , lw = 2 , linestyle = linestyles[0])
axes.plot(x , x + 2 , color = 'red' , lw = 2 , linestyle = linestyles[1])
axes.plot(x , x + 3 , color = 'green' , lw = 2 , linestyle = linestyles[2])
axes.plot(x , x + 4 , color = 'yellow' , lw = 2 , linestyle = linestyles[3])

plt.show()












fig, axes = plt.subplots(dpi=150)

# Define linestyles for blue lines
linestyles = ['-', '--', '-.', ':']

# Plot the four blue lines with increasing y-offsets and different linestyles
axes.plot(x, x + 1, color='blue', lw=2, linestyle=linestyles[0])
axes.plot(x, x + 2, color='blue', lw=2, linestyle=linestyles[1])
axes.plot(x, x + 3, color='blue', lw=2, linestyle=linestyles[2])
axes.plot(x, x + 4, color='blue', lw=2, linestyle=linestyles[3])

# Plot the black line with custom dashing
# The plot function returns a list of Line2D objects, we take the first one [0]
line = axes.plot(x, x + 4, color="black", lw=2)[0] # Changed lw='2' to lw=2
line.set_dashes([2, 2, 10, 2]) # Apply the custom dash pattern as previously intended

plt.show()