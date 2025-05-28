# Write your solution here
# You can test your function by calling it within the following block
def range_of_list(input_list:list[int]) -> int:
    return max(input_list) - min(input_list)


if __name__ == "__main__":
    my_list = [1,2,3,4,5,100]
    result = range_of_list(my_list)
    print(result)