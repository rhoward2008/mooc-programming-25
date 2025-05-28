# Write your solution here
# You can test your function by calling it within the following block
def mean(my_list:list) -> float:
    '''Returns the mean of a list'''
    return sum(my_list) / len(my_list)


if __name__ == "__main__":
    my_list = [1,2,3,4,5,10]
    result = mean(my_list)
    print(result)