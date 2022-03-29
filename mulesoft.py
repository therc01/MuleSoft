import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mulesoft")
mycursor.execute("CREATE DATABASE mulesoft")
mycursor.execute("USE mulesoft")
mycursor.execute("CREATE TABLE movies(name VARCHAR(255), "
                 "actor VARCHAR(255), "
                 "actress VARCHAR(255), "
                 "director VARCHAR(255), "
                 "year INT(4))")
sql = "INSERT INTO movies(name, actor, actress, director, year) VALUES (%s , %s, %s, %s, %s)"
val = [
  ('SURYAVANSHI', 'AKSHAY KUMAR', 'KATRINA KAIF', 'ROHIT SHETTY', 2021),
  ('AIRLIFT', 'AKSHAY KUMAR', 'NIMRAT KAUR', 'RAJA KRISHNA MENON', 2016),
  ('GOLD', 'AKSHAY KUMAR', 'ILEANA DCRUZ', 'DHARMENDRA SURESH DESAI', 2016),
  ('SHERSHAH', 'SIDHHART MALHOTRA', 'KIARA ADVANI', 'VISHNUVARDHAN', 2021),
  ('KESARI', 'AKSHAY KUMAR', 'PARINEETI CHOPRA', 'ANURAG SINGH', 2019),
  ('KABIR SINGH', 'SHAHID KAPOOR', 'KIARA ADVANI', 'SANDEEP REDDY VANGA',2019)
]
mycursor.executemany(sql, val)