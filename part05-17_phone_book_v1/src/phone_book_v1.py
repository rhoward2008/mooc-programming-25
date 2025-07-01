# Write your solution here
phone_dict = {}

while True:
    num = int(input('command (1 search, 2 add, 3 quit): '))

    if num == 1:
        search_name = input('name: ')
        if search_name in phone_dict:
            print(phone_dict[search_name])
        else:
            print('no number:')
    elif num == 2:
        add_name = input('name: ')
        add_number = input('number: ')
        print('ok!')
        phone_dict[add_name] = add_number 
    elif num == 3:
        print('quitting...')
        break
    else:
        print('Invalid input.')


#print(f'phonebook: {phone_dict}')