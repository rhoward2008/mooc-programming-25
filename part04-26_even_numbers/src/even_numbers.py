# Write your solution here
def even_numbers(list_evens:list) -> list:
    evens_only = []
    for num in list_evens:
        if num % 2 == 0:
            evens_only.append(num)
    
    return evens_only


if __name__ == '__main__':
    my_list = [1,2,3,4,5]
    new_list = even_numbers(my_list)
    print(f'original: {my_list}')
    print(f'new: {new_list}')