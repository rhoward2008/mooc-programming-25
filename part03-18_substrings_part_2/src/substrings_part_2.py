# Write your solution here
mystring = input("Please type in a string:")

for i in range(len(mystring)):
    print(mystring[len(mystring)-i-1:])