from enum import unique
from itertools import cycle
import sqlite3
import matplotlib.pyplot as plt
import pandas
import csv
import matplotlib.backends.backend_pdf
import uuid
# Connect to DB
dbname= 'sensorsdata.db'
conn=sqlite3.connect(dbname)
# Set output to be a list
conn.row_factory = lambda curs, row: row[0]
curs = conn.cursor()
curs.execute("SELECT TimeOfHit.Row_ID FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.ROWID = TimeOfHit.Row_ID WHERE pole = 'LEFT' ;") #Execute SQL
leftHits = curs.fetchall()
# print (leftHits)



    # 10:42:24

#Collect the extended data for each timestamp above
for i in leftHits:
    # first = (i-30)
    # second = (i-300)
    cX = conn.cursor()
    cY = conn.cursor()
    cZ = conn.cursor()
    x = cX.execute('SELECT x from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
    y = cY.execute('SELECT y from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
    z = cZ.execute('SELECT z from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
    xs = cX.fetchall()
    ys = cY.fetchall()
    zs = cZ.fetchall()

uniquefilename = str(uuid.uuid4()) + '.pdf'
pdf = matplotlib.backends.backend_pdf.PdfPages(uniquefilename)
fig1 = plt.figure()
    # plot 1
plt.subplot(3,1,1)
plt.plot(xs)
plt.title("X Coords")
    # plot 2
plt.subplot(3,1,2)
plt.plot(ys)
plt.title("Y Coords")
    # plot 3
plt.subplot(3,1,3)
plt.plot(zs)
plt.title("Z Coords")
plt.suptitle("Left Sensor")
# plt.show()
pdf.savefig(fig1)
pdf.close()
    # for plots in hits:    
    #     fig = plt.figure()
    #     plt.plot(hits) 
    #     pdf = PdfPages(uniquefilename)
    #     pdf.savefig(fig)
    #     pdf.close()