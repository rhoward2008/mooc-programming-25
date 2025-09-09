PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
DEBUG = False

if DEBUG:
    student_info = 'students1.csv'
    exercise_info = 'exercises1.csv'
    exam_info = 'exam_points1.csv'
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

#print(exercise_dict)

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

#print(exam_dict)

# create dictionary for final stats
# Format is: id: [name, exec_nbr, exec_pts, exm_pts, tot_pts, grade] 

final_stats = {}


for id, name in student_dict.items():

    full_name = f'{name[0]} {name[1]}' 
    
    exec_nbr = 0
    exec_pts = 0
    exm_pts = 0
    total = 0
    grade = 0

    if id in exercise_dict:
        exec_nbr = sum(exercise_dict[id])
        exec_pts = sum(exercise_dict[id]) // 4
    
    if id in exam_dict:
        exm_pts = sum(exam_dict[id])

    total = exec_pts + exm_pts

    

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
    
    final_stats[id] = [full_name, exec_nbr, exec_pts, exm_pts, total, grade]
    

## print out final dictionary with stats

# print header
header_list = ['name','exec_nbr','exec_pts.','exm_pts.','tot_pts.','grade']
print(f'{header_list[0]:30}', end='')
for col in header_list[1:]:
    print(f'{col:10}', end='')
print('\n', end='')

#print rows
for id, val_list in final_stats.items():
    print(f'{val_list[0]:30}',end='')
    for item in val_list[1:]:
        print(f'{item:<10}',end='')
    print('\n', end='')
