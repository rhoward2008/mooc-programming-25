# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word:str, num1:int, num2:int) -> bool:
    if num1 < 0 or num2 < 0 or num1 >= len(word) or num2 >= len(word):
        return False
    elif word[num1] == word[num2]:
        return True
    else:
        return False
    



if __name__ == "__main__":
    print(same_chars("programmer", 4, 1))