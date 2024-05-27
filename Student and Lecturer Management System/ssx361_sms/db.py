import sqlite3


class Database:
    # Constructor of Database class which takes a Database object
    def __init__(self, db):
        # Creates database and connects to it
        self.connection = sqlite3.connect(db)
        # Creating cursor object to run queries
        self.cursor = self.connection.cursor()

        # Create the student table in the database
        query1 = ("CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY,"
                  " name TEXT NOT NULL, surname TEXT NOT NULL, student_number TEXT NOT NULL, "
                  "student_email TEXT NOT NULL, course TEXT NOT NULL)")
        self.cursor.execute(query1)
        # Create the lecturer table in the database
        query2 = ("CREATE TABLE IF NOT EXISTS lecturers (lecturer_id INTEGER PRIMARY KEY, "
                  "name TEXT NOT NULL, email TEXT NOT NULL, department TEXT NOT NULL, "
                  "courses_taught TEXT NOT NULL, qualifications TEXT NOT NULL)")
        self.cursor.execute(query2)

        self.connection.commit()

    # READ student data
    def fetchStudentData(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        return rows

    # READ lecturer data
    def fetchLecturerData(self):
        self.cursor.execute("SELECT * FROM lecturers")
        rows = self.cursor.fetchall()
        return rows

    # CREATE student data
    def insertStudentData(self, n, s, sn, se, c):
        self.cursor.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?, ?)", (n, s, sn, se, c))
        self.connection.commit()

    # CREATE lecturer data
    def insertLecturerData(self, l_n, l_e, d, c_t, q):
        self.cursor.execute("INSERT INTO lecturers VALUES (NULL, ?, ?, ?, ?, ?)", (l_n, l_e, d, c_t, q))
        self.connection.commit()

    # UPDATE student data
    def updateStudentData(self, n, s, sn, se, c, sid):
        self.cursor.execute("UPDATE students SET name=?, surname=?, student_number=?, "
                            "student_email=?, course=? WHERE student_id=?", (n, s, sn, se, c, sid))
        self.connection.commit()

    # UPDATE lecturer data
    def updateLecturerData(self, l_n, l_e, d, c_t, q, lid):
        self.cursor.execute("UPDATE lecturers SET lecturer_name=?, lecturer_email=?, department=?, "
                            "courses_taught_email=?, qualifications=? WHERE student_id=?", (l_n, l_e, d, c_t, q, lid))
        self.connection.commit()

    # DELETE data
    def deleteStudentData(self, sid):
        self.cursor.execute("DELETE FROM students WHERE student_id=?", (sid,))
        self.connection.commit()

    # destructor to release resources (CPU and memory)
    def __del__(self):
        self.connection.close()


'''
db = Database("ms.db")

db.insertStudentData("Maboku", "Seimela", "0783342957", "maboku.seimela@live.com", "DIT360")
db.insertLecturerData("Maboku Seimela", "maboku.seimela@liveee.com", "IT department",
                      "Syntax & Scripting 361", "Higher Certificate in IT")
'''



