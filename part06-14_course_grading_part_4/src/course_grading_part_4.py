PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-14_course_grading_part_4\\src\\'
OUTPUT_PATH = 'C:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'
DEBUG = True

if DEBUG:
    student_info = 'students1.csv'
    exercise_info = 'exercises1.csv'
    exam_info = 'exam_points1.csv'
    course_info = 'course1.txt'
else:
    student_info = input('Filename for student info: ')
    exercise_info = input('Filename for exercise info: ')
    exam_info = input('Filename for exam info: ')
    course_info = input('Course information: ')

student_path = PATH + student_info
exercise_path = PATH + exercise_info
exam_path = PATH + exam_info
course_path = PATH + course_info

output_txt = OUTPUT_PATH + 'results.txt'
output_csv = OUTPUT_PATH + 'results.csv'


def read_students(file1: str) -> dict:
    '''
    Reads the file with the list of students,
    returns a dictionary 
    key = id from csv.  Value = tuple of (first name,last name)
    '''
    student_dict = {}

    with open(file1, 'r') as student_file:
        for line in student_file:
            student_list = line.split(';')
            if student_list[0] == 'id':
                continue
            else:
                student_dict[student_list[0]] = student_list[1].strip(), student_list[2].strip()
    
    return student_dict

def read_excercises(file2: str) -> dict:
    ''' Read the file with the list of excersices
    returns a dictionary
    key = id from csv.  Value = list of exercise # completed
    ''' 
    exercise_dict = {}

    with open(file2,'r') as exercise_file:
        for line in exercise_file:
            exercise_list = line.split(';')
            if exercise_list[0] == 'id':
                continue
            else:
                exercise_dict[exercise_list[0]] = [int(x.strip()) for x in exercise_list[1:]]
    
    return exercise_dict

def read_exams(file3: str) -> dict:
    ''' Read the file with the list of exams
    returns a dictionary
    key = id from csv.  Value = list of exam points
    ''' 
    exam_dict = {}

    with open(file3,'r') as exam_file:
        for line in exam_file:
            exam_list = line.split(';')
            if exam_list[0] == 'id':
                continue
            else:
                exam_dict[exam_list[0]] = [int(x.strip()) for x in exam_list[1:]]

    return exam_dict

def read_course(file4: str) -> tuple:
    '''
    Function to read course file, returns tuple with course name and study credits
    '''
    name = ''
    credits = ''

    with open(file4, 'r') as course_file:
        for line in course_file:
            course_list = line.split(':')
            if course_list[0] == 'name':
                name = course_list[1].strip()
            elif course_list[0] == 'study credits':
                credits = course_list[1].strip()
        
    
    course_tuple = name,credits
    
    #print(f'info: {course_tuple}')

    return course_tuple

def final_stats(student_dict: dict, exercise_dict: dict, exam_dict: dict) -> dict:
    '''
    Function to calculate the final statistics.  Input dictionaries for students, exercises, and exams.
    Return dictionary in this format:
    Format is: id: [name, exec_nbr, exec_pts, exm_pts, tot_pts, grade] 
    '''


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
    
    return final_stats

def write_results(final_stats, course):
    '''
    Write results to 2 files, results.txt and results.csv
    '''
    #First create and write to text file
    with open(output_txt ,'w') as txt_file:
        #write course name and credits
        txt_file.write(f'{course[0]}, {course[1]} credits\n')
        txt_file.write('======================================\n')

        # write header columns
        header_list = ['name','exec_nbr','exec_pts.','exm_pts.','tot_pts.','grade']
        txt_file.write(f'{header_list[0]:30}')
        for col in header_list[1:]:
            txt_file.write(f'{col:10}')
        txt_file.write('\n')

        #write student results 
        for id, val_list in final_stats.items():
            txt_file.write(f'{val_list[0]:30}')
            for item in val_list[1:]:
                txt_file.write(f'{item:<10}')
            txt_file.write('\n')

    
    #Second create and write to csv file
    with open(output_csv,'w') as csv_file:
        #write student data to csv file
        for id,val_list in final_stats.items():
            line = id + ';' + str(val_list[0]) + ';' + str(val_list[-1]) + '\n'
            csv_file.write(line)
            

#print(read_students(student_path))
#print(read_excercises(exercise_path))
#print(read_exams(exam_path))
stats = final_stats(read_students(student_path), read_excercises(exercise_path), read_exams(exam_path))
course = read_course(course_path)

write_results(stats,course)

