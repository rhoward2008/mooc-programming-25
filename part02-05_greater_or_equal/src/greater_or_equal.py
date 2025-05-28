# Write your solution here
num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in another number:"))

if num1 > num2:
    print(f"The greater number is {num1}")
elif num2 > num1:
    print(f"The greater number is {num2}")
else:
    print("The numbers are equal!")