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
import sqlite3

dbname="sensorsdata.db"
conn=sqlite3.connect(dbname)
curs=conn.cursor()
TIMEstatment = '''SELECT timestamp, x, y, z FROM ACC_data ORDER BY timestamp ;'''
curs.execute(TIMEstatment)
output1 = curs.fetchall()

# Xstatment = '''SELECT x FROM ACC_data ORDER BY timestamp  ;'''
# curs.execute(Xstatment)
# output2 = curs.fetchall()

# Ystatment = '''SELECT Y FROM ACC_data ORDER BY timestamp  ;'''
# curs.execute(Ystatment)
# output3 = curs.fetchall()

# Zstatment = '''SELECT Z FROM ACC_data ORDER BY timestamp  ;'''
# curs.execute(Zstatment)
# output4 = curs.fetchall()

# X2statment = '''SELECT x2 FROM ACC_data ORDER BY timestamp  ;'''
# curs.execute(Xstatment)
# output2 = curs.fetchall()

# Y2statment = '''SELECT Y2 FROM ACC_data ORDER BY timestamp  ;'''
# curs.execute(Y2statment)
# output3 = curs.fetchall()

# Zstatment = '''SELECT Z FROM ACC_data ORDER BY timestamp  ;'''
# curs.execute(Zstatment)
# output4 = curs.fetchall()

with open('test.csv', 'a', newline='') as csvfile:

    fieldnames = ['TIME','X', 'Y', 'Z']

    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    thewriter.writeheader()
    for values in output1:
        thewriter.writerow({'TIME': values, 'X': values})
    # for x in output2:
    #     thewriter.writerow({'X': x})
    # for y in output3:
    #     thewriter.writerow({'Y': y})
    # for z in output4:
    #     thewriter.writerow({'Z': z})
