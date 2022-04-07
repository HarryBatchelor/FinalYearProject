import sqlite3
import matplotlib.pyplot as plt
import pandas
import csv
dbname= 'sensorsdata.db'
conn=sqlite3.connect(dbname)
conn.row_factory = lambda curs, row: row[0]
curs = conn.cursor()
curs.execute("SELECT TimeOfHit.timestamp FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.timestamp = TimeOfHit.timestamp WHERE pole = 'LEFT';")
leftHits = curs.fetchall()
# print(leftHits)
conn.commit()
conn.close()

for x in range(len(leftHits)):
    conn=sqlite3.connect(dbname)
    conn.row_factory = lambda curs, row: row[0]
    curs = conn.cursor()
    curs.execute("""SELECT timestamp, x, y, z from ACC_data WHERE timestamp != "2022-03-29 18:17:47" ORDER BY timestamp DESC LIMIT 100;""")
    MoreLeftHits = curs.fetchall()
    # print(MoreLeftHits)

    f = open('sqlData.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(MoreLeftHits)
    f.close()  
    # data = pandas.read_sql(sql, conn)
    # print(data)
    # curs.execute(sql,x)
    # MoreLeftHits = curs.fetchall()
    # print(MoreLeftHits)
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
