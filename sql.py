import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="db"
)

mycursor = mydb.cursor()
sql="""
SHOW TABLES;
"""
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
