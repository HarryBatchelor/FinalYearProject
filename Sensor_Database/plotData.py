import sqlite3, pandas, matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#style.use('fivethirtyeight')



dbname = 'sensorsdata.db'
conn = sqlite3.connect(dbname)
sql = """SELECT timestamp, X2, Y2, Z2, x, y ,z from ACC_data ORDER BY timestamp"""


data = pandas.read_sql(sql, conn)


plt.plot(data.timestamp, data.x, label = "X Coords")
plt.plot(data.timestamp, data.y, label = "Y Coords")
plt.plot(data.timestamp, data.z, label = "Z Coords")
# plt.plot(data.timestamp, data.X2, label = "X 2 Coords")
# plt.plot(data.timestamp, data.Y2, label = "Y 2 Coords")
# plt.plot(data.timestamp, data.Z2, label = "Z 2 Coords")
plt.legend()
plt.title("Right Pole")
plt.show()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import sqlite3
# import pandas

# dbname = 'sensorsdata.db'
# conn = sqlite3.connect(dbname)
# sql = """SELECT timestamp, X2, Y2, Z2, x, y ,z from ACC_data"""

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# xs = []
# ys = []
# def animate(i, xs, ys):
#     #read data from sql
#     data = pandas.read_sql(sql, conn)
#     #add x and y to lists
#     xs.append(data.timestamp.strftime('%H:%M:%S.%f'))
#     ys.append(data.x)
#     #limit x and y lists to 20 items
#     xs = xs[-20:]
#     ys = ys[-20:]

#     #draw x and y lists
#     ax.clear()
#     ax.plot(xs, ys)

#     #format plot
#     plt.xticks(rotation=45, ha='right')
#     plt.subplots_adjust(bottom=0.30)
#     plt.title('x coords left pole')
    
# #set up plot to call animation function
# ani = animation.FuncAnimation(fig, animation, fargs=(xs, ys), interval=1000)
# plt.show()