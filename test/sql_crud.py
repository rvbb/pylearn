import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dev",
  password="Devdev!23",
  database="bypythondb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE bypythondb")
# mycursor.execute("CREATE TABLE tf (purpose VARCHAR(255), trend VARCHAR(255))")

#insert
sql = "INSERT INTO tf (purpose, trend) VALUES (%s, %s)"
val = ("a2", "b")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#select
mycursor.execute("SELECT * FROM tf WHERE purpose='a1'")
myresult = mycursor.fetchmany()
for x in myresult:
  print(x)