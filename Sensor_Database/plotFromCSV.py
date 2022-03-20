import csv
import matplotlib.pyplot as plt
import pandas

time = []
x = []
y = []
z = []

with open('test.csv', 'r') as File:
    lines = csv.reader(File, delimiter=',')
    for row in lines:
        time.append(row[0])
        x.append(row[1])
        y.append(row[2])
        z.append(row[3])

plt.plot(time, x, label = "X Coords")
plt.plot(time, y, label = "y Coords")
plt.plot(time, z, label = "z Coords")

plt.legend()
plt.title("HITS")
plt.show()
