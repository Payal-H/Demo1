"""
2. Read Employee database table from mysql and instantiate the Employee object.
Display all employee details (Name, empID, Age, Sal).
Use Employee class
"""
import MySQLdb
db = MySQLdb.connect("localhost","root","root","test" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS USERS")
sql  = """CREATE TABLE USERS(id INT primary key,name varchar(30),
                    phone varchar(10),email varchar(40) unique,password varchar(20) )"""
cursor.execute(sql)
sql1 = """INSERT INTO USERS (id, name, phone, email, password)  VALUES
                            (101,'payal','7653686873','payal1@gmail','p_h@123'),
                            (102,'pIKI','1212124512','payal_harne@gmail','p_1@123')"""

try:
   # Execute the SQL command
   cursor.execute(sql1)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

sql = "SELECT * FROM USERS"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[1]
      phone = row[2]
      email = row[3]
      password = row[4]
      # Now print fetched result
      print "id =%d,lname=%s,age=%s,sex=%s,income=%s" % \
             (id, phone, name, email, password )
except:
   print "Error: unable to fecth data"
   
db.close 

