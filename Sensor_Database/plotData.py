import sqlite3
import pandas
import matplotlib.pyplot as plt




dbname = 'sensorsdata.db'
conn = sqlite3.connect(dbname)
sql = """SELECT * from ACC_data ORDER BY timestamp"""


data = pandas.read_sql(sql, conn)
# data.info()

plt.plot(data.timestamp, data.x, label = "X Coords")
plt.plot(data.timestamp, data.y, label = "Y Coords")
plt.plot(data.timestamp, data.z, label = "Z Coords")
plt.plot(data.timestamp, data.x2, label = "X 2 Coords")
plt.plot(data.timestamp, data.y2, label = "Y 2 Coords")
plt.plot(data.timestamp, data.z2, label = "Z 2 Coords")
plt.legend()
plt.title("Right Pole")
plt.xlabel("Time")
plt.ylabel("Acceleration")
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
plt.show()