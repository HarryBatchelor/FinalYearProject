import sqlite3
dbname = 'sensorsdata.db'
conn=sqlite3.connect(dbname)
with conn:
    cur = conn.cursor
    cur.execute( """CREATE TABLE ALL_data(
    Row_ID int PRIMARY KEY,
    timestamp DATETIME, 
    x NUMERIC, 
    y NUMERIC, 
    z NUMERIC, 
    x2 NUMERIC, 
    y2 NUMERIC, 
    z2 NUMERIC """)
print("DONE")