from cProfile import label
from msilib.schema import Class
import sqlite3
import matplotlib.pyplot as plt
import pandas
dbname= 'sensorsdata.db'
conn=sqlite3.connect(dbname)
curs = conn.cursor()
curs.execute("SELECT TimeOfHit.timestamp, x, y, z FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.timestamp = TimeOfHit.timestamp WHERE pole = 'LEFT';")
leftResults = curs.fetchall()
# print(leftResults)

        # for leftResults in results:
sql = """SELECT timestamp from ACC_data WHERE timestamp != ? ORDER BY timestamp DESC LIMIT 100;""", (leftResults)
            # curs.execute("SELECT timestamp from ACC_data WHERE timestamp != '2022-03-29 18:17:47' ORDER BY timestamp DESC LIMIT 100;", (leftResults))
data = pandas.read_sql(sql, conn)
f = plt.figure()
plt.plot(data.timestamp, data.x, label = "X Coords")
plt.plot(data.timestamp, data.y, label = "Y Coords")
plt.plot(data.timestamp, data.z, label = "Z Coords")
plt.legend()
plt.title("Left Pole")
plt.xlabel("Time")
plt.ylabel("Accelration")
ax = plt.gca()
ax.axes.xasis.set_ticks([])
plt.show
f.savefig("foo.pdf")
