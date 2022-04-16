import csv
import sqlite3
import pandas as pd

dbname='sensorsdata.db'
def PoleHitLEFT():
    conn=sqlite3.connect(dbname)
    curs = conn.cursor()

    curs.execute("INSERT INTO TimeOfHit values ((SELECT Row_ID FROM ACC_data ORDER BY timestamp DESC LIMIT 1), datetime('now'),('LEFT'))")
    conn.commit()
    conn.close()
def PoleHitRIGHT():
    conn=sqlite3.connect(dbname)
    curs = conn.cursor()

    curs.execute("INSERT INTO TimeOfHit values ((SELECT Row_ID FROM ACC_data ORDER BY timestamp DESC LIMIT 1), datetime('now'), ('RIGHT'))")
    conn.commit()
    conn.close()
PoleHitRIGHT()
PoleHitLEFT()
