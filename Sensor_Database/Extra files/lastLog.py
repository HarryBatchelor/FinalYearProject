import sqlite3
conn=sqlite3.connect('sensorsdata.db')
curs=conn.cursor()

print ("\nLast raw Data logged on database:\n")
for row in curs.execute("SELECT * FROM ACC_data ORDER BY timestamp DESC LIMIT 1"):
    print (str(row[0])+" ==> X = "+str(row[1])+"	Y ="+str(row[2]))