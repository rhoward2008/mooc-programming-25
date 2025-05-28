# Write your solution here
def everything_reversed(input_list:list) -> list:
    reversed = []
    for i in input_list[::-1]:
        reversed.append(i[::-1])
    
    return reversed

if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)