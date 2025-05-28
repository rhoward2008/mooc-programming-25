# Write your solution here
str_a = input("1st Letter")
str_b = input("2nd Letter")
str_c = input("3rd Letter")

if (str_c >= str_a >= str_b)  or (str_c <= str_a <= str_b):
    print(f"The letter in the middle is {str_a}")
elif (str_c >= str_b >= str_a)  or (str_c <= str_b <= str_a):
    print(f"The letter in the middle is {str_b}")
elif (str_b >= str_c >= str_a)  or (str_b <= str_c <= str_a):
    print(f"The letter in the middle is {str_c}")