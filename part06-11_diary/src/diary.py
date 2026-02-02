# Write your solution here
folder = 'C:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'
file_name = 'diary.txt'
full_path = folder + file_name

while True:
    try:
        choice = int(input('1 - add an entry, 2 - read entries, 0 - quit\nFunction: '))
    except ValueError:
        print('Invalid entry')
        continue

    if choice == 1: # add to file
        diary = input('Diary entry: ')
        with open(full_path,'a') as file_handle:
            file_handle.write(diary +'\n')
        print('Diary saved')

    elif choice == 2: #read file
        try: 
            with open(full_path,'r') as file_handle:
                text = file_handle.read()
                print(f'Entries:\n{text}')
            print('Diary saved')

        except FileNotFoundError:
            print('File not found')

    elif choice == 0: #quit
        print('Bye now!')
        break

    else:
        print('Invalid entry')