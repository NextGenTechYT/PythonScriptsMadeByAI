import matplotlib.pyplot as plt

# Data for the graph
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Create the plot
plt.plot(x, y, color='red', linestyle='dotted', marker='o')

# Add axis labels and a title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('A Simple Graph')

# Show the plot
plt.show()
