# Write your solution here
def sum_of_positives(list_int:list[int]) -> int:
    total = 0
    for val in list_int:
        if val > 0:
            total += val
    
    return total


if __name__ == '__main__':
    my_list = [1,-2,3,-4,5]
    result = sum_of_positives(my_list)
    print(f'The result is {result}')