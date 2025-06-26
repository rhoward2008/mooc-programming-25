# Write your solution here
def times_ten(start_index: int, end_index: int):
    new_dict = {}
    for x in range(start_index, end_index+1):
        new_dict[x] = x*10
    
    return new_dict



if __name__ == "__main__":
    dict = times_ten(3,6)
    print(dict)