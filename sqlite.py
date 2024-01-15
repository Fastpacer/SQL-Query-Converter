import sqlite3

# Connect to sqlite data base

connection=sqlite3.connect("students.db")

# Create a cursor object to insert records , create table

cursor=connection.cursor()
# Create the table
table_info="""
Create table STUDENT (NAME VARCHAR(30) , CLASS VARCHAR (25), SECTION VARCHAR(25));
"""
cursor.execute(table_info)

# Insert some more records

cursor.execute("""Insert Into STUDENTS values("ADAM","MACHINE LEARNING","D")""")
cursor.execute("""Insert Into STUDENTS values("MAX","DATA SCIENCE","B")""")
cursor.execute("""Insert Into STUDENTS values("GILCHRIST","MACHINE LEARNING","B")""")
cursor.execute("""Insert Into STUDENTS values("SAM","ARTIFICIAL INTELLIGENCE","A")""")
cursor.execute("""Insert Into STUDENTS values("MICHEAL","MACHINE LEARNING","C")""")
cursor.execute("""Insert Into STUDENTS values("PATRICK","MACHINE LEARNING","C")""")
cursor.execute("""Insert Into STUDENTS values("RYAN","DATA SCIENCE","C")""")
cursor.execute("""Insert Into STUDENTS values("JAMES","MACHINE LEARNING","A")""")

# Display all the records

print("The inserted records are")
data=cursor.execute("""Select * from STUDENTS""")

for row in data:

    print(row)
