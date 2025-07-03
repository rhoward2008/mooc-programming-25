# Write your solution here
# Write your solution here
phone_dict = {}

while True:
    num_input = int(input('command (1 search, 2 add, 3 quit): '))

    if num_input == 1:
        search_name = input('name: ')
        if search_name in phone_dict:
            for num in phone_dict[search_name]:
                print(num)
        else:
            print('no number')
    elif num_input == 2:
        add_name = input('name: ')
        add_number = input('number: ')
        print('ok!')
        if add_name not in phone_dict:
            phone_dict[add_name] = [add_number]
        else:
            phone_dict[add_name].append(add_number) 
    elif num_input == 3:
        print('quitting...')
        break
    else:
        print('Invalid input.')


#print(f'phonebook: {phone_dict}')