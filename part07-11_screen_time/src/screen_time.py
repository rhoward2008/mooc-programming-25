from datetime import datetime, timedelta

PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part07-11_screen_time\\'

def screentime():
    file = input('Filename: ')
    full_path = PATH + file
    #full_path = PATH + 'screen_time.txt'

    input_date = input('Starting Date dd.mm.yyyy: ')
    start_date = datetime.strptime(input_date, '%d.%m.%Y')

    days = int(input('How many days?: '))

    screen_time = []
    date_list = []

    for i in range(days):
        day_loop = start_date + timedelta(days=i)
        date_var = day_loop.strftime('%d.%m.%Y')
        date_list.append(date_var)
        input_time = input(f'Screen time {date_var}: ')
        screen_minutes = tuple(int(x) for x in input_time.split(' '))
        #print(f'i: {input_time}')
        #print(f'{screen_minutes}')
        screen_time.append(screen_minutes)
    
    #Take screen_time list and calculate total and aaverage
    total_min = 0
    for x in screen_time:
        for y in x:
            total_min += y 
    avg_min = total_min / days
    
    #print(avg_min)
    #print(screen_time)
    #print(date_list)

    #output results to file
    with open(full_path, 'w') as file_handle:
        file_handle.write(f'Time period: {date_list[0]}-{date_list[-1]}\n')
        file_handle.write(f'Total minutes: {total_min}\n')
        file_handle.write(f'Average minutes: {avg_min}\n')
        for i in range(days):
            file_handle.write(f'{date_list[i]}: {screen_time[i][0]}/{screen_time[i][1]}/{screen_time[i][2]}\n')

    print(f'File {file} created.')



if __name__ == '__main__':
    screentime()