# write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'

#if True:
student_info = input('Filename for student info: ')
exercise_info = input('Filename for exercise info: ')
#else:
#    student_info = 'students1.csv'
#    exercise_info = 'exercises1.csv'

student_path = PATH + student_info
exercise_path = PATH + exercise_info


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


for id, name in student_dict.items():
    if id in exercise_dict:
        total = sum(exercise_dict[id])
        print(f'{name[0]} {name[1]}: {total}')
            

