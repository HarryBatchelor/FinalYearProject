from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import sqlite3
import datetime
from dateutil import parser

dbname = 'sensorsdata.db'
conn = sqlite3.connect(dbname)
curs = conn.cursor()

def read_from_db():
    curs.execute('SELECT * FROM ACC_data')
    data = curs.fetchall()
    print(data)
    for row in data:
        print(row)
        
def graph_data():
    curs.execute('SELECT time, x, y, z FROM ACC_data')
    data = curs.fetchall()
    
    dates = []
    values = []
    
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])
        
    plt.plot_date(dates, values, '-')
    plt.show()