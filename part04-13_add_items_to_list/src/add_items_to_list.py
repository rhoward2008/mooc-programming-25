# Write your solution here
num_items = int(input("How many items: "))

my_list = []

for i in range(num_items):
    x = int(input(f"Item {i+1}: "))
    my_list.append(x)

print(my_list)
