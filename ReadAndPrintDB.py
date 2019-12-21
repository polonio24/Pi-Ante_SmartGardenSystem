import sqlite3
from datetime import datetime
import time

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Piante2.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sqlite_select_query = """SELECT * from misurazioni ORDER BY dataora desc LIMIT 1"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        #print("Total rows are:  ", len(records))
        #print("Printing each row")
        for row in records:
            print("dataora: ", row[0])
            print("temperatura: ", row[1]) 
            print("humidity: ", row[2])
            print("sunlightIR: ", row[3])
            print("sunlightVisible: ", row[4])
            print("sunlightUV: ",row[5])
            print("airQuality: ",row[6])
            print("soilMoisture: ",row[7])
            print("tankPCFull: ",row[8])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        
    except KeyboardInterrupt:
    	print("exiting program")
        # if (sqliteConnection):
        #     sqliteConnection.close()
        #     print("The SQLite connection is closed")

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("The SQLite connection is closed")
while True:
	readSqliteTable()
	time.sleep(10)