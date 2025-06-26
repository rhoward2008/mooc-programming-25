# Write your solution here
def longest(strings:list) -> str:
    '''This function takes a list of strings as input and returns the longest one in the list'''
    
    #initialize to the first value in the list
    longest = strings[0]

    for i in strings:
        if len(i) > len(longest):
            longest = i
    
    return longest

if __name__ == "__main__":
    #strings = ["hi", "hiya", "hello", "howdydoody", "hi there","sdfffffffffffffffffffff"]
    strings = ["s", "hiya", "hello", "howdydoody", "hi there",""]
    print(longest(strings))