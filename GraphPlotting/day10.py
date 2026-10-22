print("Hello Everyone! This is Atif continuing to practice python.")








from matplotlib import style
style.use ('ggplot')

x = [2 , 4 , 6]
y = (12 , 14 , 16)



x2 = [3 , 5 , 7]
y2 = [7 , 14 , 18]








import matplotlib.pyplot as plt

plt.bar (x , y , label = 'Bar1' , color = 'orange')

plt.bar (x2 , y2 , label = 'Bar2' , color = 'red')

plt.xlabel ('Bar Number')

plt.ylabel ('Bar Height')

plt.title('Bar Chart')

plt.legend()
plt.show()










import numpy as np

s = np.array([2 , 4 , 6])

plt.pie(s , labels = ['A' , 'B' , 'C'])

plt.show()
print(s)










from matplotlib import pylab

print(pylab.__version__)