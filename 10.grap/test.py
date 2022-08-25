import matplotlib.pyplot as plt

x = ["1M", "2M", "3M"]
y1 = [100, 200, 150]
y2 = [1000, 1100, 1300]

plt.plot(x, y2, color='black', linewidth=4)

plt.bar(x, y1, color='blue')

plt.show()
