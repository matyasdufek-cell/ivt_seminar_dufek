
import mysql.connector

mydb = mysql.connector.connect(
  host=r"seminar.krenka.cz",
  user="c1seminar",
  password="ERwf6Li_6rT",
  database="c1seminar"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM "pampalini"")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
print(conflict)