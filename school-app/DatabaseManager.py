import mysql.connector
from datetime import datetime
from Connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DatabaseManager:
    def __init__(self):
        self.connection = connection
        self.cursor = connection.cursor()

    def create_student(self, student: Student):
        sql = f"INSERT INTO student(Name, Surname, Birthdate, Gender, ClassId) VALUES ('{student.name}','{student.surname}'," \
              f"'{student.birthdate}','{student.gender}',{student.classId})"
        self.cursor.execute(sql)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} rows recorded!")
        except mysql.connector.Error as e:
            print(e)

    def read_student_by_id(self, id):
        sql = f"SELECT * FROM student WHERE id = {id}"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        except mysql.connector.Error as e:
            print(e)

    def read_students_by_class(self, id):
        sql = f"SELECT * FROM student WHERE classid = {id}"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Student.create_student(obj)
        except mysql.connector.Error as e:
            print(e)

    def update_student(self, student: Student):
        sql = f"UPDATE student SET Name = '{student.name}' , Surname ='{student.surname}' , Birthdate = '{student.birthdate}'," \
              f"Gender= '{student.gender}' , ClassId = {student.classId} WHERE id = {student.id}"
        self.cursor.execute(sql)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} row affected !")
        except mysql.connector.Error as e:
            print(e)

    def delete_student(self, id):
        sql = f"DELETE FROM student WHERE id = {id}"
        self.cursor.execute(sql)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} row affected !")
        except mysql.connector.Error as e:
            print(e)

    def create_teacher(self, teacher: Teacher):
        pass

    def read_teacher(self, teacher: Teacher):
        pass

    def update_teacher(self, teacher: Teacher):
        pass

    def delete_teacher(self, teacher: Teacher):
        pass

    def get_classes(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.create_class(obj)
        except mysql.connector.Error as e:
            print(e)

    def __del__(self):
        self.connection.close()
        print("Db has been shutted!")


db = DatabaseManager()
# student = db.read_student_by_id(1)
# print(student.name)

# students = db.read_students_by_class(2)
# print(students[0].name)

# # student = db.read_student_by_id(1)
# # student.name = "Ahmet"
# # student.surname = "Anderson"
# db.create_student(student)

student = db.read_student_by_id(3)
student.name = "Yusuf"
db.update_student(student)
