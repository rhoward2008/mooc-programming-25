# Write your solution here
def remove_smallest(numbers: list):
    smallest = sorted(numbers)[0]
    numbers.remove(smallest)
    #print(f'list: {numbers} ** smallest: {smallest}')

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)