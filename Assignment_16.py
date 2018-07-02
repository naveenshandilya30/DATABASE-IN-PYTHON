#Question 1

import sqlite3
conn=sqlite3.connect('Table.db')

print("Database created successfully")
conn.execute('''CREATE TABLE BOOKS (BOOK_ID INT PRIMARY KEY NOT NULL,TITLE_ID TEXT NOT NULL,LOCATION TEXT NOT NULL,GENRE_ID TEXT NOT NULL)''')
conn.execute('''CREATE TABLE TITLE(TITILE_ID INT NOT NULL,TITLE_NAME TEXT NOT NULL,ISBN INT NOT NULL ,PUBLISHER_ID INT NOT NULL,PUBLISHER_YEAR INT NOT NULL)''')
conn.execute('''CREATE TABLE PUBLISHERS(PUBLISHER_ID INT NOT NULL, NAME TEXT NOT NULL,STREET_ADDRESS CHAR(20),SUITE_NUMBER INT NOT NULL,ZIP_CODE_ID INT NOT NULL)''')
conn.execute('''CREATE TABLE ZIPCODES (ZIP_CODE_ID INT NOT NULL,CITY TEXT NOT NULL,STATE TEXT NOT NULL,ZIP_CODE INT NOT NULL)''')
conn.execute('''CREATE TABLE AUTHORSTITLES (AUTHORS_TITLES_ID INT NOT NULL,AUTHOR_ID INT NOT NULL,TITLE_ID INT NOT NULL)''')
conn.execute('''CREATE TABLE AUTHORS (AUTHOR_ID INT PRIMARY KEY NOT NULL,FIRST_NAME TEXT NOT NULL,MIDDLE_NAME TEXT NOT NULL,LAST_NAME TEXT NOT NULL)''')
print("Table Created Successfully")
conn.close()


#Question 2

import sqlite3

conn=sqlite3.connect('insertion.db')

print("Opened Database Successfully")
conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY NOT NULL,
             NAME     TEXT  NOT NULL,
             AGE      INT   NOT NULL,
             ADDRESS  CHAR (50),
             SALARY     REAL)''')
print("Table created sucessfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'NAVEEN',21,'CALIFORNIA',50000.00)")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'ANKIT',20,'ENGLAND',40000.00)")
conn.commit()
print("Inserted Successfully")


#Question 3

import sqlite3

conn =sqlite3.connect('test.db')



print("BEFORE UPDATING")
cursor=conn.execute("SELECT ID,NAME,ADDRESS,SALARY from COMPANY")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3],"\n")

print("AFTER UPDATING")
conn.execute("UPDATE COMPANY set SALARY = SALARY + 30000 where AGE=20")
cursor=conn.execute("SELECT Id,Name,Address,Salary from Company")

for row in cursor:
    print("Id=",row[0])
    print("Name=",row[1])
    print("Address=",row[2])
    print("Salary=",row[3],"\n")
print("records created successfully")


