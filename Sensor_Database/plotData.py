import sqlite3, pandas, matplotlib.pyplot as plt

dbname = 'sensorsdata.db'
conn = sqlite3.connect(dbname)
sql = """SELECT timestamp, x, y, z from ACC_data ORDER BY timestamp DESC LIMIT 10"""

data = pandas.read_sql(sql, conn)

plt.plot(data.timestamp, data.x, label = "X Coords")
plt.plot(data.timestamp, data.y, label = "Y Coords")
plt.plot(data.timestamp, data.z, label = "Z Coords")
plt.legend()
plt.title("Coords")
plt.show()