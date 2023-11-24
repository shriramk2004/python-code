import matplotlib.pyplot as plt


sizes = [30, 20, 25, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']

# pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6]

# histogram
plt.hist(data, bins=6)  # bins define the number of intervals in the data
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()


categories = ['A', 'B', 'C', 'D']
values = [5, 10, 15, 20]

# bar chart
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# scatter plot
plt.scatter(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Scatter Plot')
plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# line plot
plt.plot(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Line Plot')
plt.show()