# Write your solution here
number = int(input("Please type in a number:"))

outer = 1
while outer <= number:
    inner = 1
    while inner <= number:
        print(f'{outer} x {inner} = {outer*inner}')
        inner += 1
    outer += 1
