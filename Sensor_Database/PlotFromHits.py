import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import uuid
def PlotLeft():
    # Connect to DB
    dbname= 'sensorsdata.db'
    conn=sqlite3.connect(dbname)

    # Set output to be a list
    conn.row_factory = lambda curs, row: row[0]
    curs = conn.cursor()
    curs.execute("SELECT DISTINCT TimeOfHit.Row_ID FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.ROWID = TimeOfHit.Row_ID WHERE pole = 'LEFT' ;") #Execute SQL
    leftHits = curs.fetchall()
    # print (leftHits)


    #Collect the extended data for each timestamp above
    for i in leftHits:
        cX = conn.cursor()
        cY = conn.cursor()
        cZ = conn.cursor()
        x = cX.execute('SELECT x from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
        y = cY.execute('SELECT y from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
        z = cZ.execute('SELECT z from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
        xs = cX.fetchall()
        ys = cY.fetchall()
        zs = cZ.fetchall()
    # Plot data
        for i in leftHits:
                # plot 1
            plt.subplot(3,1,1)
            plt.plot(xs)
            plt.title("X Coords")
            plt.xticks([])
                # plot 2
            plt.subplot(3,1,2)
            plt.plot(ys)
            plt.title("Y Coords")
            plt.xticks([])
                # plot 3
            plt.subplot(3,1,3)
            plt.plot(zs)
            plt.title("Z Coords")
            plt.suptitle("Left Sensor")
            plt.xticks([])
            
            # give file unique name
            uniquefilename = str(uuid.uuid4()) + '.pdf'
        plt.savefig('pdf/LEFT/'+ uniquefilename)
        plt.close()
def PlotRight():
     # Connect to DB
    dbname= 'sensorsdata.db'
    conn=sqlite3.connect(dbname)

    # Set output to be a list
    conn.row_factory = lambda curs, row: row[0]
    curs = conn.cursor()
    curs.execute("SELECT DISTINCT TimeOfHit.Row_ID FROM ACC_data INNER JOIN TimeOfHit ON ACC_data.ROWID = TimeOfHit.Row_ID WHERE pole = 'RIGHT' ;") #Execute SQL
    RightHits = curs.fetchall()
    # print (leftHits)


    #Collect the extended data for each timestamp above
    for i in RightHits:
        cX2 = conn.cursor()
        cY2 = conn.cursor()
        cZ2 = conn.cursor()
        x2 = cX2.execute('SELECT x2 from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
        y2 = cY2.execute('SELECT y2 from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
        z2 = cZ2.execute('SELECT z2 from ACC_data WHERE ROWID < (?) ORDER BY timestamp DESC LIMIT 100', (i, ))
        x2s = cX2.fetchall()
        y2s = cY2.fetchall()
        z2s = cZ2.fetchall()
    # Plot data
        for i in RightHits:
                # plot 1
            plt.subplot(3,1,1)
            plt.plot(x2s)
            plt.title("X Coords")
            plt.xticks([])
                # plot 2
            plt.subplot(3,1,2)
            plt.plot(y2s)
            plt.title("Y Coords")
            plt.xticks([])
                # plot 3
            plt.subplot(3,1,3)
            plt.plot(z2s)
            plt.title("Z Coords")
            plt.suptitle("Right Sensor")
            plt.xticks([])
            
            # give file unique name
            uniquefilename = str(uuid.uuid4()) + '.pdf'
        plt.savefig('pdf/RIGHT/'+ uniquefilename)
        plt.close()
PlotLeft()
PlotRight()