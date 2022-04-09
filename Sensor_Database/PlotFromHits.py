from enum import unique
import sqlite3
import matplotlib.pyplot as plt
import pandas
import csv
from matplotlib.backends.backend_pdf import PdfPages
import uuid
dbname= 'sensorsdata.db'
conn=sqlite3.connect(dbname)
conn.row_factory = lambda curs, row: row[0]
curs = conn.cursor()
curs.execute("SELECT DISTINCT TimeOfHit.timestamp FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.timestamp = TimeOfHit.timestamp WHERE pole = 'LEFT' ;")
leftHits = curs.fetchall()
# print(leftHits)
uniquefilename = str(uuid.uuid4()) + '.pdf'
for x in leftHits:
    # conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    hits = c.execute('SELECT x from ACC_data WHERE timestamp = (?) ORDER BY timestamp DESC LIMIT 10', (x,))
    hits = c.fetchall()
    print(hits)
    # for times in leftHits:
    #     fig = plt.figure()
    #     plt.plot(hits) 
    #     pdf = PdfPages(uniquefilename)
    #     pdf.savefig(fig)
    #     pdf.close()
    # curs.execute("""SELECT timestamp, x, y, z from ACC_data WHERE timestamp != "2022-03-29 18:17:47" AND x !="0" ORDER BY timestamp DESC LIMIT;""")
    # MoreLeftHits = curs.fetchall()
    # print(MoreLeftHits) 
    # data = pandas.read_sql(sql, conn)
    # print(data)
    # curs.execute(sql,x)
    # MoreLeftHits = curs.fetchall()
    # print(MoreLeftHits)
