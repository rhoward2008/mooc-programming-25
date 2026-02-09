PATH_INPUT = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
PATH_OUTPUT = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'

input_file = PATH_INPUT + 'lottery_numbers.csv'
output_file = PATH_OUTPUT + 'correct_numbers.csv'

def check_numbers(all_nums:list) -> bool:
    '''
    This is a helper function to check if the lottery number list meets all criteria.
    1. Must contain exactly 7 numbers
    2. Number must be between 1 and 39 (inclusive)
    3. A number cannot repeat
    '''
    #Should contain exactly seven numbers
    if len(all_nums) != 7:
        return False
    
    number_set = set()

    for x in all_nums:
        #Number must be between 1 and 39
        if x>39 or x<1:
            return False
        
        #check if number already exists
        if x in number_set:
            return False
        else:
            number_set.add(x)
    
    #If all checks above pass, return True
    return True


def filter_incorrect():
    valid_weeks = []

    with open(input_file, 'r') as input_handle:
        for line in input_handle:
            split = line.strip().split(';')
            #print(f'split: {split}')
            try:
                week = int(split[0][5:])
                numbers = [int(x) for x in split[1].split(',')]
                #print(f'week: {week} \n numbers: {numbers}')
                #print(f'No value error week = {week}, {numbers}')

                if check_numbers(numbers):
                    valid_weeks.append((week,numbers))
                
            except ValueError:
                continue

        #for x in valid_weeks:
        #    print(f'week: {x[0]}   {x[1]}')

    #Now write results to file
    with open(output_file, 'w') as output_handle:
        for line in valid_weeks:
            new_line = f'week {line[0]};'
            new_nums = ''
            for x in line[1]:
                new_nums = new_nums + str(x) + ','

            new_line = new_line + new_nums[0:len(new_nums)-1] #Remove comma at the end
            
            output_handle.write(f'{new_line}\n')
            
            

if __name__ == '__main__':
    filter_incorrect()
    print('File created')