# write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
#PATH = 'c:\\Users\\bension\\UHelsinki\\PythonIntro\\tmcdata\\mooc-programming-25\\part06-01_largest_number\\src\\'
full_path = PATH + 'numbers.txt'


def largest():
    ##with open('numbers.txt','r') as new_file:
    with open(full_path,'r') as new_file:
        
        largest = int(new_file.readline().replace('\n',''))

        #print(f'Var is initialized to the first line: {largest}')
        
        for line in new_file:
            new_line = int(line.replace('\n',''))

            if new_line > largest:
                largest = new_line


        
        return largest



if __name__ == '__main__':
    biggest_num = largest()
    print(f'Largest number in file is: {biggest_num}')