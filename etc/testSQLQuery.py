from asyncio.windows_events import NULL
import mysql.connector
import pandas as pd
import datetime as dt


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="eksdee2506",
    database="test"
)

mycursor = mydb.cursor()


# create history table example
#mycursor.execute("CREATE TABLE History (personID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), absen BOOLEAN, timestamp TIMESTAMP)")
#mycursor.execute("DESCRIBE History")

# add a column example
# mycursor.execute("ALTER TABLE history ADD COLUMN absen BOOLEAN AFTER name")k/

# add data/row (untuk booking)
nameexample = "Epo"
# mycursor.execute(
#    "INSERT INTO History (name,absen) VALUES(%s,%s)", (nameexample, False))
# mydb.commit()
# use the value <None> to pass NULL

# reset auto increment
#mycursor.execute("ALTER TABLE History AUTO_INCREMENT = 1")
# mydb.commit()

# show table
#mycursor.execute("SELECT * FROM History")

# alter a data on existing row
#datetimeex = dt.datetime.now().strftime("%d/%m/%Y %I:%M:%S")
mycursor.execute(
    "UPDATE History SET absen = %s, timestamp = CURRENT_TIMESTAMP WHERE name = %s", (False, nameexample))
mydb.commit()

#result = mycursor.fetchall()
#result = mycursor.fetchone()

for i in mycursor:
    print(i)
