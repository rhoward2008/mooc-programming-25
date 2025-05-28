# Write your solution here
mylist = [1,2,3,4,5]

index = 0

while True:
    index = int(input("Index: ")) 
    if index == -1:
        break
    new = int(input("New value:"))
    if 0 <= index < len(mylist):
        mylist[index] = new
    print(mylist)
