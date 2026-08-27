from datetime import datetime, timedelta

PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part07-14_who_cheated\\src\\'

start_file = PATH + 'start_times.csv'
end_file = PATH + 'submissions.csv'

def cheaters() -> list:
    '''
    This function reads two csv files.  First one has a list of students with start times.
    Second one contains a list students with points and hand in times.
    Returns a list of cheaters who handed in a task over 3 hours later.

    '''

    start_dict = {}
    end_dict = {}
    cheat_list = []

    # Read in the start file and create a dictionary
    with open(start_file, 'r') as start_fhandle:
        for line in start_fhandle:
            start_list = line.strip().split(';')
            hour = start_list[1][0:2]
            minute = start_list[1][3:]
            time_string = hour + ':' + minute
            start_dict[start_list[0]] = datetime.strptime(time_string, '%H:%M')

    # Read in the submissions file and create a dictionary
    with open(end_file, 'r') as end_fhandle:
        for line in end_fhandle:
            end_list = line.strip().split(';')
            student = end_list[0]
            hour = end_list[3][0:2]
            minute = end_list[3][3:]
            time_string = hour + ':' + minute
            end_time = datetime.strptime(time_string,'%H:%M')
           
            #Check if the student already exists in the dictionary.  
            #If yes then only add end_time if it is less than the existing time
            if student in end_dict:
                #If new task time is less existing time, update it
                if end_time < end_dict[student]:
                    end_dict[student] = end_time
            else:
                end_dict[student] = end_time
    
    # Now loop through the dictionary and see who cheated by turning in over 3 hours from start.
  
    for student,start_time in start_dict.items():
        end_time = end_dict.get(student)
        if end_time is not None:
            if start_time + timedelta(hours=3) < end_time:
                cheat_list.append(student)

    return cheat_list

if __name__ == '__main__':
    cheater_list = cheaters()
    print(cheater_list)