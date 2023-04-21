import  sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")
conn.execute("""
CREATE TABLE IF NOT EXISTS STUDENT_DATA(
STU_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
STU_NAME TEXT NOT NULL, 
STU_CONTACT TEXT,
STU_ADDRESS TEXT,
STU_ROLLNO TEXT NOT NULL,
COURSE_NAME TEXT NOT NULL)
""")
print ("Table STUDENT_DATA created successfully")

conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Sahil', '9867086170', 'Sakinaka','S021', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Rohan', '8879516908', 'Andheri','S025', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Abdul', '7039797097', 'Sakinaka','S003', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Aditi', '9321235403', 'Marol','S034', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Rachel', '9967326742', 'Kalyan','S002', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Jyoti', '7045467584', 'Sakinaka','S030', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Savita', '8454075564', 'Sakinaka','S014', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Iqra', '9324252553', 'Sakinaka','S020', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Shivam', '7718090403', 'Seepz','S05', 'IT')");
conn.execute("INSERT INTO STUDENT_DATA (STU_NAME,STU_CONTACT,STU_ADDRESS,STU_ROLLNO,COURSE_NAME) \
      VALUES ('Tilak', '7678018278', 'Andheri','S037', 'IT')");

conn.commit()
print ("Records inserted successfully")
conn.close()