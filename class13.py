"""
Date - FEb 16 2023
Students - Jahnavi, Indupriya, Tarani.
"""
from mysql.connector import connect
from password import password

CREATE_TABLE = """
CREATE TABLE attendence(
rollnum INT,
date DATE, 
id INT AUTO_INCREMENT PRIMARY KEY
)
"""

INSERT_CMD = """
INSERT INTO attendence(name, rollnum, experience) 
VALUES ("Jahnavi", 2, "1year")
"""

INSERT_ATT = """
INSERT INTO attendence(rollnum, date) 
VALUES (4, "2023-02-16")
"""

UPDATE_CMD = """
UPDATE students
SET rollnum = 3
WHERE name="Jahnavi"
"""

with connect(host='localhost', user='root', password=password, database='pythonclasses') as connection:
    cursor = connection.cursor()
    cursor.execute(INSERT_ATT)
    connection.commit()


# C - Create table/s
# R - Select data from table
# U - Updating table
# D - Deleting from table

# Selecting - using multiple joins --> INNER, LEFT OUTER, RIGHT OUTER JOINS.