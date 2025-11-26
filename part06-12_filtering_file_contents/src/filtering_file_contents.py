# Write your solution here
folder_input = 'C:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-12_filtering_file_contents\\src\\'
folder_output = 'C:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'

file_input = 'solutions.csv'
file1_output = 'correct.csv'
file2_output = 'incorrect.csv'

input_full = folder_input + file_input
output1_full =  folder_output + file1_output
output2_full = folder_output + file2_output

def clear_file(file:str):
    '''This function opens a file and clears its contents.  If the file doesn't exist it will create it.
    '''
    with open(file,'w') as my_file:
        pass

def filter_solutions():

    #first clear the contents of the output files or create if they don't exist
    clear_file(output1_full)
    clear_file(output2_full)

    problems = []

    #Read the input file and put contents into a list
    with open(input_full,'r') as read_file:
        for line in read_file:
            problems.append(line.strip().split(';'))

    for student in problems:
        
        #Convert list back to string with separator so we can add to .csv file.
        new_line = ''
        for word in student:
            new_line += f'{word};'

        #Check if the problem is addition
        if '+' in student[1]:
            addends = student[1].split('+')
            #if answer is correct, output to the correct.csv file
            if int(addends[0]) + int(addends[1]) == int(student[2]):
                #print(f'Yes, {addends[0]} + {addends[1]} = {student[2]}')
                with open(output1_full,'a') as output1:
                    output1.write(new_line[:-1] +'\n')

            #if answer is wrong, output to incorrect.csv file
            else:
                #print(f'Wrong! {addends[0]} + {addends[1]} != {student[2]}')
                with open(output2_full,'a') as output2:
                    output2.write(new_line[:-1] +'\n')

        #otherwise it should be subtraction.  Repeat similar logic as above for addition
        elif '-' in student[1]:
            minuend = student[1].split('-')
             #if answer is correct, output to the correct.csv file
            if int(minuend[0]) - int(minuend[1]) == int(student[2]):
                #print(f'Yes, {minuend[0]} - {minuend[1]} = {student[2]}')
                with open(output1_full,'a') as output1:
                    output1.write(new_line[:-1] +'\n')

            #if answer is wrong, output to incorrect.csv file
            else:
                #print(f'Wrong! {minuend[0]} - {minuend[1]} != {student[2]}')
                with open(output2_full,'a') as output2:
                    output2.write(new_line[:-1] +'\n')



    #print(problems[0:3])


if __name__ == '__main__':
    filter_solutions()
    print('Program complete')
