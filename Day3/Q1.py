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


db.close 

