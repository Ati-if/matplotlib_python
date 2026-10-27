print("Hello Everyone! This is Atif continuing to learn python .")










from matplotlib import style

style.use ('ggplot')

x = [2 , 4 , 6]
y = [12 , 14 , 16]


x2 = [2 , 3 , 5]
y2 = [8 , 9 , 7]










import matplotlib.pyplot as plt

plt.bar (x , y , label = 'Bar1' , color = 'g')
plt.bar (x2 , y2 , label = 'Bar2' , color = 'b')


plt.xlabel ('Bar Number')
plt.ylabel ('Bar Height')
plt.title ('Bar Chart')

plt.legend()
plt.show()