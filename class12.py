# mysql-connector-python - wrapper function in python to connect to the mysql database and do functionalities.


from mysql.connector import connect
from getpass import getpass
from password import password

CREATE_DB = 'CREATE DATABASE pythonclasses'
SHOW_DBS = 'SHOW DATABASES'

CREATE_TABLE = """
CREATE TABLE students(
name VARCHAR(100),
rollnum INT,
experience VARCHAR(10),
id INT AUTO_INCREMENT PRIMARY KEY
)
"""

list_of_students = [("Manideep", 1, "7years"), ("Jahnavi", 2, "1year"), ("Indupriya", 3, "7years")]
INSERT_CMD = """
insert into students(name, rollnum, experience) 
values (%s, %s, %s)
"""


WHERE_CLAUSE = """SELECT * FROM students WHERE name='Manideep'
"""

# with open('filename.txt') as fopen: # Opening files using python
with connect(host='localhost', user='root', password=password, database='pythonclasses') as connection:
    cursor = connection.cursor()
    cursor.executemany(INSERT_CMD, list_of_students)
    connection.commit()
