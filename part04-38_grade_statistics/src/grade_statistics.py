# Write your solution here
def input_grades() -> list:
    '''
        This function asks the user to input the exam points and exercises completes
        The function returns a list of lists in this format: [[exam1,exercise1],[exam2,exercise2]...]
    '''
    grades = []
    while True:
        exam = input('Exam points and exercises completed: ')
        if exam:
            exam_split = exam.split(' ')
            if len(exam_split) == 2:
                grades.append([int(exam_split[0]),int(exam_split[1])])
            else:
                print("Invalid input")
        else:
            break
    
    return grades


def exercise_points(completed:int) -> int:
    '''
        This function calculates the exercises points based on the number of exercises completed.
        Input is exercies compelted and return value is points based on this guideline:
        10% completed: 1 points
        20% compelted: 2 points
        ...
        100% completed: 10 points
        The maximum number of points is 10
    '''
        
    points = completed // 10



    return min(points,10) #You can't get more than 10 points

def grade(exam:int, points:int) -> int:
    '''
        This function calculates the final grade based on the exam points and exercise points        
    '''

    #If exam points are less than 10 you automatically fail
    grade = 0
    total = exam + points
    
    if exam < 10:
        pass
    elif 15 <= total <= 17:
        grade = 1
    elif 18 <= total <= 20:
        grade = 2
    elif 21 <= total <= 23:
        grade = 3
    elif 24 <= total <= 27:
        grade = 4
    elif 28 <= total <= 30:
        grade = 5

    return grade

def class_grades(input_grades:list) -> list:
    '''
        This function inputs the list of exam points and excercises completed (output from input_grade)
        and uses helper functions to create a new list in this format: [[total_points1,grade1],[total_points2,grade2]]
        This will be used later for the stats function and grade distribution

        Input list in this format: [[exam1,exercise1],[exam2,exercise2]]
    '''
    class_grades = []
    total_points = 0
    final_grade = 0

    for student in input_grades:
        #print(f'{student}')
        total_points = student[0] + exercise_points(student[1])
        final_grade = grade(student[0],exercise_points(student[1]))
        #print(f'Total points:{total_points}')
        #print(f'grade: {final_grade}')
        class_grades.append([total_points,final_grade])
    
    return class_grades


def stats(points_grades:list):
    '''
        This function take a list of all grades and points prints out the points average and pass % for the class.
        Input is a list in this format [[points1,grade1],[points2,grade2],[points3,grade3]]
    ''' 
    #First find the points average which is sum total points for all student / number of students
    points_total = 0
    count = len(points_grades)

    for point in points_grades:
        #print(f'point: {point}')
        points_total += point[0]
    
    points_avg = points_total / count
    #print(points_avg)

    #Second find the pass total.  Pass means a score of 1 or higher
    pass_total = 0

    for grade in points_grades:
        #print(f'grade: {grade}')
        if grade[1] > 0:
            pass_total += 1

    pass_percentage = (pass_total / count) * 100

    print('Statistics:')
    print(f'Points average: {points_avg:.1f}')
    print(f'Pass percentage: {pass_percentage:.1f}')


def grade_distribution(grades:list):
    grade_dict = {5:0,
                 4:0,
                 3:0,
                 2:0,
                 1:0,
                 0:0
                 }
    
    for i in grades:
       grade_dict[i] += 1

    print('Grade distribution:')
    for key,value in grade_dict.items():
        print(f'{key}:',end=' ')
        for x in range(value):
            print('*',end ='')
        print('')
        

def main():
    '''
        This is the main function which defines the flow of the program and call the helper funcitons
    '''
    raw_score = input_grades()

    points_grade = class_grades(raw_score)

    #print(f'Raw score: {raw_score}')
    #print(f'Final grade: {points_grade}')

    stats(points_grade)

    grades_list = [x[1] for x in points_grade] 
    grade_distribution(grades_list)

#Call the main function
main()

