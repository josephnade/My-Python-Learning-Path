import datetime
from DatabaseManager import DatabaseManager
from Student import Student


class App:
    def __init__(self):
        self.database = DatabaseManager()

    def initApp(self):
        message = "********\n[1]- Student List\n[2]- Add Student\n[3]- Update Student\n[4]- Delete Student\n[5]-Add Teacher\n[6]- Lessons for Classes\n[7]- Exit\n Choose: "
        while True:
            choose = input(message)
            if choose == "1":
                self.displayStudent()
            elif choose == "2":
                self.addStudent()
            elif choose == "3":
                self.updateStudent()
            elif choose == "4":
                self.deleteStudent()
            elif choose == "5":
                pass
            elif choose == "6":
                pass
            elif choose == "7":
                break
            else:
                print("Wrong input. Try Again!!")

    def displayClasses(self):
        classes = self.database.get_classes()
        for i in classes:
            print(f"{i.id} -) {i.name}")

    def displayStudent(self):
        self.displayClasses()
        class_id = input("Which class do you want to choose:")
        students = self.database.read_students_by_class(class_id)
        for s in students:
            print(f"{s.id}: {s.name} {s.surname} ")
        return class_id

    def addStudent(self):
        self.displayClasses()
        class_id = int(input("Which class would you like to add the student to: "))
        name = input("Enter student name: ")
        surname = input("Enter student surname: ")
        year = int(input("Enter student birth year: "))
        month = int(input("Enter student birth month: "))
        day = int(input("Enter student birthday: "))
        birthdate = datetime.date(year, month, day)
        gender = input("Enter student gender(E-K): ")
        student = Student(None, name, surname, birthdate, gender, class_id)
        self.database.create_student(student)
        print("Student has been added!")

    def updateStudent(self):
        class_id = self.displayStudent()
        student_id =int(input("Which student do you want to update: "))
        student = self.database.read_student_by_id(student_id)
        student.name = input("Name: ") or student.name
        student.surname= input("Surname: ") or student.surname
        student.gender = input("Gender(E/K): ") or student.gender
        student.classId = input("Class Id: ") or student.classId

        year = input("Birth year: ") or student.birthdate.year
        month = input("Birth month: ") or student.birthdate.month
        day = input("Birth day:") or student.birthdate.day

        student.birthdate = datetime.date(int(year),int(month),int(day))
        self.database.update_student(student)

    def deleteStudent(self):
        self.displayStudent()
        student_id =int(input("Which student do you want to delete: "))
        self.database.delete_student(student_id)

app = App()
app.initApp()
