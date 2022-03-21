import csv
import matplotlib.pyplot as plt
import pandas

# time = []
# x = []
# y = []
# z = []

# with open('test.csv', 'r') as File:
#     lines = csv.reader(File, delimiter=',')
#     for row in lines:
#         time.append(row[0])
#         x.append(row[1])
        # y.append(row[2])
        # z.append(row[3])

data = pandas.read_csv('test.csv')
plt.plot(data.TIME, data.X, label = "X2 Coords")
plt.plot(data.TIME, data.Y, label = "Y2 Coords")
plt.plot(data.TIME, data.Z, label = "Z2 Coords")
plt.plot(data.TIME, data.X2, label = "X2 Coords")
plt.plot(data.TIME, data.Y2, label = "Y2 Coords")
plt.plot(data.TIME, data.Z2, label = "Z2 Coords")

plt.legend()
plt.title("HITS")
plt.show()
