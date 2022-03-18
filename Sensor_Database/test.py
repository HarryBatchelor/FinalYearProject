# import csv

# colours = ['red', 'blue', 'green', 'yellow']
# colour_count = 0

# with open('test.csv', 'w', newline='') as csvfile:

#     fieldnames = ['number', 'colour']

#     thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     thewriter.writeheader()

#     for colour in colours:
#         colour_count += 1
#         thewriter.writerow({'number': colour_count, 'colour': colour})


import csv
import time
import sqlite3

dbname="sensorsdata.db"
conn=sqlite3.connect(dbname)
curs=conn.cursor()
TIMEstatment = '''SELECT timestamp FROM ACC_data ORDER BY timestamp DESC LIMIT 20 ;'''
curs.execute(TIMEstatment)
output1 = curs.fetchall()

Xstatment = '''SELECT x FROM ACC_data ORDER BY timestamp DESC LIMIT 20 ;'''
curs.execute(Xstatment)
output2 = curs.fetchall()

Ystatment = '''SELECT Y FROM ACC_data ORDER BY timestamp DESC LIMIT 20 ;'''
curs.execute(Ystatment)
output3 = curs.fetchall()

Zstatment = '''SELECT Z FROM ACC_data ORDER BY timestamp DESC LIMIT 20 ;'''
curs.execute(Ystatment)
output4 = curs.fetchall()

with open('test.csv', 'w', newline='') as csvfile:

    fieldnames = ['TIME','X', 'Y', 'Z']

    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    thewriter.writeheader()
    for timestamp in output1:
        thewriter.writerow({'TIME': timestamp})
    for x in output2:
        thewriter.writerow({'X': x})
    for y in output3:
        thewriter.writerow({'Y': y})
    for z in output4:
        thewriter.writerow({'Z': z})
