from enum import unique
import sqlite3
import matplotlib.pyplot as plt
import pandas
import csv
from matplotlib.backends.backend_pdf import PdfPages
import uuid
# Connect to DB
dbname= 'sensorsdata.db'
conn=sqlite3.connect(dbname)
# Set output to be a list
conn.row_factory = lambda curs, row: row[0]
curs = conn.cursor()
curs.execute("SELECT TimeOfHit.Row_ID FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.ROWID = TimeOfHit.Row_ID WHERE pole = 'LEFT' ;") #Execute SQL
leftHits = curs.fetchall()
print (leftHits)
# uniquefilename = str(uuid.uuid4()) + '.pdf'


    # 10:42:24

#Collect the extended data for each timestamp above
for x in leftHits:
    first = (x-30)
    second = (x-300)
    c = conn.cursor()
    timestamp = c.execute('SELECT timestamp from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (x, ))
    x = c.execute('SELECT x from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (x, ))
    hits = c.fetchall()
    print(hits)
    # for plots in hits:    
    #     fig = plt.figure()
    #     plt.plot(hits) 
    #     pdf = PdfPages(uniquefilename)
    #     pdf.savefig(fig)
    #     pdf.close()