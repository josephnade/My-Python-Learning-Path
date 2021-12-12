def calculate_average(x):
    list = x.split(':')
    student_name = list[0]
    grades = list[1]
    grades = grades.split(",")
    midterm = grades[0]
    final = grades[1]
    return student_name + "= "+str((int(midterm) + int(final)) /2)+"\n"
def read_grades():
    with open("grade.txt","r",encoding="utf-8") as file:
        for i in file:
            print(calculate_average(i),end="")
def write_grades():
    name =input("Please enter student name =")
    surname = input("Please enter student surname =")
    midterm = input("Please enter midterm grade =")
    final = input("Please enter final grade =")
    with open("grade.txt","a",encoding="utf-8") as file:
        file.write(name +" "+ surname+":"+midterm+","+final+"\n")
def save_grades():
    with open("grade.txt","r",encoding="utf-8") as file:
        list = []
        for i in file:
            list.append(calculate_average(i))
        with open("results.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)


while True:
    choose = input("[1]Read Grades\n[2]Write Grades\n[3]Save Grades\n[4]Exit\nPlease choose what do you want =")
    if choose == '1':
        content =read_grades()
    elif choose == '2':
        write_grades()
    elif choose == '3':
        save_grades()
    elif choose == '4':
        break
    else:
        print("You entered wrong input.Please try agai\nn!")