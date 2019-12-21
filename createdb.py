import sqlite3
from datetime import datetime

conn = sqlite3.connect('piante2.db')
c = conn.cursor()

print "Database opened"

c.execute(""" CREATE TABLE rilevazioni (
	time CURRENT_TIMESTAMP
	temperature NUMERIC

	);""")
conn.commit()


temperature = 1.0
dateTimeObj = datetime.now()

c.execute("INSERT INTO rilevazioni VALUES (?)",(temperature))
conn.commit()

c.execute(""" SELECT * FROM rilevazioni """)

print(c.fetchall())
conn.close()