import csv
import sqlite3
import pandas as pd

dbname='sensorsdata.db'
def PoleHitLEFT():
    conn=sqlite3.connect(dbname)
    curs = conn.cursor()

    curs.execute("INSERT INTO Hits values ((SELECT timestamp FROM TEST ORDER BY timestamp DESC LIMIT 1), ('LEFT'), (SELECT ROWID FROM TEST ORDER BY timestamp DESC LIMIT 1))")
    conn.commit()
    conn.close()
def PoleHitRIGHT():
    conn=sqlite3.connect(dbname)
    curs = conn.cursor()

    curs.execute("INSERT INTO Hits values ((SELECT timestamp FROM TEST ORDER BY timestamp DESC LIMIT 1), ('RIGHT'), (SELECT ROWID FROM TEST ORDER BY timestamp DESC LIMIT 1))")
    conn.commit()
    conn.close()
PoleHitRIGHT()
PoleHitLEFT()
