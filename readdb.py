import sqlite3

conn = sqlite3.connect('piante.db')
c = conn.cursor()

c.execute("""SELECT * FROM DATATABLE """)
print(c.fetchall())
conn.commit()
conn.close()
