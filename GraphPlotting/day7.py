print("Hello Everyone! This is day 7 of learning Python .")










from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0 , 10 , 100)


fig , axes = plt.subplots(1 , 5 , figsize = (10 , 20))

ax = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8] , polar = True)

plt.show()













fig = plt.figure()

ax = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8] , polar = True)

plt.show()














fig = plt.figure()

ax = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8] , polar = True)

t = np.linspace(0 , 2 * np.pi , 100)

ax.plot(t , t * 5 , color = 'blue' , lw = 3)

plt.show()