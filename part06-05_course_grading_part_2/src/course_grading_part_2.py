# write your solution here
# write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
DEBUG = False

if DEBUG:
    student_info = 'students4.csv'
    exercise_info = 'exercises4.csv'
    exam_info = 'exam_points4.csv'
else:
    student_info = input('Filename for student info: ')
    exercise_info = input('Filename for exercise info: ')
    exam_info = input('Filename for exam info: ')

student_path = PATH + student_info
exercise_path = PATH + exercise_info
exam_path = PATH + exam_info


#create dictionary for first csv file
#key = id from csv.  Value = tuple of (first name,last name)
student_dict = {}

with open(student_path, 'r') as student_file:
    for line in student_file:
        student_list = line.split(';')
        if student_list[0] == 'id':
            continue
        else:
            student_dict[student_list[0]] = student_list[1].strip(), student_list[2].strip()
        
    #print(student_dict)

#create dictionary for second csv file with excercises
#key = id from csv.  Value = list of exercise # completed
exercise_dict = {}

with open(exercise_path,'r') as exercise_file:
    for line in exercise_file:
        exercise_list = line.split(';')
        if exercise_list[0] == 'id':
            continue
        else:
            exercise_dict[exercise_list[0]] = [int(x.strip()) for x in exercise_list[1:]]

#create dictionary for third csv file with exam points
#key = id from csv.  Value = list of exam points
exam_dict = {}

with open(exam_path,'r') as exam_file:
    for line in exam_file:
        exam_list = line.split(';')
        if exam_list[0] == 'id':
            continue
        else:
            exam_dict[exam_list[0]] = [int(x.strip()) for x in exam_list[1:]]

print(exam_dict)

for id, name in student_dict.items():
    
    total = 0

    if id in exercise_dict:
        total += sum(exercise_dict[id]) // 4

    if id in exam_dict:
        total += sum(exam_dict[id])
    
    grade = 0

    if 0 <= total <= 14:
        grade = 0
    elif 14 < total <= 17:
        grade = 1
    elif  17 < total <= 20:
        grade = 2
    elif  20 < total <= 23:
        grade = 3
    elif  13 < total <= 27:
        grade = 4
    elif  27 < total:
        grade = 5

    print(f'{name[0]} {name[1]} {grade}')
            

