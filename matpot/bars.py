import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

x2 = [3, 4, 9]
y2 = [22, 2, 3]

plt.title("Hello matpot")

plt.xlabel("Axis X")
plt.ylabel("Axis Y")

plt.bar(x, y, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()
plt.show()
