import sqlite3
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def createTable():
    try:
        sqliteConnection = sqlite3.connect('Piante2.db')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS misurazioni (
                                    dataora datetime,
                                    temperature REAL NOT NULL,
                                    humidity REAL NOT NULL,
                                    sunlightIR REAL NOT NULL, 
                                    sunlightVisible REAL NOT NULL,
                                    sunlightUV REAL NOT NULL,
                                    airQuality REAL NOT NULL,
                                    soilMoisture REAL NOT NULL,
                                    tankPCFull REAL NOT NULL);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")


# def insertVaribleIntoTable(dataora,temperature, humidity, \
#                             sunlightIR, sunlightVisible,sunlightUV, \
#                             airQuality,soilMoisture,tankPCFull):
#     try:
#         sqliteConnection = sqlite3.connect('Piante2.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         sqlite_insert_with_param = """INSERT INTO 'misurazioni'
#                           ('dataora', 'temperature', 'humidity', 'sunlightIR', 'sunlightVisible','sunlightUV','airQuality','soilMoisture','tankPCFull') 
#                           VALUES (?, ?, ?, ?, ?,?,?,?,?);"""

#         data_tuple = (dataora,temperature, humidity, 
#                         sunlightIR, sunlightVisible,sunlightUV,
#                         airQuality,soilMoisture,tankPCFull)

#         cursor.execute(sqlite_insert_with_param, data_tuple)
#         sqliteConnection.commit()
#         print("Python Variables inserted successfully into misurazioni table")

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to insert Python variable into sqlite table", error)
#     finally:
#         if (sqliteConnection):
#             sqliteConnection.close()
#             print("The SQLite connection is closed")




# def readSqliteTable():
#     try:
#         sqliteConnection = sqlite3.connect('Piante2.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         sqlite_select_query = """SELECT * from misurazioni"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Total rows are:  ", len(records))
#         print("Printing each row")
#         for row in records:
#             print("dataora: ", row[0])
#             print("temperatura: ", row[1]) 
#             print("humidity: ", row[2])
#             print("sunlightIR: ", row[3])
#             print("sunlightVisible: ", row[4])
#             print("sunlightUV: ",row[5])
#             print("airQuality: ",row[6])
#             print("soilMoisture: ",row[7])
#             print("tankPCFull: ",row[8])
#             print("\n")

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read data from sqlite table", error)
#     finally:
#         if (sqliteConnection):
#             sqliteConnection.close()
#             print("The SQLite connection is closed")


## --- MAIN -----
createTable()
# insertVaribleIntoTable(datetime.now(), 21 , 46, \
#                         111 , 112 , 113 , \
#                         798, 70, 80)
# readSqliteTable()