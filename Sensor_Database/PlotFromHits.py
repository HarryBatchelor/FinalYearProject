from cProfile import label
from msilib.schema import Class
import sqlite3
import matplotlib.pyplot as plt
import pandas
dbname= 'sensorsdata.db'
conn=sqlite3.connect(dbname)
conn.row_factory = lambda curs, row: row[0]
curs = conn.cursor()
curs.execute("SELECT TimeOfHit.timestamp FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.timestamp = TimeOfHit.timestamp WHERE pole = 'LEFT';")
leftResults = curs.fetchall()
# print(leftResults)

sql = """SELECT timestamp from ACC_data WHERE timestamp != {seq} ORDER BY timestamp DESC LIMIT 100;""".format(seq=','.join(['?']*len(leftResults))),
conn.row_factory = lambda curs, row: row[0]
curs.execute(sql,leftResults)
# data = pandas.read_sql(sql, conn)
# print (data)
# f = plt.figure()
# plt.plot(data.timestamp, data.x, label = "X Coords")
# plt.plot(data.timestamp, data.y, label = "Y Coords")
# plt.plot(data.timestamp, data.z, label = "Z Coords")
# plt.legend()
# plt.title("Left Pole")
# plt.xlabel("Time")
# plt.ylabel("Accelration")
# ax = plt.gca()
# ax.axes.xasis.set_ticks([])
# plt.show
# f.savefig("foo.pdf")
