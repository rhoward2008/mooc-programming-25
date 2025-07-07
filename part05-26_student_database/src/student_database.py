# Write your solution here
## Peter: None
## Peter: [(econ,3),(math,2)]
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = []

def print_student(students: dict, name: str):
    if name in students:
        if students[name]:
            print(f'{name}: \n {len(students[name])} completed courses')
            for grade in students[name]:
                print(f'  {grade[0]} {grade[1]} ')
        else:
            print(f'{name}: \n no completed courses')
    else:
        print(f'{name}: no such person in the database')

def add_course(students: dict, name: str, course: tuple):
    new_class = course[0]
    new_grade = course[1]
    add_grade = True

    #Only add in new score if student already exists and the new grade is greater than 0
    #If the student already took the class, don't add if the new grade is less than or equal to old one
    if name in students and new_grade > 0:
        for grade in students[name]:
            if grade[0] == new_class and new_grade <= grade[1]:
                add_grade = False
            elif grade[0] == new_class and new_grade >= grade[1]:
                students[name].remove(grade)

        if add_grade:
            students[name].append(course)
        

def summary(students: dict):
    count = len(students)
    most_name = ''
    most_count = 0
    best_name = ''
    best_grade = 0

    for name,classes in students.items():
        if len(classes)>most_count:
            most_name = name
            most_count = len(classes)
    
        sum = 0

        for grade in classes:
            sum += grade[1]
        
        if len(classes):
            if (sum / len(classes)) > best_grade:
                best_name = name
                best_grade = sum / len(classes)

    print(f'Student count: {count}')
    print(f'most courses completed {most_count} {most_name}')
    print(f'best average grade {best_grade} {best_name}')
    
    

if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
    #print(f'break1: {students}')
    print_student(students, "Peter")
    summary(students)
    #print(f'break2: {students}')