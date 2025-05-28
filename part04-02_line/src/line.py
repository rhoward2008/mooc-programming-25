# Write your solution here
# You can test your function by calling it within the following block
def line(num: int, word: str):
    if len(word) > 0:
        print(word[0]*num)
    else:
        print("*"*num)


if __name__ == "__main__":
    line(7, "%")
    line(3,"")