from datetime import datetime, timedelta

PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part07-15_who_cheated_2\\src\\'

start_file = PATH + 'start_times.csv'
submissions_file = PATH + 'submissions.csv'

def final_points() -> dict:
    #points_dict will contain a subdictionary for each student with a list of tasks and scores
    # {'jarmo': {1: 8, 2: 10},
    #  'timo': {2: 10, 3: 20}          
    # }
    points_dict = {}
    start_dict = {}

    # Read in the start file and create a dictionary of start times
    with open(start_file, 'r') as start_fhandle:
        for line in start_fhandle:
            start_list = line.strip().split(';')
            hour = start_list[1][0:2]
            minute = start_list[1][3:]
            time_string = hour + ':' + minute
            start_dict[start_list[0]] = datetime.strptime(time_string, '%H:%M')

    #Read in the submissions file and create the points dictionary
    with open(submissions_file, 'r') as sub_fhandle:
        for line in sub_fhandle:
            submission_list = line.strip().split(';') #should look like this: [name, task#, point, endtime]
            student = submission_list[0]
            task = submission_list[1]
            points = int(submission_list[2])
            end_time = datetime.strptime(submission_list[3],'%H:%M')

            #First check end time.  If over 3 hours past start, ignore
            if start_dict[student] + timedelta(hours=3) > end_time:
                #If student not in points_dict, add them with empty task sub-dictionary
                if student not in points_dict:
                    points_dict[student] = {}
           
                #If the task is repeated, choose the highest point value
                #Use 0 as placeholder value in case this is the first instance of the task (get would return NULL without the default value)
                #print(f'existing value: {student} task: {task}')
                points_dict[student][task] = max(points_dict[student].get(task,0), points )


    #final_dict will look at the points_dict and calcuate the total points for each student
    # {'jarmo': 18, 
    # 'timo': 30}
    final_dict = {}

    for student, pointer in points_dict.items():
        final_dict[student] = sum(pointer.values())

    return final_dict


if __name__ == '__main__':
    answer = final_points()
    print(answer)