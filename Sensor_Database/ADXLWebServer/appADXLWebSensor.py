from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

# Retrieve data from database

def getData():
	conn=sqlite3.connect('../sensorsdata.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM ACC_data ORDER BY timestamp DESC LIMIT 10"):
		time = str(row[0])
		x = row[1]
		y = row[2]
		z = row[3]
	conn.close()
	return time, x, y, z
# main route 
@app.route("/")
def index():	
	time, x, y, z = getData()
	templateData = {
		'time': time,
		'x': x,
		'y': y,
        'z': z
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)