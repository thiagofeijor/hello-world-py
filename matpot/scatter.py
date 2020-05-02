import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

plt.title("Hello matpot")

plt.xlabel("Axis X")
plt.ylabel("Axis Y")

plt.scatter(x, y, color="red", marker="h", s=100)
plt.plot(x, y, linestyle=":")

plt.show()
