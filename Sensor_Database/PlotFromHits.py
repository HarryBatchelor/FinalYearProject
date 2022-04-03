import sqlite3
import matplotlib as plt

dbname= 'sensorsdata.db'
def getHitsLEFT():
    conn=sqlite3.connect(dbname)
    curs = conn.cursor()

    curs.execute("FROM TimeOfHit SELECT timestamp WHERE pole = 'LEFT'")
    conn.commit()
    conn.close()
    leftResults = curs.fetchall()
    
 SELECT TimeOfHit.timestamp, x, y, z FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.timestamp = TimeOfHit.timestamp WHERE pole = 'LEFT';