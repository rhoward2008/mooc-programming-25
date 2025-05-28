# Write your solution here
def longest_series_of_neighbours(my_list:list) -> int:
    longest = 0
    counter = 0
    last = ''

    for i,value in enumerate(my_list):
        #print(f'Start: i={i}, value={value} longest={longest}, count={counter}, last={last}')
        if i > 0:
            if abs(value - last) == 1:
                counter += 1
                if counter > longest:
                    longest = counter
            else:
                counter = 0

        last = value 
        #print(f'End: longest={longest}, count={counter}, last={last}')

    return longest+1

if __name__ == '__main__':
    my_list = [1, 2, 3,1,2,1,2,0,1,2,3,4,5]
    print(longest_series_of_neighbours(my_list))