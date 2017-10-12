import matplotlib.pyplot as plt

# input_values = list(range(1, 6))
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, edgecolors='none', s=40)
plt.title("Cubed numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)
plt.axis([0, 5001, 0, 5001**3])
plt.savefig('cubed_plot_loose.png')
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()


plt.show()