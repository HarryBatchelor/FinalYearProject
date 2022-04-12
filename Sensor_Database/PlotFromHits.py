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
curs.execute("SELECT DISTINCT TimeOfHit.timestamp FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.timestamp = TimeOfHit.timestamp WHERE pole = 'LEFT' ;") #Execute SQL
leftHits = curs.fetchall()

uniquefilename = str(uuid.uuid4()) + '.pdf'

#Collect the extended data for each timestamp above
for x in leftHits:
    c = conn.cursor()
    timestamp = c.execute('SELECT x from ACC_data WHERE timestamp = (?) ORDER BY timestamp DESC LIMIT 10', (x,))
    # xs = c.execute('SELECT x FROM ACC_data WHERE ')
    hits = c.fetchall()
    print(hits)
    for plots in hits:    
        fig = plt.figure()
        plt.plot(hits) 
        pdf = PdfPages(uniquefilename)
        pdf.savefig(fig)
        pdf.close()