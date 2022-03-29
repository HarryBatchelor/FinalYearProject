import sqlite3
import pandas
import matplotlib.pyplot as plt

dbname = 'sensorsdata.db'
conn = sqlite3.connect(dbname)
sql = """SELECT timestamp, X2, Y2, Z2, x, y ,z from ACC_data ORDER BY timestamp"""


data = pandas.read_sql(sql, conn)

Xs = [float(data.X2)]

plt.plot(data.timestamp, Xs, label = "X 2 Coords")
# plt.plot(data.timestamp, data.Y2, label = "Y 2 Coords")
# plt.plot(data.timestamp, data.Z2, label = "Z 2 Coords")
# plt.legend()
# plt.title("Right Pole")
# plt.xlabel("Time")
# plt.ylabel("Acceleration")
# ax = plt.gca()

# ax.axes.xaxis.set_ticks([])
# plt.show()