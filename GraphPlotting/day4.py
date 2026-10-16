print("Hello Everyone! This is the 4th day of plotting graphs using matplotlib")








from matplotlib import pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

fig = plt.figure()

axis = fig.add_axes([0.1 , 0.1 , 0.8 , 0.8])

axis.plot(x , y , 'b')
axis.set_xlabel('X-label')
axis.set_ylabel('Y-label')
axis.set_title('Title')

plt.show()

