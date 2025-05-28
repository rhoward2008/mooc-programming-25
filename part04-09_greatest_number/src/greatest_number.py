# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(a: int, b: int, c:int):
    numbers = sorted([a,b,c])
    return numbers[-1]


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)