# Write your solution here
number = int(input("Please type in a number:"))

i = 1
j = 2

while i <= number:
    if j > number:
        print(i)
    else:
        print(j)
        print(i)
    i += 2
    j += 2