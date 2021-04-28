# -*- coding: utf-8 -*-

#! pip install db-sqlite3
import sqlite3

conn = sqlite3.connect("exp2.db")
cur = conn.cursor()
conn = sqlite3.connect("test.db")
print("Database opened sucessfully");

conn.execute('''CREATE TABLE COMPANY2
             (ID INT PRIMARY KEY NOT NULL,
              NAME  TEXT NOT NULL,
              AGE INT NOT NULL,
              ADDRESS CHAR(50),
              SALARY REAL);''')
print("table created successfully");

conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (101,'PRAVALLIKA',20,'KOWKOOR',25000)");
conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES(102,'SINDUJA',20,'NIZAMBAD',24000)");
conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES(103,'SARU',20,'KAMMAM',23000)");
conn.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES(104,'SATYA',20,'NIZAMBAD',21000)");
conn.commit()
print("records created successfully");

for row in conn.execute('select * from COMPANY2'):
  print(row)

conn.commit()

conn.close()
